#!/bin/sh
echo "Running Database migrations..."
python3 manage.py migrate

echo "Configuring and gunicorn webserver..."
NUM_CPU=`nproc`
NUM_WORKERS=${GUNICORN_WORKERS:=$(( 2 * NUM_CPU + 1))}

echo "Spawing $NUM_WORKERS gevent workers"
gunicorn app.wsgi:application --bind 0.0.0.0:4444 --workers $NUM_WORKERS
