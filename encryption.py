# encryption.py

from cryptography.fernet import Fernet

# Generate a Fernet key
def generate_fernet_key():
    return Fernet.generate_key()

# Encrypt data using Fernet
def encrypt(data, key):
    f = Fernet(key)
    return f.encrypt(data.encode()).decode()

# Decrypt data using Fernet
def decrypt(data, key):
    f = Fernet(key)
    return f.decrypt(data.encode()).decode()
