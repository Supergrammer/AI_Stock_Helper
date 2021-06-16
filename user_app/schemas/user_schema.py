from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class UserRequest(BaseModel):
    pass

class UserResponse(BaseModel):
    pass

class UserAuth(BaseModel):
    email: str
    password: str

class User(BaseModel):
    id: int
    email: str
    password: str
    username: str
    nickname: Optional[str] = None
    created_date: Optional[datetime] = None
    updated_date: Optional[datetime] = None

class UserCreate(UserRequest):
    email: str
    password: str
    username: str
    nickname: Optional[str] = None

class UserDelete(UserRequest, UserAuth):
    pass

class UserGet(UserResponse):
    id: int
    email: str
    username: str
    nickname: Optional[str] = None
    created_date: Optional[datetime] = None
    updated_date: Optional[datetime] = None

    class Config:
        orm_mode = True