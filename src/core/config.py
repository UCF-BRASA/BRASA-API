from typing import Any, Dict, List

from pydantic import BaseSettings
from starlette.config import Config

envVariables = Config(env_file=".env")


class Settings(BaseSettings):
    # API routing prefix constants
    API_PREFIX: str = "/api"
    VERSION_PREFIX: str = "/v0.1"

    # metadata constants
    VERSION: str = "0.1.0"
    PROJECT_NAME: str = "UCF BRASA API"

    # tag metadata to be updated by each new route (for docs purposes)
    app_tags_metadata: List[Dict[str, Any]] = []

    # getting POETRY_ENV setting from .env
    POETRY_ENV: str = envVariables("POETRY_ENV", cast=str, default="development")

    # setting DEBUG setting
    DEBUG: bool = True if POETRY_ENV == "development" else False

    # getting DB env info
    DB_URI: str = envVariables("DB_URI", cast=str)
    DB_USERNAME: str = envVariables("DB_USERNAME", cast=str)
    DB_PASSWORD: str = envVariables("DB_PASSWORD", cast=str)

    # setting the URI completely
    DB_COMPLETE_URI: str = DB_URI % (DB_USERNAME, DB_PASSWORD)

    class Config:
        env_file = ".env"


settings = Settings()
