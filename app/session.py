import json, os
from app.crypto import encrypt, decrypt

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SESSION_FILE = os.path.join(BASE_DIR, "data", "session.json")

def save_session(email, password):
    with open(SESSION_FILE, "w") as f:
        json.dump({
            "email": email,
            "password": encrypt(password)
        }, f)

def load_session():
    if not os.path.exists(SESSION_FILE):
        return None, None

    with open(SESSION_FILE) as f:
        data = json.load(f)

    return data["email"], decrypt(data["password"])
