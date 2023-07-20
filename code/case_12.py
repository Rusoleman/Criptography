import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

nonce = b64decode('9Yccn/f5nJJhAt2S')#Issu could be here
key = bytes.fromhex('E2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB74')
text = bytes("He descubierto el error y no volveré a hacerlo mal", 'UTF-8')

try:
    cipher = AES.new(key, AES.MODE_GCM,nonce=nonce)
    ciphertext, tag = cipher.encrypt_and_digest(text)
    nonce_b64 = b64encode(cipher.nonce).decode('utf-8')
    ciphertext_b64 = b64encode(ciphertext).decode('utf-8')
    tag_b64 =b64encode(tag).decode('utf-8')
    mensaje_json = json.dumps({'nonce':nonce_b64, 'tag': tag_b64, 'texto cifrado':ciphertext_b64})
    print(mensaje_json)
    message_json=json.loads(mensaje_json)
    print("Resultado en B64:", message_json['texto cifrado'])
    print("Resultado en hexadecimal:", b64decode(message_json['texto cifrado']).hex())

except (ValueError, KeyError) as error:
    print('Problemas para descifrar....')
    print("El motivo del error es:", error)