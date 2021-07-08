from fastapi.routing import APIRouter

from .app_router import router as app_router
# from .user_auth_router import router as user_auth_router
from .user_router import router as user_router

router = APIRouter()
router.include_router(app_router)
# router.include_router(user_auth_router)
router.include_router(user_router)