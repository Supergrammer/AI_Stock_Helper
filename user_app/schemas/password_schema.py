from uuid import UUID
from pydantic import BaseModel

class Password(BaseModel):
    id: UUID
    password_history: list[str]

    class Config:
        orm_mode = True