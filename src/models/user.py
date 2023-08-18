from enum import Enum
from typing import Optional, Union

from beanie import Document
from pydantic import BaseModel, Field
from typing_extensions import Annotated

from core.constants import USERS_COLLECTIONS
from models.base import Response


class Gender(str, Enum):
    men = "Men"
    woman = "Woman"
    non_binary = "Non-binary"
    other = "Other"
    no_disclosure = "Prefer not to say"


class User(Document):
    username: str  # this will be the user's email
    password: str
    fullname: str
    date_of_birth: str
    gender: Annotated[Union[Gender, None], Field(alias="Gender")] = None
    origin_city: str
    major: str
    school_year: int

    class Settings:
        # collection name
        name = USERS_COLLECTIONS

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Pedro Fachetti Carvalho",
                "email": "pedro@gmail.com",
                "gender": "Male",
                "course_of_study": "Computer Science",
                "year": 4,
                "gpa": 3.7,
            }
        }


class OptionalUserModel(BaseModel):
    fullname: Optional[str]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Pedro Fachetti Carvalho",
                "email": "pedro@school.com",
                "course_of_study": "Water resources and environmental engineering",
                "year": 4,
                "gpa": 4.0,
            }
        }


class UserResponse(Response):
    data: User | None
