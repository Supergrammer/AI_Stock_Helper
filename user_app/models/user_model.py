from sqlalchemy import Column, Integer, String

from .base_model import Base, BaseMixin

class User(Base, BaseMixin):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(51), unique=True, index=True)
    password = Column(String(21))
    username = Column(String(11))