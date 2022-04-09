import pandas
# encrypting
from cryptography.fernet import Fernet
import cryptography

import base58
from Crypto.PublicKey import RSA
from files.Nodes.XX_utils import *
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15


df = pandas.read_csv('Admins.csv')
df=df.drop(columns=['Private_key'])
df = df.to_json()

df = json.loads(df)

new_dict={}
n_dict={}

l1=[new_dict,n_dict]

data={"test":1}

user={"add":b'3eqLZijdad7VCLHPXfsViZJGpKFGupeQrjzz7DDD4SxTDXaS7F4g4Dv',
      "priv":b'-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAp1MBSjL0jvMLhBU/Bj3CxSoKZcVXRBgvJ+2SNqZpR1IKfG4c\ntso5lFWC+GfhEZq3saZX4cBWcvhWyJX3a/vvw3p+AUfPX3WASr3SW9QngNwIQyea\nKbj3PXX2ooUEmKZ5j+tQibZ+LQYoxhiwrRcP2W1X4XdPg5Chws8eM0IWCspIAnN7\n1SK9RPakeo5qxHDojMyQDITHaaom3VadmbQZ9mZSTUr74HkOyj8mjvFk9dmgRe45\nnXICsB4TCgfj4AVQqhJAWKADH8y6sp6e3weXhxgC7UrxwUienBuiNDX5Q2mD9roS\nwPBtH4Xj3Q23JRMIb3uRMOnUUeEsokwa/3pdzQIDAQABAoIBAA2SV+HwhR6Z8kt5\n1hbuNOYwgg+XWvv5qP8bljon83uAWSJjltRxGnKzuhmAHEs4JrTAy1/S7am9bXvI\n+JZOvoSD/HfWuI7Dfvu3YgcZvt4eurrVTPwb9edxy7OKurQCmL/GjedFoP4k6D/w\nUIneYeY4WyIjpWFRMcjiOAH48JHAwCzoj+jLdkisCibemHqdxGAsKuh+Lf6QaA8W\nNTmG5e/S5YSF88rLLzWIHxcABzchx7G/scPwFt4DEIgPqagTsuCETqR2blTTF+2l\njVFqHEYWv6eVlovr7ZEuCAkale/RgePCMsXup/vc1aL+yuC9QLudgpyk5FbIwG1n\n60pqoT8CgYEAu971BQpuF6xFd4bXSe+30Apo+FZihBhEGXuh1+M/EeN/gPy9DAwP\ntTG/3gmHO1NyJ5R9cQBA1u1nVQICy41fSyiGpM6vAHBURuFyUAvo9o5Nbck/j8B8\ndTNoXABtmW//10lIN/E+Be+pAMI0l6HlzqvEk3dtogOArEJ5ACLmINcCgYEA5ACX\nWNf6zmZululYKSXA5xnS2drxSR+1OZUgmatf5qjvbmsyk/pt9qgW9bDpRzX9BN+l\nIwlHK3n1Shdw1gKv5XhC0R4PrbcmlYCloKTdvBwOqIrlZLHbKzDEqyldZq2+ziFs\nIIerJQtPIWb3mrd081VLExmNkEQV9cYrne9UzfsCgYEAjhOMxKUgoPJ9DmmBAr8x\nCTn2LGhX1IHtbkAbIwMOPV8Im+mGpkew0VywNyCJjooKuHgJbZ29a0zaamU86+cb\n++DIAnbzzacldP0lz/dR1LPFRpN9aB8vgArCj2EbgYA7wPoAjZ35Q8/8xUAZOdsL\nygIIhWU6Gd4AP0V98GZ0Fr0CgYAD6Q6vc2TVzWPwKqhcbE1WqVa4bczdmDGffzND\n73CBoDwbBLOlXhIsvM1IAXS+x+pC/yLx6uLRmBHg524D/Z/Oq7VZqM5UCGQdBEvS\n6YD0DPcjZN5yT6qWnwuAdAEqFajEGEameC0zQXJl/EIa4TKcScYz2ahX5RMLWA6/\ncq9dqQKBgAUTSOjWalhQqXtnEdL74aMbYy5G9CHNv0M9F+BOunOsMPKbe2Ji0iVe\nkge11c199OYRCZF16WGL3PVOg0syzqStygDgZyhNORutzFHlqlK9iU7AbXq+g1et\nHtWAQLGVZ/uzc+37aOIcds6fwb5chnic5Go8dnTuPYRu6X5kuuTq\n-----END RSA PRIVATE KEY-----',
      "pub":b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAp1MBSjL0jvMLhBU/Bj3C\nxSoKZcVXRBgvJ+2SNqZpR1IKfG4ctso5lFWC+GfhEZq3saZX4cBWcvhWyJX3a/vv\nw3p+AUfPX3WASr3SW9QngNwIQyeaKbj3PXX2ooUEmKZ5j+tQibZ+LQYoxhiwrRcP\n2W1X4XdPg5Chws8eM0IWCspIAnN71SK9RPakeo5qxHDojMyQDITHaaom3VadmbQZ\n9mZSTUr74HkOyj8mjvFk9dmgRe45nXICsB4TCgfj4AVQqhJAWKADH8y6sp6e3weX\nhxgC7UrxwUienBuiNDX5Q2mD9roSwPBtH4Xj3Q23JRMIb3uRMOnUUeEsokwa/3pd\nzQIDAQAB\n-----END PUBLIC KEY-----'
}

def vvv():
    print(type(user["priv"]))

def initialize_wallet():
    private_key = RSA.generate(2048)
    public_key = private_key.publickey().export_key()
    private_key = private_key.export_key()
    hash_1 = calculate_hash(public_key, hash_function="sha256")
    hash_2 = calculate_hash(hash_1, hash_function="ripemd160")
    address = base58.b58encode(hash_2)
    return {"private_key":private_key,
            "public_key":public_key,
            "address":address}

def validate_signature(public_key: bytes, signature: bytes, transaction_data):
    transaction_data = json.dumps(transaction_data, indent=2).encode('utf-8')
    public_key_object = RSA.import_key(public_key)
    transaction_hash = SHA256.new(transaction_data)
    try:
        pkcs1_15.new(public_key_object).verify(transaction_hash, signature)
        return True
    except (ValueError, TypeError):
        #error signature not correct
        return False

#creates a signature
#check
def create_signature(Data, Private_Key):
    Private_Key=RSA.import_key(Private_Key)
    bytes=json.dumps(Data, indent=2).encode('utf-8')
    hash_object = SHA256.new(bytes)
    signature = pkcs1_15.new(Private_Key).sign(hash_object)

    return signature


def admins():
    df = pandas.read_csv('Admins.csv')
    df = df.drop(columns=['Private_key'])

    data={}
    for i in df.index:
        data[df.iloc[i][0]]=df.iloc[i][1]
        print(df.iloc[i][0],":",data[df.iloc[i][0]])
    Genesis_Admins = json.dumps(data)
    print(Genesis_Admins)
    #print(Genesis_Admins)

def Fernet_encryption_decryption():
    message = "my deep dark secret".encode()
    key=Fernet.generate_key()

    f = Fernet(key)
    encrypted = f.encrypt(message)
    print("encrypted",encrypted)

    key = Fernet.generate_key()

    f = Fernet(key)

    try:

        decrypted = f.decrypt(encrypted)
        print(decrypted)
        print("yolo")

    except (cryptography.fernet.InvalidToken, TypeError):
        print("error")

def dict_tester1():
    x={}

    new_dict["1"]=1
    new_dict["2"] = 1
    new_dict["3"] = 1

    n_dict["1"]=1
    n_dict["2"] = 0
    n_dict["3"] = 1

    for dictt in l1:
        for i in dictt:
            x[i]=dictt[i]

    print(x)

def listts():
    list1=["1","2"]
    list2=["3","4"]

    list1.append(list2)

    print(list1)


def tester():
    for i in df["Address"]:
        print(type(df["Address"][i]))

def ccc():
    W1 = initialize_wallet()
    print(W1["private_key"])
    print(type(W1["private_key"]))
    signature = create_signature(data, W1["private_key"])
    print(signature)
    check = validate_signature(W1["public_key"], signature, data)
    print(check)

def importting():
    df = pandas.read_csv('Admins.csv')
    data = {}
    for i in df.index:
        data[df.iloc[i][0]] = df.iloc[i][2]
        # print(df.iloc[i][0],":",data[df.iloc[i][0]])
    Genesis_Admins = json.dumps(data)
    ##############################################
    print(type(df.iloc[0][2]))

    # my Wallet
    x=bytes(df.iloc[0][1], 'utf-8')
    print(x)
    print(type(x))

    X_Address = df.iloc[0][0]
    X_Private_Key = RSA.import_key(x)
    X_Public_Key = df.iloc[0][2]


    print(X_Private_Key)
    print(X_Public_Key)
    print(X_Address)

if __name__ == '__main__':
    importting()
