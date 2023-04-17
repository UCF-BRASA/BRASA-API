from typing import Any, Dict, List

from starlette.config import Config

envVariables = Config(env_file=".env")

# API routing prefix constants
API_PREFIX = "/api"
VERSION_PREFIX = "/v0.1"

# metadata constants
VERSION = "0.1.0"
PROJECT_NAME = "BRASA API"

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
