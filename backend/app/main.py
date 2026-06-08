from fastapi import FastAPI

from app.db.base import Base
from app.db.session import engine

import app.models.scan

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"status": "ok"}