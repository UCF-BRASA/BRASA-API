from models.services import Service
from models.user import User

user_collection = User
service_collection = Service


async def add_student(new_user: User) -> User | None:
    return await new_user.insert_one(new_user)
