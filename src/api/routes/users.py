from fastapi import APIRouter, HTTPException

from core.config import app_tags_metadata
from schemas.prediction import TestRequest, TestResponse

app_tags_metadata.append({"name": "Users", "description": "Users Tag Description"})
router: APIRouter = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    path="/add",
    response_model=TestResponse,
    name="Adds a user",
)
async def add(body: TestRequest):
    try:
        name = body.name
        other = body.other

        return TestResponse(salve=f"name={name} -> other={other}")

    except Exception:
        raise HTTPException(status_code=404, detail="Some Exception")
