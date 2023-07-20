import hashlib
s = hashlib.sha3_256()
s2 = hashlib.sha512()
s.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía.","utf-8"))
s2.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía","utf-8"))
print("SHA3-256: ",s.hexdigest())
print("SHA2-256: ",s2.hexdigest())
