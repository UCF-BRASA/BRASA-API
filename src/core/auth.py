from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext

from core.config import settings


class AuthHandler:
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def encode_token(self, user_id):
        payload = {
            "exp": datetime.utcnow()
            + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
            "iat": datetime.utcnow(),
            "sub": user_id,
        }
        return jwt.encode(payload, settings.AUTH_SECRET_KEY, algorithm=settings.ALGORITHM)

    def decode_token(self, token):
        try:
            payload = jwt.decode(
                token, settings.AUTH_SECRET_KEY, algorithms=[settings.ALGORITHM]
            )
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Signature has expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)


def checkUCFEmail(user_email) -> bool:
    domain = user_email.split("@")[1]
    if domain == settings.UCF_DOMAIN:
        return True

    return False
