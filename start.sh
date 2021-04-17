#!/bin/sh

echo "Installing Python dependencies..."
pipenv install --system --deploy

echo "Running Database migrations..."
python3 manage.py migrate

echo "Collecting static files..."
python3 manage.py collectstatic --noinput

echo "Configuring and gunicorn webserver..."
NUM_CPU=`nproc`
NUM_WORKERS=${GUNICORN_WORKERS:=$(( 2 * NUM_CPU + 1))}

echo "Spawing $NUM_WORKERS gevent workers"
gunicorn karobari.wsgi:application --bind 0.0.0.0:4444 --workers $NUM_WORKERS