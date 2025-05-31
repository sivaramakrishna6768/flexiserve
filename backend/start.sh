#!/bin/sh

# Just use the provided DATABASE_URL from Render environment
export DATABASE_URL=${DATABASE_URL}

echo "Waiting for db:5432...--timeout=30..."
wait-for-it.sh "${DATABASE_URL##*@}" -t 30 -- echo "Postgres is up"

echo "Running Alembic migrations..."
alembic upgrade head

echo "Starting FastAPI server..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
