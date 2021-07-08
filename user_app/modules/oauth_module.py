from datetime import datetime, timedelta

from fastapi import HTTPException, status, Depends

from fastapi.security.oauth2 import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt

from sqlalchemy.orm import Session

from ..models.user_model import User
from ..schemas import user_schema, token_schema

from ..config.config import get_configurations
from ..config.database import get_db

c = get_configurations()
SECRET_KEY = c.secret_key
HASH_ALGORITHM = c.hash_algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = c.access_token_expire_minutes

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def get_hashed_password(plain):
    return pwd_context.hash(plain)

def is_authenticated_user(form_data: OAuth2PasswordRequestForm, db: Session = get_db()):
    user = db.query(User).filter(User.email == form_data.username).first()

    if not user or \
        not verify_password(form_data.password, user.password.password_history[-1]):
        return False
    return user    

def create_access_token(data: dict, expire_minutes: int = ACCESS_TOKEN_EXPIRE_MINUTES):
    to_encode = data.copy()
    to_encode.update(
        {"exp": datetime.utcnow() + timedelta(minutes=expire_minutes)})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=HASH_ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = get_db()):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[HASH_ALGORITHM])
        email: str = payload.get("email")

        if not email:
            raise credentials_exception
        token_data = token_schema.TokenData(email=email)
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise credentials_exception

    return user

async def get_current_active_user(current_user: user_schema.User = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    return current_user