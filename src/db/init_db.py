from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from core.config import settings
from core.constants import MAIN_DB
from models.services import Service
from models.user import User

client = AsyncIOMotorClient(settings.DB_COMPLETE_URI)
mongo_db = client.get_database(MAIN_DB)
brasa_users_collection = mongo_db.get_collection("brasa-users")


async def initiate_database():
    await init_beanie(
        database=client.get_database(MAIN_DB),
        document_models=[User, Service],  # type: ignore
    )
