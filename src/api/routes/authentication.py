import json
from datetime import datetime, timedelta

import jwt
from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError

from core.auth import checkUCFEmail
from core.config import settings
from core.constants import SUCCESS
from core.hashing import Hasher
from core.security import create_access_token
from db.operations import add_user, find_user
from models.authentication import (
    LoginResponseModel,
    RegisterResponse,
    RegisterUserDetails,
    Token,
)
from models.user import User, UsernameModel, UserResponse

from ..utils.OAuth2 import (
    OAuth2PasswordBearerWithCookie,
    authenticate_user,
    get_current_user,
)

settings.app_tags_metadata.append(
    {"name": "Authentication", "description": "Authentication Routes"}
)
router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/token", response_model=Token)
async def login_for_access_token(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
):  # added response as a function parameter
    user = await authenticate_user(
        username=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    response.set_cookie(
        key="access_token",
        value=f"Bearer {access_token}",
        httponly=True,
        secure=True,
        samesite="none",
    )  # set HttpOnly cookie in response

    return Token(access_token=access_token, token_type="bearer")


@router.post("/register", response_model=RegisterResponse)
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
    hashed_password = Hasher.get_password_hash(user_details.password)

    # create new user with given info
    new_user = User(
        username=user_details.username,
        password=hashed_password,
        firstName=user_details.firstName,
        lastName=user_details.lastName,
        dateOfBirth=user_details.dateOfBirth,
        gender=user_details.gender,
        originCity=user_details.originCity,
        major=user_details.major,
        schoolYear=user_details.schoolYear,
        isBrasaMember=brasa_member_status,
        createdAt=datetime.utcnow(),
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


@router.get("/user-profile", response_model=UserResponse)
async def read_user_profile(current_user: User = Depends(get_current_user)):
    """
    Retrieve the user's profile data.
    """
    return UserResponse(
        status_code=status.HTTP_200_OK,
        response_type=SUCCESS,
        description="User acquired",
        data=current_user,
    )
