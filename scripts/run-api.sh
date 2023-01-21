#!/usr/bin/env bash
exec uvicorn \
    --host $APP_HOST \
    --port $APP_PORT \
    api_boot:app
