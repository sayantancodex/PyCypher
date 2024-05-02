import secrets
def tokengenerator():
    token = secrets.token_hex()
    return token

