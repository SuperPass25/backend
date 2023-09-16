# models.py

from pydantic import BaseModel

class UsernameCreate(BaseModel):
    username: str

class Password(BaseModel):
    website: str
    username: str
    password: str

class MasterPasswordCreate(BaseModel):
    master_password: str

class MasterPasswordEncrypt(BaseModel):
    master_password: str
