from enum import Enum
from typing import ClassVar

from fastapi.security import OAuth2PasswordBearer
from pydantic_settings import BaseSettings, SettingsConfigDict


class ApiEnviromentEnum(str, Enum):
    development = "development"
    production = "production"


class DatabaseSettings:
    """Configuration for database connection"""

    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_HOST: str
    DATABASE_PORT: int


class Settings(BaseSettings, DatabaseSettings):
    """Configuration for the application"""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    CLIENT_ORIGIN: str
    API_ENVIRONMENT: ApiEnviromentEnum = ApiEnviromentEnum.development.value
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_HOST: str
    MAIL_PORT: int
    SECRET_KEY: str
    BACKEND_PORT: int
    BACKEND_HOST: str
    LOG_LEVEL: str = "INFO"
    TOKEN_EXPIRY: int = 12
    TOKEN_URL: str = "/auth/token"
    TOKEN_MANAGER: ClassVar[OAuth2PasswordBearer] = OAuth2PasswordBearer(
        tokenUrl=TOKEN_URL
    )


settings = Settings()
