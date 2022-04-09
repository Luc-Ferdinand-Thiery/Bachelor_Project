import base58
from Crypto.PublicKey import RSA
import pandas
from files.Nodes.XX_utils import *
import ast





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


if __name__ == '__main__':
    test_load_wallet()
