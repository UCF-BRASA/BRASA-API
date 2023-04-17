import uvicorn
from fastapi import FastAPI

from api.routes.base import router as api_router
from core.config import (
    API_PREFIX,
    DEBUG,
    PROJECT_NAME,
    VERSION,
    VERSION_PREFIX,
    app_tags_metadata,
)


def get_application() -> FastAPI:
    application = FastAPI(
        title=PROJECT_NAME, debug=DEBUG, version=VERSION, openapi_tags=app_tags_metadata
    )
    application.include_router(api_router, prefix=f"{API_PREFIX}{VERSION_PREFIX}")

    return application


def start_server() -> None:
    """Launched with `poetry run start` at root level"""
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)


app: FastAPI = get_application()
