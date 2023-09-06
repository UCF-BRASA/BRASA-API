from typing import Optional, Union

from beanie import PydanticObjectId
from pydantic import BaseModel, Field
from typing_extensions import Annotated

from models.base import Response
from models.user import Gender, User


class AuthDetails(BaseModel):
    username: str
    password: str


class RegisterUserDetails(AuthDetails):
    firstName: str
    lastName: str
    dateOfBirth: str
    gender: Annotated[Union[Gender, None], Field(alias="gender")] = None
    originCity: str
    major: str
    schoolYear: str


class LoginResponseModel(BaseModel):
    id: Optional[PydanticObjectId]
    username: str  # this will be the user's email
    firstName: str
    lastName: str
    dateOfBirth: str
    gender: Annotated[Union[Gender, None], Field(alias="gender")] = None
    originCity: str
    major: str
    schoolYear: str


class RegisterResponse(Response):
    data: User | None


class LoginResponse(Response):
    data: LoginResponseModel | None


class Token(BaseModel):
    access_token: str
    token_type: str
