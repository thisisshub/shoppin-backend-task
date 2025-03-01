#!/bin/sh

if [ "$1" = "celery" ]; then
    exec poetry run celery -A backend.celery worker --loglevel=info
else
    exec poetry run python manage.py runserver 0.0.0.0:8000
fi 