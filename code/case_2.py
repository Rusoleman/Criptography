from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

iv_bytes = bytes.fromhex('00' * 16)
key = bytes.fromhex('A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72')

try:
    cipher = AES.new(key, AES.MODE_CBC, iv_bytes)
    b64_txt =  b64decode('TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI=')
    decrytpted_message_bytes = unpad(cipher.decrypt(b64_txt), AES.block_size, style="pkcs7")
    #msg_db = cipher.decrypt(b64_txt) #conocer cantidad de padding
    print("El texto en claro es:", decrytpted_message_bytes.hex())
except (ValueError, KeyError) as error:
    print('Problemas para descifrar....')
    print("El motivo del error es:", error)