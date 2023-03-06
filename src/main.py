from fastapi import FastAPI
import uvicorn

from api.routes.endpoints import router as api_router
from core.config import API_PREFIX, VERSION_PREFIX, DEBUG, PROJECT_NAME, VERSION


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    application.include_router(api_router, prefix=f'{API_PREFIX}{VERSION_PREFIX}')

    return application

app = get_application()

def start_server():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
