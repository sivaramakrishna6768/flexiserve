#!/bin/bash

echo "Waiting for database..."
./wait-for-it.sh "$DB_HOST" 5432 --timeout=30 --strict -- echo "Database is up"

echo "Running Alembic migration..."
alembic upgrade head

echo "Starting FastAPI server..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
