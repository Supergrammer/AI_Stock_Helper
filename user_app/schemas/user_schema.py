from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel

from .password_schema import Password

class UserRequest(BaseModel):
    pass

class UserResponse(BaseModel):
    pass

class UserInput(BaseModel):
    pass

class UserCreateOrUpdate(UserRequest):
    email: str
    password: Optional[str] = None
    username: str
    nickname: Optional[str] = None
    authority: Optional[list[str]] = []

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