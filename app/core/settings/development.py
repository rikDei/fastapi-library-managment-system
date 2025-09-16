from sqlalchemy.engine.url import URL


import logging

from pydantic import computed_field

from app.core.settings.app import AppSettings


class DevAppSettings(AppSettings):
    """
    Development application settings.
    """

    debug: bool = True

    title: str = "[DEV] Controvento API"

    logging_level: int = logging.DEBUG

    class Config(AppSettings.Config):
        env_file: str = ".env.dev"

    @computed_field
    @property
    def sqlalchemy_engine_props(self) -> dict[str, URL | bool]:  # pyright: ignore[reportIncompatibleMethodOverride, reportImplicitOverride]
        return dict(url=self.sql_db_uri, echo=True)
