
from starlette.config import Config
from starlette.datastructures import Secret


config = Config(".env")

# prefix constants
API_PREFIX = "/api"
VERSION_PREFIX="/v0.1"

# metadata constants
VERSION = "0.1.0"
PROJECT_NAME = "BRASA API"

# getting DEBUG setting from .env
DEBUG: bool = config("DEBUG", cast=bool, default=False)

