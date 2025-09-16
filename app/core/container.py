from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.config import get_app_settings
from app.core.settings.base import BaseAppSettings


class Container:
    """Dependency injector project container."""

    def __init__(self, settings: BaseAppSettings) -> None:
        self._settings: BaseAppSettings = settings
        self._engine: AsyncEngine = create_async_engine(self._settings.sql_db_uri)

    async def session(self) -> AsyncIterator[AsyncSession]:
        async with AsyncSession(self._engine) as session:
            try:
                yield session
                await session.commit()
            except Exception:
                await session.rollback()
                raise
            finally:
                await session.close()


container = Container(settings=get_app_settings())
