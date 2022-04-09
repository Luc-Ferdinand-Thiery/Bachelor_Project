#C-Node
#Stores all Data & sends it to all other nodes

from hashlib import sha256
import json
import time

from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15

from cryptography.fernet import Fernet
import cryptography

from flask import Flask, request
import requests

from files.Node.Admins import *

app = Flask(__name__)
# the address to other participating members of the network
peers = set()


#C-Node
#Stores all Data & sends it to all other nodes

##############################################
#List of Admins Adresses and Their Public Key
df = pandas.read_csv('Admins.csv')
data={}
for i in df.index:
    data["address"]=df.iloc[i][0]
    data["private_key"] = df.iloc[i][1]
    data["public_key"] = df.iloc[i][2]

Genesis_Admins = json.dumps(data)
##############################################


#my Wallet
My_Wallet=wallet()
My_Wallet.load(df.iloc[0][0],df.iloc[0][1],df.iloc[0][2])

print(My_Wallet.address, My_Wallet.private_key, My_Wallet.public_key)
print(data)

################# Functions #############################

#returns all admins
#check
def get_admins():
    addresses={}
    for block in blockchain.chain:
        for address in block.admins:
            pubkey=block.admins[address]
            addresses[address]=pubkey
    return addresses

#returns all unverified users
#check
def get_unverfied_addresses():
    addresses={}
    for block in blockchain.chain:
        for hash in block.unverified_addresses:
            prefix=block.unverified_addresses[hash]
            addresses[hash]=prefix
    return addresses

#returns all verified users
#check
def get_verfied_addresses():
    addresses={}
    for block in blockchain.chain:
        for address in block.verified_addresses:
            pubkey=block.verified_addresses[address][0]
            token = block.verified_addresses[address][1]
            addresses[address]=[pubkey,token]
    return addresses

#validates if a signature is valid or not
#check
def validate_signature(public_key, signature, data:dict):
    if isinstance(public_key, str) and isinstance(signature, str):
        public_key=ast.literal_eval(public_key)
        signature=ast.literal_eval(signature)


    data_byte= json.dumps(data, indent=2).encode('utf-8')
    public_key_object = RSA.import_key(public_key)
    data_hash = SHA256.new(data_byte)
    try:
        pkcs1_15.new(public_key_object).verify(data_hash, signature)
        return True
    except (ValueError, TypeError):
        #error signature not correct
        return False

#creates a signature
#check
def create_signature(Data, Private_Key):
    bytes=json.dumps(Data, indent=2).encode('utf-8')
    hash_object = SHA256.new(bytes)
    signature = pkcs1_15.new(Private_Key).sign(hash_object)

    return signature

#create the chain
#check
def create_chain_from_dump(chain_dump):
    generated_blockchain = Blockchain()
    generated_blockchain.create_genesis_block()
    for idx, block_data in enumerate(chain_dump):
        if idx == 0:
            continue  # skip genesis block
        block = Block(block_data["owner"],
                      block_data["signature"],
                      block_data["index"],
                      block_data["timestamp"],
                      block_data["previous_hash"],
                      block_data["admins"],
                      block_data["ballots"],
                      block_data["addresses"],
                      block_data["transactions"],
                      block_data["nonce"])

        data = {"index": block_data["index"],
                "timestamp": block_data["timestamp"],
                "previous_hash": block_data["previous_hash"],
                "admins": block_data["admins"],
                "unverified_addresses": block_data["unverified_addresses"],
                "verified_addressees": block_data["verified_addresses"],
                "votes": block_data["votes"]}


        if validate_signature(block_data["owner"], block_data["signature"], data) == False:
            raise Exception("The chain dump is tampered!!")

        proof = block_data['hash']
        added = generated_blockchain.add_block(block, proof)
        if not added:
            raise Exception("The chain dump is tampered!!")
    return generated_blockchain

#check for longest chain -> consensus algorithm
#check
def consensus():
    """
    Our naive consensus algorithm. If a longer valid chain is
    found, our chain is replaced with it.
    """
    global blockchain

    longest_chain = None
    current_len = len(blockchain.chain)

    for node in peers:
        response = requests.get('{}chain'.format(node))
        length = response.json()['length']
        chain = response.json()['chain']
        if length > current_len and blockchain.check_chain_validity(chain):
            current_len = length
            longest_chain = chain

    if longest_chain:
        blockchain = longest_chain
        return True

    return False

#send new block to other partys
#check
def announce_new_block(block):
    """
    A function to announce to the network once a block has been mined.
    Other blocks can simply verify the proof of work and add it to their
    respective chains.
    """
    for peer in peers:
        url = "{}add_block".format(peer)
        headers = {'Content-Type': "application/json"}
        requests.post(url,
                      data=json.dumps(block.__dict__, sort_keys=True),
                      headers=headers)


################# Block and Blockchain Objects #############################
#check
class vote:
    def __init__(self, address, data, signature):
        self.address=address
        self.data = data
        self.signature = signature #
#check
class Block:
    def __init__(self, owner, signature, index, timestamp, previous_hash, admins, unverified_addresses, verified_addresses, votes, nonce=0):

        #Block Owner
        self.owner = owner
        self.signature = signature

        #Block Meta Data
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce #nonce not included in signature


        #Block Data
        self.admins = admins #stores all admins to become C-Node -> "Address":pubkey
        self.unverified_addresses = unverified_addresses    # "hash":"prefix"
        self.verified_addresses = verified_addresses        # "Address":[pub_key,token]
                                                                        #token = 1 -> can vote
                                                                        # token = 0 -> can't vote
        self.votes = votes


    def compute_hash(self):
        #A function that returns the hash of the block contents.
        block_str = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_str.encode()).hexdigest()
#check
class Blockchain:
    # difficulty of our PoW algorithm
    difficulty = 2

    def __init__(self):
        self.unconfirmed_admins = {}    #"address":pub_key
        self.unconfirmed_votes = []
        self.unconfirmed_unverified_addresses = {}  # "hash":"prefix"
        self.unconfirmed_verified_addresses = {}    # "Address":[pub_key,token]
                                                                        #token = 1 -> can vote
                                                                        # token = 0 -> can't vote
        self.chain = [] #all transactions

    def create_genesis_block(self):
        """
        Method to create Genesis Block
        """
        #Data -> Nonce by default=0
        Data={"index":0,
              "timestamp":0,
              "previous_hash":0,
              "admins":Genesis_Admins,
              "unverified_addresses":[],
              "verified_addresses":[],
              "votes":[]} #Data From Genesis Block without Nonce
        #creates a signature for the block data
        signature=create_signature(Data,My_Wallet.private_key)


        g_block = Block(
            owner=My_Wallet.address,
            signature=signature,
            index=0,
            timestamp=0,
            previous_hash=0,
            admins=Genesis_Admins,
            unverified_addresses = self.unconfirmed_unverified_addresses,
            verified_addresses = self.unconfirmed_verified_addresses,
            votes=self.unconfirmed_votes)

        g_block.hash = g_block.compute_hash()
        self.chain.append(g_block)

    @property
    def last_block(self):
        return self.chain[-1]

    def add_block(self, block, proof):
        """
        A function that adds the block to the chain after verification.
        Verification includes:
        * Checking if the proof is valid.
        * The previous_hash referred in the block and the hash of latest block
          in the chain match.
        """
        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False

        if not Blockchain.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    @staticmethod
    def proof_of_work(block):
        """
        Function that tries different values of nonce to get a hash
        that satisfies our difficulty criteria.
        """
        block.nonce = 0

        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()

        return computed_hash

    @classmethod
    def is_valid_proof(cls, block, block_hash):
        """
        Check if block_hash is valid hash of block and satisfies
        the difficulty criteria.
        """
        return (block_hash.startswith('0' * Blockchain.difficulty) and
                block_hash == block.compute_hash())

    @classmethod
    def check_chain_validity(cls, chain):
        result = True
        previous_hash = "0"

        for block in chain:
            block_hash = block.hash
            # remove the hash field to recompute the hash again
            # using `compute_hash` method.
            delattr(block, "hash")

            if not cls.is_valid_proof(block, block_hash) or \
                    previous_hash != block.previous_hash:
                result = False
                break

            block.hash, previous_hash = block_hash, block_hash

        return result

    #################### Data Adding ######################################

    # new admin gets added
    def add_new_admin(self, admin_address, pub_key):
        self.unconfirmed_votes[admin_address]=pub_key

    #new vote gets added
    def add_new_vote(self, vote):
        self.unconfirmed_votes.append(vote)

    #new Address gets added
    def add_new_unverified_addresses(self,unverified_addresses, prefix):
        self.unconfirmed_unverified_addresses[unverified_addresses]=prefix

    #new verified Address gets added
    def add_new_verified_addresses(self, verified_addresses, pubkey):
        self.unconfirmed_verified_addresses[verified_addresses]=[pubkey, 1] #1 stands for token

    #person has added
    def check_of_voter(self, checked_addresses, pubkey):
        self.unconfirmed_verified_addresses[checked_addresses] = [pubkey, 0]  #0 stands for no token


    ################### Mining #########################
    #check
    def mine(self):
        """
        This function serves as an interface to add the pending
        transactions to the blockchain by adding them to the block
        and figuring out Proof Of Work.
        """
        if not self.unconfirmed_votes and not self.unconfirmed_unverified_addresses and not self.unconfirmed_verified_addresses and not self.unconfirmed_admins:
            return False


        last_block = self.last_block
        timestamp=time.time()

        # Data From Genesis Block without Nonce
        Data = {"index": last_block.index + 1,
                "timestamp": timestamp,
                "previous_hash": last_block.hash,
                "admins": self.unconfirmed_admins,
                "unverified_addresses": self.unconfirmed_unverified_addresses,
                "verified_addresses": self.unconfirmed_verified_addresses,
                "votes": self.unconfirmed_votes}
        signature = create_signature(Data, My_Wallet.private_key)

        new_block = Block(
            owner=My_Wallet.address,
            signature=signature,
            index=last_block.index + 1,
            timestamp=timestamp,
            previous_hash=last_block.hash,
            admins=self.unconfirmed_admins,
            unverified_addresses=self.unconfirmed_unverified_addresses,
            verified_addresses=self.unconfirmed_verified_addresses,
            votes=self.unconfirmed_votes)

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)

        self.unconfirmed_votes = []
        self.unconfirmed_unverified_addresses = {}
        self.unconfirmed_verified_addresses = {}
        self.unconfirmed_admins = {}

        return True
############################################################################

# the node's copy of blockchain
blockchain = Blockchain()
blockchain.create_genesis_block()







################# Data API endpoints#############################

################ POST #################################
# endpoint to vote -> check if vote is eligible
#check
@app.route('/vote', methods=['POST'])
def vote():
    Addresses=get_verfied_addresses()

    user_address = request.get_json()["user_address"]       #user addresse
    user_signature = request.get_json()["signature"]        #signature
    vote = request.get_json()["vote"]                       #vote as whole
    ballot = request.get_json()["ballot"]                   #just the ballot

    if not user_address:
        return "Invalid data", 400
    if not user_signature:
        return "Invalid data", 400
    if not vote:
        return "Invalid data", 400
    if not ballot:
        return "Invalid data", 400

    #object vote:   [
    #                   address=user_address
    #                   data=ballot
    #                   signature=user_signature
    #               ]

    for i in Addresses:
        if i == user_address:
            if Addresses[i][1]==1: #check if user still has a token
                if validate_signature(user_address, user_signature, vote) == True: #if signature is validated
                    pub_key=Addresses[i][0]

                    new_vote=vote(user_address, ballot, user_signature) #creates new object
                    blockchain.add_new_vote(new_vote) #adds the vote object to other votes
                    blockchain.check_of_voter(user_address,pub_key) #adds another instance of the voter to the address
                    return "success", 200
                return "Invalid Signature", 400
            return "Already Voted", 400
        return "Address not found", 400
#check
@app.route('/verify', methods=['POST'])
def verify():
    #Fernet sha 256 encryption

    #"hash":prefix
    #hash->{address:address,
    #       pub_key:pubkey}

    prefix = request.get_json()["prefix"]  # user addresse
    f = Fernet(request.get_json()["password"])#creates key

    if not prefix:
        return "Invalid data", 400

    if not f:
        return "Invalid data", 400

    Addresses = get_unverfied_addresses()

    for i in Addresses:
        if Addresses[i]==prefix:
            try:
                decrypted = f.decrypt(i) #decryptes with key
                dict1 = json.loads(decrypted)
                address=dict1["address"]
                pub_key=dict1["pubkey"]

                blockchain.add_new_verified_addresses(address,pub_key)

                return "Success, Address is Now activated!", 200
            except (cryptography.fernet.InvalidToken, TypeError):
                return "Wrong Password", 400
        return "Wrong Prefix", 400
#check
#admins
@app.route('/add_user', methods=['POST'])
def add_user():
    admin_address = request.get_json()["admin_address"]
    admin_signature = request.get_json()["admin_signature"]
    data = request.get_json()["data"]

    #data-> "{  "hash":hash,
    #           "prefix":prefix}"

    if not admin_address:
        return "Invalid data", 400
    if not admin_signature:
        return "Invalid data", 400
    if not data:
        return "Invalid data", 400

    # Checks if User and Signature is correct -> public key verification

    Admins=get_admins()

    for i in Admins:
        if i == admin_address:
            p_key=Admins[i]
            if validate_signature(p_key, admin_signature, data) == True:
                dict1 = json.loads(data)
                blockchain.add_new_unverified_addresses(dict1["hash"], dict1["prefix"])
            return "Invalid User", 400

        return "Invalid User", 400

# endpoint to add a block mined by someone else to
# the node's chain. The block is first verified by the node
# and then added to the chain.
#check
@app.route('/add_block', methods=['POST'])
def verify_and_add_block():
    admin_address = request.get_json()["admin_address"]
    admin_signature = request.get_json()["admin_signature"]

    Admins = get_admins()

    block_data = request.get_json()

    data={"index":block_data["index"],
          "timestamp":block_data["timestamp"],
          "previous_hash":block_data["previous_hash"],
          "admins":block_data["admins"],
          "unverified_addresses":block_data["unverified_addresses"],
          "verified_addressees":block_data["verified_addresses"],
          "votes":block_data["votes"]}



    for i in Admins:
        if i == admin_address:
            p_key = Admins[i]
            if validate_signature(p_key, admin_signature, data) == True:
                dict1 = json.loads(data)
                blockchain.add_new_unverified_addresses(dict1["hash"], dict1["prefix"])
            return "Invalid User", 400

        return "Invalid User", 400

    if validate_signature(block_data["owner"],block_data["signature"],data) == False:
        return "The block was discarded by the node: Invalid Signature", 400



    block = Block(owner=block_data["owner"],
                  signature=block_data["signature"],
                  index=block_data["index"],
                  timestamp=block_data["timestamp"],
                  previous_hash=block_data["previous_hash"],
                  admins=block_data["admins"],
                  unverified_addresses=block_data["unverified_addresses"],
                  verified_addresses=block_data["verified_addresses"],
                  votes=block_data["votes"])



    proof = block_data['hash']
    added = blockchain.add_block(block, proof)

    if not added:
        return "The block was discarded by the node", 400

    return "Block added to the chain", 201









################ GET #################################

# endpoint to return the node's copy of the chain.
# Our application will be using this endpoint to query
# all the posts to display.
#check
@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data,
                       "peers": list(peers)})


# endpoint to request the node to mine the unconfirmed
# transactions (if any). We'll be using it to initiate
# a command to mine from our application itself.
@app.route('/mine', methods=['GET'])
def mine_unconfirmed_transactions():
    result = blockchain.mine()
    if not result:
        return "No transactions to mine"
    else:
        # Making sure we have the longest chain before announcing to the network
        chain_length = len(blockchain.chain)
        consensus()
        if chain_length == len(blockchain.chain):
            # announce the recently mined block to the network
            announce_new_block(blockchain.last_block)
        return "Block #{} is mined.".format(blockchain.last_block.index)

# endpoint to query unconfirmed transactions
@app.route('/pending_tx', methods=['GET'])
def get_pending_tx():
    return json.dumps(blockchain.unconfirmed_transactions)








############################################################################







################# Network Access API endpoints #############################
#to register others
#only allows people to register that have a valid addresse
#check
@app.route('/register_node', methods=['POST'])
def register_new_peers():

    node_address = request.get_json()["node_address"]
    if not node_address:
        return "Invalid data", 400

    admin_address = request.get_json()["admin_address"]
    if not admin_address:
        return "Invalid data", 400

    admin_signature = request.get_json()["admin_signature"]
    if not admin_signature:
        return "Invalid data", 400

    admin_text = request.get_json()["text"]
    if not admin_text:
        return "Invalid data", 400

    Admins=get_admins()

    #Checks if User and Signature is correct -> public key verification
    for i in Admins:
        if i == admin_address:
            p_key = Admins[i]
            if validate_signature(p_key, admin_signature, admin_text) == False:
                return "Invalid User", 400
        return "Invalid User", 400

    # Add the node to the peer list
    peers.add(node_address)

    # Return the consensus blockchain to the newly registered node
    # so that he can sync
    return get_chain()


#to register himself
#check
@app.route('/register_with', methods=['POST'])
def register_with_existing_node():
    """
    Internally calls the `register_node` endpoint to
    register current node with the node specified in the
    request, and sync the blockchain as well as peer data.
    """
    node_address = request.get_json()["node_address"]
    if not node_address:
        return "Invalid data", 400

    admin_address = request.get_json()["admin_address"]
    if not admin_address:
        return "Invalid data", 400

    admin_signature = request.get_json()["admin_signature"]
    if not admin_signature:
        return "Invalid data", 400

    admin_text = request.get_json()["admin_text"]
    if not admin_text:
        return "Invalid data", 400

    data = {"node_address": request.host_url,
            "admin_address": admin_address,
            "admin_signature": admin_signature,
            "admin_text": admin_text}



    headers = {'Content-Type': "application/json"}

    # Make a request to register with remote node and obtain information
    response = requests.post(node_address + "/register_node",
                             data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        global blockchain
        global peers
        # update chain and the peers
        chain_dump = response.json()['chain']
        blockchain = create_chain_from_dump(chain_dump)
        peers.update(response.json()['peers'])
        return "Registration successful", 200
    else:
        # if something goes wrong, pass it on to the API response
        return response.content, response.status_code
############################################################################



############################################################################
# Uncomment this line if you want to specify the port number in the code
if __name__ == '__main__':
    app.run(debug=True, port=8000)
