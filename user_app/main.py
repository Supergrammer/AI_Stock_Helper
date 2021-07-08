from fastapi import FastAPI

from .config.database import engine

from .models import models
from .routers import routers

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(routers.router)