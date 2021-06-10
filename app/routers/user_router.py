from fastapi import APIRouter, Depends, HTTPException
from ..services import user_service

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@router.get("/")
def get_all_users():
    return user_service.get_all_user()