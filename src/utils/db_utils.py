from pydantic import PostgresDsn

from src.config.settings import settings


def get_sqlalchemy_database_url() -> str:
    """Get the SQLAlchemy database URL.

    Returns:
        str: The SQLAlchemy database URL.

    """

    database_uri = str(
        PostgresDsn.build(
            scheme="postgresql",
            username=settings.DATABASE_USER,
            password=settings.DATABASE_PASSWORD,
            host=settings.DATABASE_HOST,
            port=int(settings.DATABASE_PORT),
            path=settings.DATABASE_NAME,
        )
    )

    return database_uri


class Constants:
    """Constants for the DB models"""

    MAX_LENGTH: int = 125
    MIN_LENGTH: int = 50
    MAX_LENGTH_DESCRIPTION: int = 1000
    MAX_LENGTH_URL: int = 500
    MAX_LENGTH_PHONE: int = 15
    MAX_LENGTH_EMAIL: int = 255
    MAX_LENGTH_USERNAME: int = 50
    MAX_LENGTH_PASSWORD: int = 255
    MAX_LENGTH_TITLE: int = 50
    MAX_LENGTH_TEXT: int = 500
    MAX_LENGTH_NAME: int = 50
    MAX_LENGTH_LASTNAME: int = 50
    MAX_LENGTH_ADDRESS: int = 255
    CLEANER_ROLE_NAME: str = "Cleaner"
    CUSTOMER_ROLE_NAME: str = "Customer"
