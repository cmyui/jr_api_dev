#!/usr/bin/env python3
import uvicorn
from fastapi import FastAPI

import settings
import services

import controllers.users

app = FastAPI()

app.include_router(controllers.users.router)


@app.on_event("startup")
async def on_startup():
    await services.database.connect()


@app.on_event("shutdown")
async def on_shutdown():
    await services.database.disconnect()


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
    )
