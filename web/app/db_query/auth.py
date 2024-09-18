import os
import psycopg2
from psycopg2 import extras
import bcrypt
import uuid

salt = bcrypt.gensalt()

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
    cur.execute("SELECT * FROM users WHERE username=\"%s\"", (username))
    data = cur.fetchone()
    cur.close()
    return data


def register(username, password, rating):
    try:
        data = login(username)
        #check if user exists
        print(data)
        uuid = str(uuid.uuid4())
        cur = connection.cursor()
        cur.execute("INSERT INTO users (username, password, rating, uuid) VALUES (%s, %s, %s, %s)", (username, password, rating, uuid))
        cur.commit()
        cur.close()
    except:
        return BrokenPipeError
    






