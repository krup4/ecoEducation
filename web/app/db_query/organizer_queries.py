
# SQL INJECTION ALERT 🚨🚨🚨🚨🚨🚨
from argon2 import PasswordHasher
import uuid
from psycopg2 import extras
import psycopg2
import os


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


def reg_org(uuid, data):
    events = data.get('owned_events')
    right_events = '[ '
    for el in events:
        right_events += f'"{el}", '
    right_events = right_events[:-2:]
    right_events += ' ]'
    return f"INSERT INTO organizers (uuid, login, password, name, proof, owned_events) VALUES ('{uuid}', '{data.get('login')}', '{ph.hash(data.get('password'))}', '{data.get('name')}', '{data.get('proof')}', '{right_events}')"


def logIn(loginS):
    cur = connection.cursor()
    cur.execute(f"SELECT * FROM organizers WHERE login = '{loginS}'")
    data = cur.fetchone()
    cur.close()
    return data


def login_check(loginS, password):
    data = logIn(loginS)
    # return data
    if (data is None):
        return False
    try:
        ph.verify(data[3], password)
        return True
    except:
        return False
