#!/bin/bash

# Detect database host
DB_HOST=${DB_HOST:-db}

echo "Waiting for PostgreSQL at $DB_HOST:5432..."
./wait-for-it.sh $DB_HOST:5432 --timeout=30 --strict -- echo "Postgres is up"

# Run Alembic migrations
alembic upgrade head

# Start the FastAPI app
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
