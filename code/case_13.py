import os
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import ed25519

path = os.path.abspath(os.getcwd())

private_key  = RSA.import_key(open(path + "\clave-rsa-oaep-priv.pem").read())
public_key  = RSA.import_key(open(path + "\clave-rsa-oaep-publ.pem").read())

ec_private_key = os.path.join(path, "ed25519-priv")
ec_public_key = os.path.join(path, "ed25519-publ")

class Cipher():
    def __init__(self, private_key_path, public_key_path, ec_public_key_path, ec_private_key_path):
        self.public_key = public_key_path
        self.private_key = private_key_path
        with open(ec_private_key_path, 'rb') as file:
            pubk = file.read()
            self.ec_public_key = pubk 
        with open(ec_private_key_path, 'rb') as file:
            pk = file.read()
            self.ec_private_key = pk

    def sign_ed25519(self, msg):
        key = ed25519.SigningKey(self.ec_private_key)
        signature = key.sign(msg.encode('utf-8'))
        return signature.hex()
        
    def sign_pkcs1_v1_5(self, msg):
        mhash = SHA256.new(msg.encode('utf-8'))
        signature = pkcs1_15.new(self.private_key).sign(mhash)
        return signature


c = Cipher(private_key, public_key, ec_public_key, ec_private_key)
msg = "El equipo está preparado para seguir con el proceso, necesitaremos más recursos."
s1 = c.sign_pkcs1_v1_5(msg)
s2 = c.sign_ed25519(msg)
print("Firma PKCS#1v1.5: ",s1.hex())
print("Firma ED25519: ", s2)