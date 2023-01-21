#!/usr/bin/env python3
from fastapi import FastAPI

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
