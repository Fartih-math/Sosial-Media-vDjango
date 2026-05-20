#!/usr/bin/env bash

echo "==> Running Database Migrations..."
python manage.py migrate --noinput

echo "==> Creating Default Superuser..."
python manage.py createsuperuser --noinput || echo "Superuser already exists or skipped."

echo "==> Starting Web Server..."
gunicorn project_name.wsgi:application
