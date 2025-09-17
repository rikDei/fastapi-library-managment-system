from datetime import datetime, timedelta, timezone

import bcrypt
import jwt
from pydantic import BaseModel, Field

from app.core.config import get_app_settings
from app.models.user import User

settings = get_app_settings()


def verify_password(plain_password: str, hashed_password: str):
    return bcrypt.checkpw(
        password=plain_password.encode("utf-8"),
        hashed_password=hashed_password.encode("utf-8"),
    )


def get_password_hash(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


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
