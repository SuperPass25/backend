from fastapi import FastAPI
from pydantic import BaseModel
from generate_password import generate_secure_password  # Import the function
from models import UsernameCreate, MasterPasswordCreate, MasterPasswordEncrypt, Password

app = FastAPI()

db = []

@app.get("/")
async def hello_world():
    return "Hello world"


## Create the username

@app.post("/create-username/", response_model=UsernameCreate)
async def create_username(username_data: UsernameCreate):
    # Here, you can process and store the username as needed
    return username_data

# Create the master password
app.post("")

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
