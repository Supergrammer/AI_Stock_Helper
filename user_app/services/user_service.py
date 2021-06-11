from ..schemas.user_schema import User_request, User_response
from sqlalchemy import schema
from sqlalchemy.orm import Session

from ..config.database import get_db

from ..models.user_model import User
from ..schemas.user_schema import *

def get_user(id: int, db: Session = get_db()):
    return db.query(User).filter(User.id == id).first()

def get_user_by_email(email: str, db: Session = get_db()):
    return db.query(User).filter(User.email == email).first()

def get_all_user(skip: int = 0, limit: int = 100, db: Session = get_db()):
    return db.query(User).offset(skip).limit(limit).all()

# def create_user(user: User_request, db: Session = get_db()):
#     # db_user = User_request(email=user.email, password=user.password, username=user.username)
#     db_user = User(**user.dict())

#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

def create_user(user: User_request, db: Session = get_db()):
    db_user = User(
        email=user.email,
        password=user.password,
        username=user.username
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user