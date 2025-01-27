from user import User 
from hmac import compare_digest

def authenticate(username,password):
    user = User.Find_by_username(username)
    if user and compare_digest(user.password,password):
        return user

def identity(payload):
    user_id = payload['identity']
    return User.Find_by_id(user_id)