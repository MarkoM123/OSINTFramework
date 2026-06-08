from celery import Celery

celery_app = Celery(
    "osint",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
    include=["app.tasks.scan_tasks"],
)

celery_app.conf.update(
    task_track_started=True,
)