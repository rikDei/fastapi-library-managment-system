import logging
from typing import Any

from app.core.settings.base import BaseAppSettings
from version import response


class AppSettings(BaseAppSettings):
    """
    Base application settings
    """

    debug: bool = False
    title: str = response["message"]
    version: str = response["version"]
    openapi_url: str = "/openapi.json"
    docs_url: str = "/"
    redoc_url: str = "/redoc"
    openapi_prefix: str = ""

    api_prefix: str = "/api/v1"

    allowed_hosts: list[str] = ["*"]

    logging_level: int = logging.INFO

    class Config:
        validate_assignment: bool = True

    @property
    def fastapi_kwargs(self) -> dict[str, Any]:
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }
