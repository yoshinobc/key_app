import pickle
import os

def check_user(name,token):
    if os.path.exists("data/userlists") and os.path.exists("data/tokenlists"):
        userlists = "data/userlists"
        tokenlists = "data/tokenlists"
    else:
        return 0

    if (name,token) in tokenlists.item():
        return 1
        
    else :
        return 0
