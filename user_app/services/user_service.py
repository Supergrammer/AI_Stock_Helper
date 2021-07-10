from uuid import UUID

from sqlalchemy.orm import Session

from ..config.database import get_db

from ..modules import oauth_module
from ..models.user_model import User
from ..models.password_model import Password
from ..schemas import user_schema

def create_user(user: user_schema.UserCreateOrUpdate, db: Session = get_db()):
    user = User(
        email=user.email,
        password=Password(
            password_history=[oauth_module.get_hashed_password(user.password)]),
        username=user.username,
        nickname=user.nickname,
        authority=user.authority)

    db.add(user)
    db.commit(); db.refresh(user)
    return user

def get_user_by_id(id: UUID, db: Session = get_db()):
    return db.query(User).filter(User.id == id).first()

def get_user_by_email(email: str, db: Session = get_db()):
    return db.query(User).filter(User.email == email).first()

def get_all_users(skip: int = 0, limit: int = 100, db: Session = get_db()):
    return db.query(User).offset(skip).limit(limit).all()

def update_user(user: user_schema.UserCreateOrUpdate, db: Session = get_db()):
    user = User(
        email=user.email,
        password = db.query(Password).filter(Password.id == User.id),
        username=user.username,
        nickname=user.nickname,
        authority=user.authority)

    db.query(User).filter(User.email == user.email).update(user)
    db.commit()
    return user

def delete_user(email: str, db: Session = get_db()):
    user = db.query(User).filter(User.email == email).first()
    
    db.delete(user)
    db.commit()
    return user