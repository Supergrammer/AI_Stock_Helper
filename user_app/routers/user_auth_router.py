from fastapi import APIRouter, HTTPException, status, Depends, Security

from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from ..models.user_model import User
from ..schemas import user_auth_schema
from ..services import user_auth_service

router = APIRouter(
    prefix="/user/auth",
    tags=["auth"],
)

@router.post("/token", response_model=user_auth_schema.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_auth_service.is_user_authenticated(form_data=form_data)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    
    access_token = user_auth_service.create_access_token(
        data={"email": user.email, "scopes": form_data.scopes})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/my_info")
async def read_user_info(current_user: User = Security(user_auth_service.get_current_active_user, scopes=["userinfo"])):
    return current_user