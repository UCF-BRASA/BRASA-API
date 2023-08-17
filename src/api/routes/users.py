# from datetime import datetime

from fastapi import APIRouter, HTTPException, status

from core.config import settings
from core.constants import SUCCESS
from db.operations import add_student

# from models.base import Response
from models.user import User, UserResponse

settings.app_tags_metadata.append(
    {"name": "Users", "description": "Users Tag Description"}
)
router: APIRouter = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    path="/add",
    response_model=UserResponse,
    name="Adds a user",
)
async def add(body: User):
    try:
        new_user = await add_student(body)

        return UserResponse(
            status_code=status.HTTP_200_OK,
            response_type=SUCCESS,
            description="Successfully added a user",
            data=new_user,
        )

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Some Exception"
        )
