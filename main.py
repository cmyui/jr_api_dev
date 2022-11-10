#!/usr/bin/env python3
import uvicorn
from fastapi import FastAPI, Response, status

import models.users
import settings
import services
import usecases.users

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await services.database.connect()


@app.on_event("shutdown")
async def on_shutdown():
    await services.database.disconnect()


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user_row = await usecases.users.get_user(user_id)
    if user_row is None:
        return Response(
            content="User not found.",
            status_code=status.HTTP_404_NOT_FOUND,
        )

    return models.users.User(
        id=user_row["id"],
        email=user_row["email"],
        first_name=user_row["first_name"],
    )


@app.post("/users")
async def create_user(signup_data: models.users.SignupForm):
    user_row = await usecases.users.create_user(
        email=signup_data.email,
        first_name=signup_data.first_name,
        password=signup_data.password,
    )
    if user_row is None:
        return Response(
            content="Failed to create user.",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return models.users.User(
        id=user_row["id"],
        email=user_row["email"],
        first_name=user_row["first_name"],
    )


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
    )
