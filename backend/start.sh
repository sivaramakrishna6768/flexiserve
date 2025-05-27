#!/bin/bash
./wait-for-it.sh db 5432
echo "Database is up"

alembic upgrade head
uvicorn app.main:app --host 0.0.0.0 --port 8000
