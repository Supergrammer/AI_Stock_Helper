from fastapi import APIRouter, HTTPException, status, Depends

from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from ..modules import oauth_module
from ..schemas import user_schema, token_schema

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

class ProxyUser():
    def __init__(self, user = Depends(oauth_module.get_current_active_user)):
        self.user = user

@router.post("/token", response_model=token_schema.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = oauth_module.is_authenticated_user(form_data=form_data)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    
    access_token = oauth_module.create_access_token( \
        data={"email": user.email, "scopes": form_data.scopes})
    return {"access_token": access_token, "token_type": "bearer"}

# @router.get("/my_info", response_model=user_schema.UserRead)
# async def read_user_info(current_user = Depends(ProxyUser)):
#     return current_user