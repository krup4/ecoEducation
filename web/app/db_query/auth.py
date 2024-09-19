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
    cur.execute(f"SELECT * FROM users WHERE username = '{username}'")
    data = cur.fetchone()
    cur.close()
    return data


def auth_check(username, password):
    data = login(username)
    if (data is None):
        return False
    try:
        ph.verify(data[2], password)
        return True
    except:
        return False


def register(username, password, full_name, rating):
    data = login(username)
    # check if user exists
    if (data != None):
        return
    cur = connection.cursor()
    # return (username, str(h), full_name, rating, crazy)
    cur.execute(f"INSERT INTO users (username, password, full_name, rating, uuid) VALUES ('{username}', '{ph.hash(password)}', '{full_name}', '{rating}', '{uuid.uuid4()}')", #sql injection alert
    )
    connection.commit()
    cur.close()

