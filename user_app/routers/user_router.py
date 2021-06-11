from fastapi import APIRouter, Depends, HTTPException
from ..schemas import user_schema
from ..services import user_service

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@router.get("/")
def get_all_users():
    return user_service.get_all_user()

# @router.post("/signup", response_model=user_schema.User_response)
# def create_user(user: user_schema.UserCreate):
#     db_user = user_service.get_user_by_email(email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already exist...")
#     return user_service.create_user

@router.post("/signup")
def create_user(user: user_schema.User_request):
    return user_service.create_user(user=user)