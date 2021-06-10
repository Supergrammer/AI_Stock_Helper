import uvicorn
from fastapi import FastAPI

# TODO : Cannot use relative import in main.py
# from config.database import SessionLocal

from .routers import user_router
from .config.database import engine
from .models import user_model

user_model.Base.metadata.create_all(bind=engine)

def create_app():
    app = FastAPI()
    return app

app = FastAPI()

app.include_router(user_router.router)

# if __name__ == "__main__":
#    uvicorn.run("main:app", host="0.0.0.0", port=7000, workers=4, reload=True)