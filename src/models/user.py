from datetime import datetime
from enum import Enum
from typing import Union

from beanie import Document
from pydantic import BaseModel, Field
from typing_extensions import Annotated

from core.constants import USERS_COLLECTIONS
from models.base import Response


class Gender(str, Enum):
    men = "Man"
    woman = "Woman"
    non_binary = "Non-binary"
    other = "Other"
    no_disclosure = "Prefer not to say"


class User(Document):
    username: str  # this will be the user's email
    password: str
    firstName: str
    lastName: str
    dateOfBirth: str
    gender: Annotated[Union[Gender, None], Field(alias="gender")] = None
    originCity: str
    major: str
    schoolYear: str
    isBrasaMember: bool = Field(default=False)
    userStatus: str = Field(default="active")
    createdAt: datetime

    class Settings:
        # collection name
        name = USERS_COLLECTIONS

    class Config:
        schema_extra = {
            "example": {
                "username": "some_email@ucf.edu",  # this will be the user's email
                "password": "some_password",
                "first_name": "First name",
                "last_name": "Last name",
                "date_of_birth": "DD/MM/YYYY",
                "gender": "Men | Woman | Non-binary | Other | Prefer not to say",
                "origin_city": "Rio de Janeiro",
                "major": "Computer Science",
                "school_year": "Senior",
            }
        }


class UsernameModel(BaseModel):
    username: str

    class Settings:
        # collection name
        name = USERS_COLLECTIONS


class UserResponse(Response):
    data: User | None
