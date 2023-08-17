from datetime import date
from typing import Optional

from beanie import Document
from pydantic import BaseModel


class Service(Document):
    name: str
    date_to_finish: date

    class Config:
        schema_extra = {"example": {"name": "", "date_to_finish": "2032-04-05"}}


class UpdateServiceModel(BaseModel):
    name: Optional[str]
    date_to_finish: Optional[date]

    class Collection:
        name = "service"

    class Config:
        schema_extra = {"example": {"name": "", "date_to_finish": "2032-04-05"}}
