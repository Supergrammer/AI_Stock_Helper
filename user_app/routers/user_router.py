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
# NOTE: /user/signup : 회원가입
@router.post("/signup", response_model=user_schema.UserRead)
async def create_user(user: user_schema.UserCreateOrUpdate):
    if not user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password has not been entered")
    if user_service.get_user_by_email(email=user.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    return user_service.create_user(user)

# NOTE: /user/get : id 또는 email 로부터 유저 정보를 반환
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

# NOTE: /user/get/all : 모든 유저의 정보를 반환
@router.get("/get/all", response_model=List[user_schema.UserRead])
async def get_all_users(skip: Optional[int] = None, limit: Optional[int] = None):
    return user_service.get_all_users(skip=skip, limit=limit)

# NOTE: /user/update : 유저 정보 업데이트
@router.put("/update", response_model=user_schema.UserRead)
async def update_user(user: user_schema.UserCreateOrUpdate):
    db_user = user_service.get_user_by_email(email=user.email)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User does not exist")
    return user_service.update_user(user)

# NOTE: /user/signout : email 을 인자로 받아 회원탈퇴
@router.delete("/signout", response_model=user_schema.UserRead)
async def delete_user(email: str):
    db_user = user_service.get_user_by_email(email)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User does not exist")
    return user_service.delete_user(email)