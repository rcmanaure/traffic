import datetime
from src.config.settings import settings
import jwt


def create_token(data: dict, expires_delta: datetime.timedelta = None):
    """
    Create a token with the given data and expiry time

    :param data: dict
    :param expires_delta: datetime.timedelta

    :return: str (token)
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.now(datetime.timezone.utc) + expires_delta
    else:
        expire = datetime.datetime.now(
            datetime.timezone.utc
        ) + datetime.timedelta(seconds=1)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256")
    return encoded_jwt
