from datetime import timedelta

from fastapi import APIRouter, HTTPException, status

from app.core.config import get_app_settings
from app.core.dependencies import DBSession, FormData, UserDep
from app.core.security import (
    Token,
    authenticate_user,
    create_access_token,
    get_password_hash,
)
from app.models.user import User, UserCreate, UserPublic
from app.repositories.user import UserRepository

settings = get_app_settings()

router = APIRouter(tags=["Security"])

def create_token(username: str) -> Token:
        access_token_expires = timedelta(minutes=settings.jwt_token_expiration_minutes)
        access_token = create_access_token(
            data={"sub": username}, expires_delta=access_token_expires
        )
        token = Token(access_token=access_token, token_type="bearer")
        return token

@router.post("/token")
async def get_token(session: DBSession, form_data: FormData):
    try:
        db_user = await UserRepository.get_user_by_username(
            session=session, username=form_data.username
        )
        user = authenticate_user(db_user=db_user, password=form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return create_token(username=user.username)
    except Exception as e:
        raise e


@router.get("/users/me")
async def get_user_me(current_user: UserDep):
    user_public = UserPublic.model_validate(current_user)
    return user_public


@router.post("/sign-up", status_code=status.HTTP_201_CREATED)
async def sing_up(session: DBSession, user_create: UserCreate):
    try:
        hashed_password = get_password_hash(user_create.password)
        user = User(
            username=user_create.username,
            hashed_password=hashed_password,
            email=user_create.email,
        )
        await UserRepository.create_user(session=session, user=user)
        return create_token(username=user.username)
    except Exception as e:
        raise e
