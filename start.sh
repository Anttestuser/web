#!/bin/sh

sleep 10

python manage.py migrate
python manage.py collectstatic --noinput
gunicorn --bind 0.0.0.0:8000 web.wsgi --timeout 0

