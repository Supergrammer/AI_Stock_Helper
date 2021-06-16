from typing import List, Optional
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
    scopes: List[str] = []

class UserAuth(BaseModel):
    email: str
    password: str

class UserDelete(UserAuth):
    pass