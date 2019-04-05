import pickle
import os

def add_user(name,token):

    if os.path.exists("data/userlists"):
        userlists = "data/userlists"
    else:
        userlists = set()

    if name in userlists:

        return 0
    else:
        add_token()
        userlists.append(name)
        pickle.dump(userlists,"data/userlists")

        return 1

def encode(token):
    import cipher

    encryptText = cipher.encrypt(token)

    return encryptText

def add_token(name,token):
    if os.path.exists("data/tokenlists"):
        tokenlists = "data/tokenlists"
    else:
        tokenlists = {}

    token_code = encode(token)
    tokenlists.update(name,token_code)
    pickle.dump(tokenlists,"data/tokenlists")
