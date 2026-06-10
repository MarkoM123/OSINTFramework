from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.models.asset import Asset
from app.db.session import SessionLocal
from app.models.scan import Scan
from app.tasks.scan_tasks import scan_domain
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
    scan_domain.delay(
    scan.id,
    scan.target,
)

    return {
        "scan_id": scan.id,
        "status": scan.status,
        "target": scan.target,
    }
@router.get("/scans/{scan_id}")
def get_scan(
    scan_id: int,
    db: Session = Depends(get_db),
):
    scan = db.get(Scan, scan_id)

    if not scan:
        return {"error": "Scan not found"}

    assets = (
        db.query(Asset)
        .filter(Asset.scan_id == scan_id)
        .all()
    )

    return {
        "scan_id": scan.id,
        "target": scan.target,
        "status": scan.status,
        "asset_count": len(assets),
        "assets": [
            asset.value
            for asset in assets[:100]
        ],
    }