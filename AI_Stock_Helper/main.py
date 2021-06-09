from typing import Optional

import uvicorn
from fastapi import FastAPI

def create_app():
    app = FastAPI()
    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=7000, workers=4, reload=True)