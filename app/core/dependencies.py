from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import get_app_settings
from app.core.container import container
from app.core.security import TokenData
from app.models.user import User
from app.repositories.user import UserRepository

settings = get_app_settings()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

DBSession = Annotated[AsyncSession, Depends(container.session)]
JWTToken = Annotated[OAuth2PasswordBearer, Depends(oauth2_scheme)]
FormData = Annotated[OAuth2PasswordRequestForm, Depends()]


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)], session: DBSession
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm]
        )
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except jwt.InvalidTokenError:
        raise credentials_exception
    user = await UserRepository.get_user_by_username(
        session=session, username=token_data.username
    )
    if user is None:
        raise credentials_exception
    return token_data.username


UserDep = Annotated[User, Depends(get_current_user)]
