from pydantic import BaseModel


## input models


class SignupForm(BaseModel):
    email: str
    first_name: str
    password: str


## output models


class User(BaseModel):
    id: int
    email: str
    first_name: str
