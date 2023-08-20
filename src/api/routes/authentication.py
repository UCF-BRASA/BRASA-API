import json
from datetime import datetime

from bson import json_util
from fastapi import APIRouter, Depends, HTTPException, status

from core.auth import AuthHandler, checkUCFEmail
from core.config import settings
from core.constants import SUCCESS
from db.operations import add_user, find_user
from models.authentication import (
    AuthDetails,
    LoginResponse,
    LoginResponseModel,
    RegisterResponse,
    RegisterUserDetails,
)
from models.user import User, UsernameModel

settings.app_tags_metadata.append(
    {"name": "Authentication", "description": "Authentication Routes"}
)
router = APIRouter(prefix="/auth", tags=["Authentication"])
auth_handler = AuthHandler()


@router.post("/register", status_code=201)
async def register(user_details: RegisterUserDetails):
    brasa_member_status = False

    # check if username (email) is already taken
    if await find_user(UsernameModel(username=user_details.username)):
        raise HTTPException(status_code=400, detail="Username is taken")
    if checkUCFEmail(user_details.username) is False:
        raise HTTPException(status_code=400, detail="Invalid UCF email")
    else:
        brasa_member_status = True

    # hash user's password
    hashed_password = auth_handler.get_password_hash(user_details.password)

    # create new user with given info
    new_user = User(
        username=user_details.username,
        password=hashed_password,
        first_name=user_details.first_name,
        last_name=user_details.last_name,
        date_of_birth=user_details.date_of_birth,
        gender=user_details.gender,
        origin_city=user_details.origin_city,
        major=user_details.major,
        school_year=user_details.school_year,
        brasa_member=brasa_member_status,
        created_at=datetime.utcnow(),
    )

    # create user on DB
    try:
        await add_user(new_user)
        return RegisterResponse(
            status_code=status.HTTP_200_OK,
            response_type=SUCCESS,
            description="User created successfully",
            data=new_user,
        )

    except Exception as e:
        return {"error": e}


@router.post("/login")
async def login(auth_details: AuthDetails):
    user = await find_user(UsernameModel(username=auth_details.username))

    # check if user exists and if password is correct
    if (user is None) or (
        not auth_handler.verify_password(auth_details.password, user["password"])
    ):
        raise HTTPException(status_code=401, detail="Invalid username and/or password")

    # if all is good, get and return the JWT token
    token = auth_handler.encode_token(user["username"])

    # loginResponse = JSONResponse({"message": "Login successful", "token": token})

    # expires = datetime.today() - timedelta(hours=0, minutes=2)

    # loginResponse.set_cookie(
    #     key="jwt_token",
    #     value=token,
    #     secure=True,
    #     httponly=True,
    #     expires=expires.strftime("%H:%M:%S GMT"),
    # )

    # id = user["_id"]
    # first_name = user["first_name"]
    # last_name = user["last_name"]
    # date_of_birth = user["date_of_birth"]
    # gender = user["gender"]
    # origin_city = user["origin_city"]
    # major = user["major"]
    # school_year = user["school_year"]

    return LoginResponse(
        status_code=status.HTTP_200_OK,
        response_type=SUCCESS,
        description="Login successful",
        data=LoginResponseModel(
            id=user["_id"],
            token=token,
            username=user["username"],
            first_name=user["first_name"],
            last_name=user["last_name"],
            date_of_birth=user["date_of_birth"],
            gender=user["gender"],
            origin_city=user["origin_city"],
            major=user["major"],
            school_year=user["school_year"],
        ),
    )


@router.get("/get_user_info")
async def get_user_info(username=Depends(auth_handler.auth_wrapper)):
    user = await find_user(UsernameModel(username=username))

    first_name = user["first_name"]
    last_name = user["last_name"]

    return {"first_name": first_name, "last_name": last_name}


def parse_json(data):
    return json.loads(json_util.dumps(data))
