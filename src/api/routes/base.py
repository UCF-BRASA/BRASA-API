from fastapi import APIRouter, HTTPException, status

from api.routes.authentication import router as auth_router
from api.routes.services import router as service_router
from api.routes.users import router as users_router
from core.constants import SUCCESS
from models.base import Response

# include all routers
router = APIRouter()
router.include_router(router=users_router)
router.include_router(router=service_router)
router.include_router(router=auth_router)


# hello world router (for "/" path)
hello_world_router = APIRouter()


@hello_world_router.get(
    path="/",
    response_model=Response,
    name="Hello World",
)
async def hello_world():
    try:
        return Response(
            status_code=status.HTTP_200_OK,
            response_type=SUCCESS,
            description="Hello World endpoint",
            data=None,
        )

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Some Exception"
        )
