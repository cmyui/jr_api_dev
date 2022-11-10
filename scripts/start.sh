source .env

uvicorn main:app \
    --reload \
    --host $APP_HOST \
    --port $APP_PORT
