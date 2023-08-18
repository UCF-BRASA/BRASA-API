from models.services import Service
from models.user import User

user_collection = User
service_collection = Service


async def add_user(new_user: User) -> User | None:
    return await new_user.insert_one(new_user)


async def find_user(user_info: User) -> User | None:
    return await user_info.find_one({"username": user_info.username})
