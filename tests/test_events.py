import requests
import datetime

BASE_URL = 'https://api.greeneduinitiative.ru/event'


def add():
    event = {
        "time": datetime.datetime.now().isoformat(),
        "adress": "pupupu",
        "name": 'lorem ipsum set',
        "cost": 52,
        "tags": ["ewrw", "wrwer", "ewrwer"],
        "description": 'adhjvbhdbavldaf'
    }

    response = requests.post(f"{BASE_URL}/add", json=event)
    print(response.json())
    return response.json()

def delete(uuid):
    event = {
        "uuid": uuid
    }

    response = requests.post(f"{BASE_URL}/delete", json=event)
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


# edit("b990284c-bc23-44c3-8cfc-a2b7204bd7e5")
#delete("b990284c-bc23-44c3-8cfc-a2b7204bd7e5")
add()
