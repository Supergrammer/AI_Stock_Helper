from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel

class UserRequest(BaseModel):
    pass

class UserResponse(BaseModel):
    pass

class UserAuth(BaseModel):
    email: str
    password: str

class UserPassword(BaseModel):
    id: UUID
    password_history: list[str]

    class Config:
        orm_mode = True

class User(BaseModel):
    id: UUID
    email: str
    password: UserPassword
    username: str
    nickname: Optional[str] = None
    authority: Optional[list[str]] = []

    created_date: datetime
    updated_date: datetime

    class Config:
        orm_mode = True

class UserCreate(UserRequest):
    email: str
    password: str
    username: str
    nickname: Optional[str] = None
    authority: Optional[list[str]] = []

class UserDelete(UserRequest, UserAuth):
    pass

class UserRead(UserResponse):
    id: UUID
    email: str
    username: str
    nickname: Optional[str] = None
    authority: Optional[list[str]] = []

    created_date: datetime
    updated_date: datetime

    class Config:
        orm_mode = True