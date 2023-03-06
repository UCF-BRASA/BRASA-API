from fastapi import APIRouter

from api.routes.users import router as users_router
from api.routes.services import router as service_router

router = APIRouter()
router.include_router(router=users_router)
router.include_router(router=service_router)
