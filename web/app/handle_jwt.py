import jwt

SECRET = "PASTEYOURSECRETHERE" #insecure value

def encode_jwt(username):
    return jwt.encode({"username":username}, SECRET, algorithm="HS256")

def decode_jwt(JWT):
    return jwt.decode(JWT, SECRET, algorithms=["HS256"])