from datetime import datetime, timedelta

from fastapi import HTTPException, status, Depends, Security

from fastapi.security.oauth2 import OAuth2PasswordBearer, OAuth2PasswordRequestForm, SecurityScopes
from passlib.context import CryptContext
from jose import JWTError, jwt

from pydantic import ValidationError

from ..models.user_model import User
from ..schemas import user_auth_schema

from ..config.config import get_configurations
from ..config.database import get_db

c = get_configurations()
SECRET_KEY = c.secret_key
HASH_ALGORITHM = c.hash_algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = c.access_token_expire_minutes

db = get_db()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    scopes={"userinfo": "gg"}
)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def get_hashed_password(plain):
    return pwd_context.hash(plain)

def create_access_token(data: dict, expire_minutes: int = ACCESS_TOKEN_EXPIRE_MINUTES):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expire_minutes)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=HASH_ALGORITHM)

    return encoded_jwt

def is_user_authenticated(form_data: OAuth2PasswordRequestForm):
    user = db.query(User).filter(User.email == form_data.username).first()

    if not user or \
        not verify_password(form_data.password, user.password):
        return False
    return user

async def get_current_user(security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)):
    authenticate_value = "Bearer" \
            + f' scope="{security_scopes.scope_str}"' if security_scopes.scopes else ''

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value}
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[HASH_ALGORITHM])
        email: str = payload.get("email")

        if not email:
            raise credentials_exception

        token_scopes = payload.get("scopes", [])
        token_data = user_auth_schema.TokenData(email=email, scopes=token_scopes)
    except (JWTError, ValidationError):
        raise credentials_exception

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise credentials_exception

    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value}
            )

    return user

async def get_current_active_user(current_user: User = Security(get_current_user, scopes=[])):
    if not current_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    return current_user