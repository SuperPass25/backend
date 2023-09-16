from fastapi import FastAPI
from pydantic import BaseModel
from generate_password import generate_secure_password  # Import the function

app = FastAPI()

class Password(BaseModel):
    website: str
    username: str
    password: str

db = []

@app.get("/")
async def hello_world():
    return "Hello world"

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
    
# This is not actually taking a length from parameters. This is probably a form that needs to be filled out by
# the user and then sent here 
@app.post("/generate-password/{length}", response_model=dict)
async def generate_password(length: int):
    password = generate_secure_password(length)
    return {"password": password}
