import base58
from Crypto.PublicKey import RSA
import binascii
import csv
from files.Nodes.XX_utils import *
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15

class Owner:
    def __init__(self, private_key: RSA.RsaKey, public_key: bytes, address: bytes):
        self.private_key = private_key
        self.public_key = public_key
        self.address = address

        print(public_key)
        print(address)



    def create_admin_signature(self, pw):
        data={
            "address":str(self.address),
            "password":str(pw)
        }

        self.bytes=json.dumps(data, indent=2).encode('utf-8')
        hash_object = SHA256.new(self.bytes)
        self.signature = pkcs1_15.new(self.private_key).sign(hash_object)


        print(self.signature)
        return self.signature

    def validate_signature(self, public_key: bytes, signature: bytes, transaction_data: bytes):
        public_key_object = RSA.import_key(public_key)
        transaction_hash = SHA256.new(transaction_data)
        pkcs1_15.new(public_key_object).verify(transaction_hash, signature)

        try:
            pkcs1_15.new(public_key_object).verify(transaction_hash, signature)
            return True
        except (ValueError, TypeError):
            #error signature not correct
            return False


def initialize_wallet():
    private_key = RSA.generate(2048)
    public_key = private_key.publickey().export_key()
    private_key = private_key.export_key()
    hash_1 = calculate_hash(public_key, hash_function="sha256")
    hash_2 = calculate_hash(hash_1, hash_function="ripemd160")
    address = base58.b58encode(hash_2)
    return Owner(private_key, public_key, address)




class Transaction:
    def __init__(self, owner: Owner, receiver_address: bytes, amount: int, signature: str = ""):
        self.owner = owner
        self.receiver_address = receiver_address
        self.amount = amount
        self.signature = signature

    def generate_data(self) -> bytes:
        transaction_data = generate_transaction_data(self.owner.address, self.receiver_address, self.amount)
        return convert_transaction_data_to_bytes(transaction_data)

    def sign(self):
        transaction_data = self.generate_data()
        hash_object = SHA256.new(transaction_data)
        signature = pkcs1_15.new(self.owner.private_key).sign(hash_object)
        self.signature = binascii.hexlify(signature).decode("utf-8")

    def send_to_nodes(self):
        return {
            "sender_address": self.owner.address,
            "receiver_address": self.receiver_address,
            "amount": self.amount,
            "signature": self.signature
        }



#creating 10 admins
if __name__ == '__main__':


     #creating 10 wallets and storing them in csv
    x=[]
    for i in range (0,10):
        new_wallet=initialize_wallet()
        x.append(new_wallet)
    with open('Admins.csv', 'w') as f:
        write = csv.writer(f)

        fields=["Address", "Private_key", "Public_key"]
        write.writerow(fields)
        for i in x:
            # using csv.writer method from CSV package
            write.writerow([i.address, i.private_key, i.public_key])


