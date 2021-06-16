from sqlalchemy.orm import Session

from ..config.database import get_db

from ..models.user_model import User
from ..schemas import user_schema

db: Session = get_db()

def get_user_by_id(id: int):
    return db.query(User).filter(User.id == id).first()

def get_user_by_email(email: str):
    return db.query(User).filter(User.email == email).first()

def get_all_users(skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(user: user_schema.UserCreate):
    user = User(**user.dict())

    db.add(user)
    db.commit(); db.refresh(user)
    return user

def delete_user(user: user_schema.UserDelete):
    user = db.query(User).filter(User.email == user.email and User.password == user.password).first()

    db.delete(user)
    db.commit()
    return user