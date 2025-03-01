from celery import Celery

app = Celery("backend", broker="redis://redis:6379/0")

app.config_from_object("backend.settings", namespace="CELERY")

app.autodiscover_tasks()