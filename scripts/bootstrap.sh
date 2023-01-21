#!/usr/bin/env bash
cd /srv/root

/scripts/await-service.sh $DB_HOST $DB_PORT
/scripts/init-db.sh
/scripts/migrate-db.sh up

exec /scripts/run-api.sh
