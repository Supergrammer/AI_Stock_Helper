from fastapi import FastAPI

from .config.database import engine

from .models import models
from .routers import user_router, user_auth_router
from .config import config

models.Base.metadata.create_all(bind=engine)

setting = config.get_configurations()

app = FastAPI()
app.include_router(user_router.router)
app.include_router(user_auth_router.router)