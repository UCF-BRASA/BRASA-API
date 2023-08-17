from fastapi import status
from fastapi.testclient import TestClient

from core.constants import SUCCESS
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "status_code": status.HTTP_200_OK,
        "response_type": SUCCESS,
        "description": "Hello World endpoint",
        "data": None,
    }
