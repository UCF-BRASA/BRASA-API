import uvicorn
from fastapi import FastAPI

from api.routes.authentication import AuthHandler
from api.routes.base import hello_world_router
from api.routes.base import router as api_router
from core.config import settings
from db.init_db import initiate_database


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
        version=settings.VERSION,
        openapi_tags=settings.app_tags_metadata,
    )
    application.include_router(hello_world_router)
    application.include_router(
        api_router, prefix=f"{settings.API_PREFIX}{settings.VERSION_PREFIX}"
    )

    return application


def start_server() -> None:
    """Launched with `poetry run start` at root level"""
    uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT, reload=True)


app: FastAPI = get_application()


@app.on_event(event_type="startup")
async def start_database():
    await initiate_database()


@app.on_event(event_type="startup")
async def start_auth_service():
    auth_handler = AuthHandler()
    return auth_handler
