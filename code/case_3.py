from Crypto.Cipher import ChaCha20_Poly1305
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes
from Crypto.Hash import HMAC, SHA256
import json
import secrets


def chacha20_cipher(text):
    txt_bytes = bytes(text, 'UTF-8')
    cipher_key = bytes.fromhex('AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120')
    unonce = b64decode('9Yccn/f5nJJhAt2S')#The nonce should be unique ever thi is an example
    #unonce = get_random_bytes(12) #Unique nonce 12 bytes
    cipher = ChaCha20_Poly1305.new(key=cipher_key, nonce=unonce)
    ciphertext, tag = cipher.encrypt_and_digest(txt_bytes)
    
    # IMPROVEMENT: HMAC w/ SHA256 to add authentication to our messages
    hmac_key = SHA256.new(cipher_key).digest()
    hmac = HMAC.new(hmac_key, digestmod=SHA256)
    hmac.update(ciphertext)
    hmac_value = hmac.digest()

    json_res = json.dumps({
        "nonce": b64encode(unonce).decode(),
        "cipher_txt": b64encode(ciphertext).decode(),
        "tag":b64encode(tag).decode(),
        "hmac": b64encode(hmac_value).decode()
    })
    return json_res

def cipher_verification(json_data, cipher_key):
    data = json.loads(json_data)
    unonce = b64decode(data['nonce'])
    ciphertext = b64decode(data['cipher_txt'])
    tag = b64decode(data['tag'])
    hmac_value = b64decode(data['hmac'])

    #Calculate HMAC
    hmac_key = SHA256.new(cipher_key).digest()
    hmac = HMAC.new(hmac_key, digestmod=SHA256)
    hmac.update(ciphertext)
    calculated_hmac = hmac.digest()
    #Verify HMAC
    if not secrets.compare_digest(calculated_hmac, hmac_value):
        raise ValueError("HMAC verification failed.The message may have been tampered with.")

    cipher = ChaCha20_Poly1305.new(key=cipher_key, nonce=unonce)
    decrypted_txt = cipher.decrypt_and_verify(ciphertext, tag)
    return decrypted_txt.decode('UTF-8')
    

ck = bytes.fromhex('AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120')
encrypted_data = chacha20_cipher("KeepCoding te enseña a codificar y a cifrar")
print("Message Signed and Ecrypted:", encrypted_data)

try:
    decrypted_text = cipher_verification(encrypted_data, ck)
    print("Message decrypted and verified:", decrypted_text)
except ValueError as e:
    print("Error:", str(e))