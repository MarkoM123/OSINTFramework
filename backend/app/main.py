from fastapi import FastAPI

from app.api.router import api_router
from app.db.base import Base
from app.db.session import engine

import app.models.asset
import app.models.finding
import app.models.scan

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="OSINT Framework",
)

app.include_router(api_router)


@app.get("/")
def root():
    return {"status": "ok"}