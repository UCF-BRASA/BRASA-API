from datetime import datetime

from fastapi import APIRouter, HTTPException, status

from core.config import settings
from core.constants import SUCCESS
from models.base import Response
from models.services import UpdateServiceModel

# from schemas.prediction import TestRequest, TestResponse


settings.app_tags_metadata.append(
    {"name": "Services", "description": "Service Tag Description"}
)
router = APIRouter(prefix="/services", tags=["Services"])


@router.get(
    path="/add",
    response_model=Response,
    name="Test endpoint",
)
async def mama(body: UpdateServiceModel):
    try:
        return Response(
            status_code=status.HTTP_200_OK,
            response_type=SUCCESS,
            description="Successfully got a service",
            data=datetime.now().strftime("%Hh:%Mm:%Ss"),
        )

    except Exception:
        raise HTTPException(status_code=404, detail="Some Exception")
