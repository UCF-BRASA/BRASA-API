from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException

from core.auth import AuthHandler
from core.config import settings
from db.operations import add_user
from models.authentication import AuthDetails, RegisterUserDetails
from models.user import User

settings.app_tags_metadata.append(
    {"name": "Authentication", "description": "Authentication Routes"}
)
router = APIRouter(prefix="/auth", tags=["Authetication"])

#  main.py
auth_handler = AuthHandler()
users = []


@router.post("/register", status_code=201)
async def register(user_details: RegisterUserDetails):
    if any(x["username"] == user_details.username for x in users):
        raise HTTPException(status_code=400, detail="Username is taken")

    hashed_password = auth_handler.get_password_hash(user_details.password)
    new_user = User(
        username=user_details.username,
        password=hashed_password,
        fullname=user_details.fullname,
        date_of_birth=user_details.date_of_birth,
        gender=user_details.gender,
        origin_city=user_details.origin_city,
        major=user_details.major,
        school_year=user_details.school_year,
    )
    await add_user(new_user)
    # users.append({"username": user_details.username, "password": hashed_password})
    return


@router.post("/login")
def login(auth_details: AuthDetails):
    user = None

    for each_user in users:
        if each_user["username"] == auth_details.username:
            user = each_user
            break

    if (user is None) or (
        not auth_handler.verify_password(auth_details.password, user["password"])
    ):
        raise HTTPException(status_code=401, detail="Invalid username and/or password")
    token = auth_handler.encode_token(user["username"])
    return {"token": token}


@router.get("/unprotected")
def unprotected():
    return {"hello": "world"}


@router.get("/protected")
def protected(username=Depends(auth_handler.auth_wrapper)):
    return {"name": username}
