from sqlalchemy.engine.url import URL


import logging

from pydantic import computed_field
from sqlalchemy.pool.impl import NullPool

from app.core.settings.app import AppSettings


class TestAppSettings(AppSettings):
    """
    Test application settings.
    """

    debug: bool = True

    title: str = "[TEST] Controvento API"

    logging_level: int = logging.DEBUG

    class Config(AppSettings.Config):
        env_file: str = ".env.test"

    @computed_field
    @property
    def sqlalchemy_engine_props(self) -> dict[str, URL | bool | type[NullPool] | str]:  # pyright: ignore[reportIncompatibleMethodOverride, reportImplicitOverride]
        return dict(
            url=self.sql_db_uri,
            echo=False,
            poolclass=NullPool,
            isolation_level="AUTOCOMMIT",
        )
