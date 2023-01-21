#!/usr/bin/env bash
mysql \
    --host=$DB_HOST \
    --port=$DB_PORT \
    --user=$DB_USER \
    --password=$DB_PASS \
    --execute="CREATE DATABASE IF NOT EXISTS ${DB_NAME}"

echo "${DB_NAME} database created (if it didn't exist)"
