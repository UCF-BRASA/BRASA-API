from fastapi import APIRouter, HTTPException

from core.config import app_tags_metadata
from schemas.prediction import TestRequest, TestResponse

app_tags_metadata.append({"name": "Services", "description": "Service Tag Description"})
router = APIRouter(prefix="/services", tags=["Services"])


@router.get(
    path="/add",
    response_model=TestResponse,
    name="Test endpoint",
)
async def mama(body: TestRequest):
    try:
        return TestResponse(
            salve=f"""Service Endpoint!
            name={body.name}
            other={body.other}"""
        )

    except Exception:
        raise HTTPException(status_code=404, detail="Some Exception")
