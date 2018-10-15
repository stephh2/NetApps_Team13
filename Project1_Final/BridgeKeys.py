#IBM INFO
IBM_url="https://stream.watsonplatform.net/text-to-speech/api"
IBM_username="e431d0ee-b55f-4ed1-bd3b-72e0874b870f"
IBM_password="MDNfVMstpi7I"

from cryptography.fernet import Fernet

k= Fernet.generate_key()
f = Fernet(k)
encrypted_IBM_url = f.encrypt(IBM_url)
encrypted_IBM_username = f.encrypt(IBM_username)
encrypted_IBM_password = f.encrypt(IBM_password)
