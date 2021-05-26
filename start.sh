#!/bin/sh
python manage.py migrate
python manage.py process_tasks --sleep 600 &
python manage.py runserver 0.0.0.0:80
