from typing import Optional

from beanie import Document
from pydantic import BaseModel

from core.constants import USERS_COLLECTIONS
from models.base import Response


class User(Document):
    fullname: str
    course_of_study: str
    year: int
    gpa: float

    class Settings:
        # collection name
        name = USERS_COLLECTIONS

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Pedro Fachetti Carvalho",
                "email": "pedro@gmail.com",
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
