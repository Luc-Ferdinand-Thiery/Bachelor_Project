import base58
from Crypto.PublicKey import RSA
import pandas
import ast
import csv
from Crypto.Signature import pkcs1_15

from Crypto.Hash import RIPEMD160, SHA256
import json

def calculate_hash(data, hash_function: str = "sha256"):
    if type(data) == str:
        data = bytearray(data, "utf-8")
    if hash_function == "sha256":
        h = SHA256.new()
        h.update(data)
        return h.hexdigest()
    if hash_function == "ripemd160":
        h = RIPEMD160.new()
        h.update(data)
        return h.hexdigest()


def generate_transaction_data(sender_bitcoin_address, receiver_bitcoin_address, amount: int) -> dict:
    return {
        "sender": sender_bitcoin_address,
        "receiver": receiver_bitcoin_address,
        "amount": amount
    }


def convert_transaction_data_to_bytes(transaction_data: dict):
    new_transaction_data = transaction_data.copy()
    new_transaction_data["sender"] = str(transaction_data["sender"])
    new_transaction_data["receiver"] = str(transaction_data["receiver"])
    new_transaction_data["amount"] = str(transaction_data["amount"])
    return json.dumps(new_transaction_data, indent=2).encode('utf-8')

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

def create_signature(Data, Private_Key):
    bytes=json.dumps(Data, indent=2).encode('utf-8')
    hash_object = SHA256.new(bytes)
    signature = pkcs1_15.new(Private_Key).sign(hash_object)

    return signature

#creates
class wallet:
    def __init__(self):
        self.address = None
        self.private_key = None
        self.public_key = None

    #creates a completley new wallet
    def create(self):
        private_key = RSA.generate(2048) #creates private key
        self.public_key = private_key.publickey().export_key()
        self.private_key = private_key.export_key()
        hash_1 = calculate_hash(self.public_key, hash_function="sha256")
        hash_2 = calculate_hash(hash_1, hash_function="ripemd160")
        self.address = base58.b58encode(hash_2)


    #loads an already created wallet
    def load(self, add, priv, pub):
        #checks if data is bytes
        if isinstance(add, (bytes, bytearray)) and isinstance(priv, (bytes, bytearray)) and isinstance(pub, (bytes, bytearray)):
            self.address= add
            self.private_key = RSA.import_key(priv)
            self.public_key = pub
        else:
            #if not -> try to convert it
            try:
                #converts stringbyte to byte
                self.address = ast.literal_eval(add)
                self.private_key = RSA.import_key(ast.literal_eval(priv))
                self.public_key = ast.literal_eval(pub)

            except (ValueError):
                print("error")

def test_create_wallet():

    new_wallet = wallet()
    new_wallet.create()
    print(type(new_wallet.address), new_wallet.address)
    print(type(new_wallet.private_key), new_wallet.private_key)
    print(type(new_wallet.public_key), new_wallet.public_key)

def test_load_wallet():
    df = pandas.read_csv('Admins.csv') #already created wallets
    new_wallet = wallet()
    new_wallet.load(df.iloc[0][0],
                    df.iloc[0][1],
                    df.iloc[0][2])
    print(type(new_wallet.address), new_wallet.address)
    print(type(new_wallet.private_key), new_wallet.private_key)
    print(type(new_wallet.public_key), new_wallet.public_key)

def test_signature():
    data={
        "a":"test1",
        "b":"test2"
    }



    df = pandas.read_csv('Admins.csv')  # already created wallets
    W1 = wallet()
    W1.load(df.iloc[0][0],
                    df.iloc[0][1],
                    df.iloc[0][2])

    sig=create_signature(data,W1.private_key)
    print(type(sig))
    print(str(sig))
    check=validate_signature(W1.public_key, sig, data)
    print(check)


def create_Admins_csv():
    addresses=[]
    for i in range (0,10):
        new_wallet=wallet
        new_wallet.load()
        addresses.append(new_wallet)
    with open('Admins.csv', 'w') as f:
        write = csv.writer(f)

        fields=["Address", "Private_key", "Public_key"]
        write.writerow(fields)
        for i in addresses:
            # using csv.writer method from CSV package
            write.writerow([i.address, i.private_key, i.public_key])

if __name__ == '__main__':
    test_signature()
