from fastapi import FastAPI
from pydantic import BaseModel
from generate_password import generate_secure_password  # Import the function
from models import UsernameCreate, MasterPasswordCreate, MasterPasswordEncrypt, Password
from encryption import generate_fernet_key, encrypt

app = FastAPI()

db = []

@app.get("/")
async def hello_world():
    return "Hello world"

# Generate a Fernet key
key = generate_fernet_key()

## Create the username

@app.post("/create-username/", response_model=UsernameCreate)
async def create_username(username_data: UsernameCreate):
    # Here, you can process and store the username as needed
    return username_data

# Create the master password
@app.post("/create-master-password/", response_model=dict)
async def create_master_password(password_data: MasterPasswordCreate):
    # Store the master password securely or associate it with the user account
    master_password = password_data.master_password

    # Return a response indicating success (you may want to add more logic)
    return {"message": "Master password created successfully"}

@app.post("/encrypt-master-password/", response_model=dict)
async def encrypt_master_password(password_data: MasterPasswordEncrypt):
    # Encrypt the master password using the generated Fernet key
    encrypted_password = encrypt(password_data.master_password, key)

    # Return the encrypted password (you may want to store it securely)
    return {"encrypted_password": encrypted_password}

# THE CRUD part for the other passwords

@app.post("/passwords/create", response_model=Password)
async def create_password(password: Password):
    db.append(password)
    return password

@app.get("/passwords/", response_model=list[Password])
async def read_passwords():
    return db

@app.put("/passwords/{password_id}", response_model=Password)
async def update_password(password_id: int, updated_password: Password):
    if 0 <= password_id < len(db):
        db[password_id] = updated_password
        return updated_password

@app.delete("/passwords/{password_id}", response_model=Password)
async def delete_password(password_id: int):
    if 0 <= password_id < len(db):
        deleted_password = db.pop(password_id)
        return deleted_password

@app.post("/generate-password/{length}", response_model=dict)
async def generate_password(length: int):
    password = generate_secure_password(length)
    return {"password": password}
