import time

from app.tasks.celery_app import celery_app


@celery_app.task
def scan_domain(scan_id: int, target: str):
    print(f"Starting scan {scan_id} for {target}")

    time.sleep(10)

    print(f"Finished scan {scan_id}")