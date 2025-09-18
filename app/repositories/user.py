from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel.sql.expression import select

from app.models.user import User


class UserRepository:
    @staticmethod
    async def get_user_by_username(session: AsyncSession, username: str):
        stmt = select(User).where(User.username == username)
        res = await session.scalar(stmt)
        return res

    @staticmethod
    async def create_user(session: AsyncSession, user: User):
        session.add(user)
        return None
