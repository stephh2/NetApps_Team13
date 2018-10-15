from cryptography.fernet import Fernet

consumer_key="YWK6bomMzqSvfMIaty6iHNYtc"
consumer_secret="ZTTEjeudJpT5XPShH0U8E1Lp1H2fOpPyEV1GjE124GAhk1hEy0"

access_token="1041789280086106113-8c1PBH8ayeQy9s2MKstymI6QpwqAib"
access_token_secret="UHP7LgKv5Nn0enByeoI3zq13FPaBiveLfopYot96xPZIe"

key = Fernet.generate_key()
f = Fernet(key)

encrypted_consumer_key = f.encrypt(consumer_key)
encrypted_consumer_secret = f.encrypt(consumer_secret)
encrypted_access_token = f.encrypt(access_token)
encrypted_access_token_secret = f.encrypt(access_token_secret)