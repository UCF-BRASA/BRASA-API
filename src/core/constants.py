from core.config import settings

# response types
SUCCESS: str = "success"

# database related info
MAIN_DB: str = "dev-web" if settings.DEBUG else "prod-web"
USERS_COLLECTIONS: str = "brasa-users"
