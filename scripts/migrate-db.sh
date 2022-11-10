source .env

MIGRATIONS_PATH=migrations
MIGRATIONS_SCHEMA_TABLE=schema_migrations

DB_DSN="mysql://${DB_USER}:${DB_PASS}@tcp(${DB_HOST}:${DB_PORT})/${DB_NAME}?x-migrations-table=${MIGRATIONS_SCHEMA_TABLE}"


case "$1" in
    "up")
        migrate -path ${MIGRATIONS_PATH} -database "${DB_DSN}" up
        ;;
    "down")
        migrate -path ${MIGRATIONS_PATH} -database "${DB_DSN}" down
        ;;
    "version")
        migrate -path ${MIGRATIONS_PATH} -database "${DB_DSN}" version
        ;;
    "force")
        migrate -path ${MIGRATIONS_PATH} -database "${DB_DSN}" force $2
        ;;
    "create")
        shift
        raw_input=$@
        lower_input=${raw_input,,}
        lower_snake_case_input=${lower_input// /_}
        migrate create -seq -ext sql -dir ${MIGRATIONS_PATH} $lower_snake_case_input
        ;;
    *)
        echo "Usage: $0 {up|down|version|force|create}"
        exit 1
esac
