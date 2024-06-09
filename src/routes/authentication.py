from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.authentication import create_token
from src.db import get_db
from src.dtos.authentication.user import UserJwtPayload
from src.models.user import User
from src.config.settings import settings
from src.authentication.validators import verify_password


authentication_router = APIRouter(prefix=settings.TOKEN_URL, tags=["login"])


@authentication_router.post("")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),  # noqa
    db: Session = Depends(get_db),  # noqa
):  # noqa
    try:
        user = db.query(User).filter_by(username=form_data.username).first()
        if not user:
            # you can return any response or error of your choice
            raise HTTPException(status_code=404, detail="User not found")
        elif verify_password(form_data.password, user.password) is False:
            raise HTTPException(status_code=400, detail="Invalid password") 
        elif user.is_active is False:
            raise HTTPException(status_code=400, detail="User is not active")

    except SQLAlchemyError as error:
        raise error

    data = UserJwtPayload(
        id=str(user.id),
        email=user.email,
        username=user.username,
        is_active=user.is_active,
        role_id=str(user.role_id),
        role_name=user.role.name,
        first_name=user.first_name,
        last_name=user.last_name,
        zipcode=user.zipcode,
        contact_number=user.contact_number,
        city=user.city,
    ).model_dump()

    access_token = create_token(data, timedelta(hours=settings.TOKEN_EXPIRY))

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


# TODO: save the token in the database or in-memory cache to blacklist it
TOKEN_BLACKLIST = set()


@authentication_router.post("/logout")
def user_logout(Authorization: str = Depends(settings.TOKEN_MANAGER)):  # noqa
    TOKEN_BLACKLIST.add(Authorization)

    return {"message": "Token revoked", "token": Authorization}
