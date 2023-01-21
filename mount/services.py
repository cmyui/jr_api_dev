from databases import Database

import settings


def create_dsn(
    driver: str,
    user: str,
    password: str,
    host: str,
    port: int,
    database: str,
):
    return f"{driver}://{user}:{password}@{host}:{port}/{database}"


database = Database(
    create_dsn(
        driver="mysql",
        user=settings.DB_USER,
        password=settings.DB_PASS,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        database=settings.DB_NAME,
    )
)
