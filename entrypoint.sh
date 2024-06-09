#!/bin/sh
# Run the database migrations
alembic upgrade head

#run server
if [ "$API_ENVIRONMENT" = "development" ]; then
    echo "API_ENVIRONMENT development"
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload

elif [ "$API_ENVIRONMENT" = "production" ]; then
    echo "API_ENVIRONMENT production"
    gunicorn -k uvicorn.workers.UvicornWorker -c gunicorn_conf.py main:app

else
    echo "API_ENVIRONMENT is invalid"
    exit 1
fi
