from typing import Union

from pydantic import BaseModel, Field
from typing_extensions import Annotated

from models.base import Response
from models.user import Gender, User


class AuthDetails(BaseModel):
    username: str
    password: str


class RegisterUserDetails(AuthDetails):
    first_name: str
    last_name: str
    date_of_birth: str
    gender: Annotated[Union[Gender, None], Field(alias="gender")] = None
    origin_city: str
    major: str
    school_year: str


class Token(BaseModel):
    token: str


class RegisterResponse(Response):
    data: User | None


class LoginResponse(Response):
    data: Token | None
