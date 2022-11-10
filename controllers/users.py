from fastapi import APIRouter, Response, status

import models.users

import usecases.users

router = APIRouter()


@router.get("/users/{user_id}")
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


@router.post("/users")
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
