from fastapi import FastAPI

from .config.database import engine

from .models import user_model
from .routers import user_router, user_auth_router
from .config import config

user_model.Base.metadata.create_all(bind=engine)

setting = config.get_configurations()

app = FastAPI()
app.include_router(user_router.router)
app.include_router(user_auth_router.router)