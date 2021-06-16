from sqlalchemy import Column, Integer, String

from .base_model import Base, BaseMixin

class User(Base, BaseMixin):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    email = Column(String(51), unique=True, index=True, nullable=False)
    password = Column(String(65), nullable=False)
    username = Column(String(11), nullable=False)
    authority = Column(String, nullable=False)

    nickname = Column(String(21), nullable=True)