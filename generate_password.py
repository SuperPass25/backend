# password_generator.py

import secrets

def generate_secure_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+[]{}|;:\<>?/"
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

