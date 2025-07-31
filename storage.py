import json
import os
from encryption import encrypt_password, decrypt_password

DATA_FILE = "data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def save_password(service, username, password):
    data = load_data()
    data[service] = {
        "username": username,
        "password": encrypt_password(password) }
    save_data(data)

def get_password(service):
    data = load_data()
    if service in data:
        entry = data[service]
        entry["password"] = decrypt_password(entry["password"])
        return entry

def delete_password(service):
    data = load_data()
    if service in data:
        del data[service]
        save_data(data)
        return True
    return False