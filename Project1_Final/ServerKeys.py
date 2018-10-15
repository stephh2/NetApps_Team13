from cryptography.fernet import Fernet


app_id = "R3JJ97-G824RGYY9T"


key = Fernet.generate_key()
f = Fernet(key)
encrypted_app_id = f.encrypt(app_id)