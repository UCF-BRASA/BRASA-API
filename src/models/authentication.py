# schemas.py
from typing import Union

from pydantic import BaseModel, Field
from typing_extensions import Annotated

from models.user import Gender, User


class AuthDetails(BaseModel):
    username: str
    password: str


class RegisterUserDetails(AuthDetails, User):
    fullname: str
    date_of_birth: str
    gender: Annotated[Union[Gender, None], Field(alias="Gender")] = None
    origin_city: str
    major: str
    school_year: int
