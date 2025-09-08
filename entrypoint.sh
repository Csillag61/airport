#!/bin/sh

# Wait for PostgreSQL
if [ "$DATABASE_URL" != "" ]; then
	echo "Waiting for postgres..."
	while ! nc -z db 5432; do
		sleep 1
	done
fi

# Run migrations and collectstatic
python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn airport.wsgi:application --bind 0.0.0.0:8000
