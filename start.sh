#!/bin/bash
function wait_for_db_migration () {
    while ! python3 manage.py sqlflush > /dev/null 2>&1; do
        echo "Waiting for the Database to be ready..."

        sleep 5
    done

    echo "Database is ready, running migrations..."

    python3 manage.py migrate --noinput
}

echo "Running Database migrations..."
wait_for_db_migration;

echo "Collecting staticfiles..."
python3 manage.py collectstatic --noinput

echo "Configuring and gunicorn webserver..."
NUM_CPU=`nproc`
NUM_WORKERS=${GUNICORN_WORKERS:=$(( 2 * NUM_CPU + 1))}
NUM_THREADS=${NUM_WORKERS}

echo "Spawing $NUM_WORKERS gthread workers"
gunicorn app.wsgi:application --bind 0.0.0.0:4444 --workers $NUM_WORKERS --threads $NUM_THREADS
