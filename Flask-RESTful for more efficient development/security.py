from hmac import compare_digest

from user import User

users = [
    User(1,'Jason','xyz'),
    User(2,'Ricardo','abc')
]

username_mapping = {
    u.username : u for u in users
}
# We have used the concept of creating a dictionary using set comprehension where key is username and value is related user object.

userid_mapping = {
    u.id : u for u in users
}

def authenticate(username,password):
    user = username_mapping.get(username,None)
    if user and compare_digest(user.password,password):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id,None)