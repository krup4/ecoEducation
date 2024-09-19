import requests
import datetime

BASE_URL = 'http://172.22.0.4:8080/org'

# id SERIAL PRIMARY KEY,
#     uuid UUID,
#     login TEXT,
#     password TEXT,
#     name TEXT,
#     proof TEXT,
#     owned_events JSON

def reg():
    org = {
        "login": "uvbndvn",
        "password": "dsvsdv",
        "name": "sdoufvbd",
        "proof": "dvdfvd",
        "owned_events": ["soidfvns", "dsufvbdsv", "jsdbvsv"]
    }

    response = requests.post(f"{BASE_URL}/register", json=org)
    print(response.json())


def log():
    org = {
        "login": "uvbndv",
        "password": "dsvdv"
    }

    response = requests.post(f"{BASE_URL}/login", json=org)
    print(response.json())


def edit(uuid):
    event = {
        "uuid": uuid,
        "cost": 57,
        "tags": ["ewrw", "wrwer"],
        "description": 'hui'
    }
    response = requests.post(f"{BASE_URL}/edit", json=event)
    print(response.json())

# reg()
log()
