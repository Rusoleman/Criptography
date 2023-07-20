from ssl import VerifyFlags
import jwt

public_key = open("public.pem").read()
private_key = open("private.pem").read()

encoded = jwt.encode({"idUsuario": 1, "movTarjeta": [{"id": 1,"comercio": "Comercio Juan", "importe": 5000}, {}],"id": 2,"comercio": "Rest Paquito", "importe": 6000,"Moneda": "EUR", "Saldo": 23400}, private_key, algorithm="RS256")
print(encoded)
print("================================")
decode = jwt.decode(encoded, public_key,algorithms="RS256", options={"verify_signature": True})
print(decode)
print("================================")