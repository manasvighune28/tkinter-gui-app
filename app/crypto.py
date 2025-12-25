from cryptography.fernet import Fernet
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
KEY_FILE = os.path.join(DATA_DIR, "secret.key")

def get_cipher():
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()

    return Fernet(key)

def encrypt(text):
    return get_cipher().encrypt(text.encode()).decode()

def decrypt(text):
    return get_cipher().decrypt(text.encode()).decode()
