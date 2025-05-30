#!/bin/sh

# Wait for Postgres to be available
echo "Waiting for Postgres..."

until nc -z -v -w30 db 5432
do
  echo "Waiting for database connection..."
  sleep 1
done

echo "Postgres is up - running migrations..."
alembic upgrade head

echo "Starting FastAPI server..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
