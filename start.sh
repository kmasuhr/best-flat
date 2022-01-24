#!/usr/bin/env sh

cd backend
#python manage.py runserver --noreload
gunicorn flats_ui.wsgi:application --bind 0.0.0.0:$PORT
