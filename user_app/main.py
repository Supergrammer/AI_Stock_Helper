from fastapi import FastAPI, Depends

from .config.database import engine

from .models import user_model
from .routers import user_router
from .config import config

user_model.Base.metadata.create_all(bind=engine)

setting = config.get_configurations()

app = FastAPI()
app.include_router(user_router.router)