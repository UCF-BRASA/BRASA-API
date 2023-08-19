from db.init_db import brasa_users_collection
from models.services import Service
from models.user import User, UsernameModel

user_collection = User
service_collection = Service


async def add_user(new_user: User) -> User | None:
    return await new_user.insert_one(new_user)


async def find_user(user_info: UsernameModel) -> User:
    return await brasa_users_collection.find_one({"username": user_info.username})
