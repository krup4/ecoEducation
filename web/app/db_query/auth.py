import os
import psycopg2
from psycopg2 import extras
import uuid
from argon2 import PasswordHasher

ph = PasswordHasher()

user = os.environ['POSTGRES_USERNAME']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
port = os.environ['POSTGRES_PORT']
database = os.environ['POSTGRES_DATABASE']
connection = psycopg2.connect(user=user,
                              password=password,
                              host=host,
                              port=port,
                              database=database)

 

def login(username):
    cur = connection.cursor()    
    cur.execute("SELECT * FROM users WHERE username=(%s)", (username,))
    data = cur.fetchone()
    cur.close()
    return data

def auth_check(username, password):
    data = login(username)
    if (data == None):
        return False
    if ph.verify(password ,data[2]):
        return True
    else:
        return False

def register(username, password, full_name, rating):
    try:
        data = login(username)
        #check if user exists
        print(data)
        crazy = str(uuid.uuid4())
        cur = connection.cursor()
        hash = ph(password)
        cur.execute("INSERT INTO users (username, password, full_name, rating, uuid) VALUES (%s, %s, %s, %s, %s)", (username, str(hash), full_name, rating, crazy))
        cur.commit()
        cur.close()
    except:
        return BrokenPipeError
    






