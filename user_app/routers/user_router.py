from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, HTTPException, status
from ..schemas import user_schema
from ..services import user_service


router = APIRouter(
    prefix="/user",
    tags=["user"],
)

# TODO: async await
@router.get("/get", response_model=user_schema.UserRead)
async def get_user_by_id_or_email(id: Optional[UUID] = None, email: Optional[str] = None):
    if not bool(id) ^ bool(email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    else:
        user = user_service.get_user_by_id(id=id) if id \
            else user_service.get_user_by_email(email=email)

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return user

@router.get("/get/all", response_model=List[user_schema.UserRead])
async def get_all_users(skip: Optional[int] = None, limit: Optional[int] = None):
    return user_service.get_all_users(skip=skip, limit=limit)

@router.post("/signup", response_model=user_schema.User)
async def create_user(user: user_schema.UserCreate):
    db_user = user_service.get_user_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    return user_service.create_user(user)

@router.delete("/signout", response_model=user_schema.UserRead)
async def delete_user(user: user_schema.UserDelete):
    db_user = user_service.get_user_by_email(email=user.email)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User does not exist")
    return user_service.delete_user(user)