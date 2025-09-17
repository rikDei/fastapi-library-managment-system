from datetime import datetime, timedelta, timezone

import jwt
from app.core.config import get_app_settings
from passlib.context import CryptContext
from pydantic import BaseModel, Field

from app.models.user import User

settings = get_app_settings()

pwd_context = CryptContext(schemes=["bcrypt"])


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(secret=plain_password, hash=hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def authenticate_user(db_user: User | None, password: str):
    if not db_user:
        return False
    if not verify_password(password, db_user.hashed_password):
        return False
    return db_user


class Token(BaseModel):
    access_token: str
    token_type: str = Field(default="Bearer")


def create_access_token(
    data: dict,
    expires_delta: timedelta = timedelta(minutes=settings.jwt_token_expiration_minutes),
):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.jwt_secret_key, algorithm=settings.jwt_algorithm
    )
    return encoded_jwt


class TokenData(BaseModel):
    username: str | None = None
