from fastapi import Depends, HTTPException
from src.config.settings import settings
import jwt
from src.dtos.authentication.user import UserJwtPayload
from src.routes.authentication import TOKEN_BLACKLIST


def decode_token(token):
    """
    Decode the token and return the payload if the token is valid

    :param token: str

    :return: dict
    """
    # TODO: check if the token is in the blacklist in the database or in-memory cache
    if token in TOKEN_BLACKLIST:
        raise HTTPException(status_code=401, detail="Token has been revoked")
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Signature has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


def decode_bearer_token(
    token,
):  # noqa
    try:
        decoded_token = decode_token(token)
        return UserJwtPayload(**decoded_token)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))


def get_current_user(token: str = Depends(settings.TOKEN_MANAGER)):  # noqa
    return decode_bearer_token(token)
