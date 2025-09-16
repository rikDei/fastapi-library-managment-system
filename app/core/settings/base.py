from enum import StrEnum

from pydantic import Field
from pydantic.fields import computed_field
from pydantic_settings import BaseSettings
from sqlalchemy.engine.url import URL


class AppEnvTypes(StrEnum):
    """
    Available application environments.
    """

    production = "prod"
    development = "dev"
    testing = "test"


class BaseAppSettings(BaseSettings):
    app_env: AppEnvTypes = Field(default=AppEnvTypes.production)

    postgres_host: str = Field(default="localhost")
    postgres_port: int = Field(default=5432)
    postgres_user: str = Field(default="postgres")
    postgres_password: str = Field(default="postgres")
    postgres_db: str = Field(default="postgres")

    jwt_secret_key: str = Field(default="1234")
    jwt_token_expiration_minutes: int = 60 * 24 * 7  # one week.
    jwt_algorithm: str = "HS256"

    model_config = {  # pyright: ignore[reportUnannotatedClassAttribute]
        "extra": "ignore",
        "env_file": ".env",
    }

    @computed_field
    @property
    def sql_db_uri(self) -> URL:
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.postgres_user,
            password=self.postgres_password,
            host=self.postgres_host,
            port=self.postgres_port,
            database=self.postgres_db,
        )

    @computed_field
    @property
    def sqlalchemy_engine_props(self) -> dict[str, URL]:
        return dict(url=self.sql_db_uri)
