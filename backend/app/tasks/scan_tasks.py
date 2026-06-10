import subprocess

from app.models.scan import Scan
from app.models.asset import Asset
from app.db.session import SessionLocal
from app.tasks.celery_app import celery_app


@celery_app.task
def scan_domain(scan_id: int, target: str):
    print(f"Starting scan {scan_id} for {target}")

    result = subprocess.run(
        ["subfinder", "-d", target, "-silent"],
        capture_output=True,
        text=True,
    )

    db = SessionLocal()

    try:
        for subdomain in result.stdout.splitlines():

            asset = Asset(
                scan_id=scan_id,
                asset_type="subdomain",
                value=subdomain,
            )

            db.add(asset)

        db.commit()

        scan = db.get(Scan, scan_id)

        if scan:
            scan.status = "completed"
            db.commit()

    finally:
        db.close()

    print(f"Finished scan {scan_id}")