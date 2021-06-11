from typing import List, Optional

from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User_request(BaseModel):
    email: str
    password: str
    username: str

class User_response(BaseModel):
    id: int
    email: str
    password: str
    username: str

    class Config:
        orm_mode = True