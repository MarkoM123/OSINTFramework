from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.scan import Scan

router = APIRouter()


class ScanCreate(BaseModel):
    target: str


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/scans")
def create_scan(
    payload: ScanCreate,
    db: Session = Depends(get_db),
):
    scan = Scan(
        target=payload.target,
        status="pending",
    )

    db.add(scan)
    db.commit()
    db.refresh(scan)

    return {
        "scan_id": scan.id,
        "status": scan.status,
        "target": scan.target,
    }