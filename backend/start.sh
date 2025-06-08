#!/bin/bash

# Load env vars from .env.render for Render
if [ -f .env.render ]; then
  export $(cat .env.render | xargs)
fi

echo "Running Alembic migration..."
alembic upgrade head

echo "Starting FastAPI server..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
