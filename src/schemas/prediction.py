from pydantic import BaseModel


class TestResponse(BaseModel):
    salve: str


class TestRequest(BaseModel):
    name: str
    other: int
