from fastapi import APIRouter, Depends, status
from fastapi_filter import FilterDepends
from sqlalchemy.orm import Session
from src.authentication.oauth_implementation import (
    get_current_user,
)
from src.db import get_db
from src.dtos.request.error_msg import ErrorMsgDTO
from src.filters.user_filter import UserFilter
from src.models.roles_permissions import Role
from src.models.user import User
from src.dtos.authentication.user import UserJwtPayload
from src.dtos.request.user import UserDTO, UserUpdateDTO
from src.dtos.response.user import UserResponseDTO
from src.routes.base_crud import DatabaseCRUD
from fastapi_pagination import Page
from fastapi.responses import Response
from src.authentication.validators import get_password_hash

tag = "users"
user_router = APIRouter(prefix=f"/{tag}", tags=[tag])


@user_router.post(
    "/",
    response_model=UserResponseDTO,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"model": ErrorMsgDTO},
        500: {"model": ErrorMsgDTO},
    },
)
def create_user(
    user: UserDTO, db: Session = Depends(get_db)  # noqa
) -> UserResponseDTO:
    db_operations = DatabaseCRUD(db)
    role = db_operations.get_by_field(Role, "name", user.role_id.value)
    user.role_id = role.id
    user.password = get_password_hash(user.password)
    user = db_operations.create_row(User, user)
    return user


@user_router.get(
    "/",
    response_model_exclude_none=False,
)
def get_users(
    user_filter: UserFilter = FilterDepends(UserFilter),  # noqa
    db: Session = Depends(get_db),  # noqa
) -> Page[UserResponseDTO]:  # noqa
    db_operations = DatabaseCRUD(db)
    users = db_operations.get_all(User, user_filter)
    return users


@user_router.get("/me")
def get_user_me(
    current_user: UserJwtPayload = Depends(get_current_user),  # noqa
):  # noqa
    return current_user


@user_router.get("/{user_id}")  # noqa
def get_user(user_id: str, db: Session = Depends(get_db)):  # noqa
    """
    Get a user by id
    """
    db_operations = DatabaseCRUD(db)
    user = db_operations.get_by_id(User, user_id)
    return user


@user_router.put(
    "/{user_id}",
    response_model=UserResponseDTO,
)
def update_user(
    user: UserUpdateDTO,
    user_id: str,
    db: Session = Depends(get_db),  # noqa
):  # noqa
    """
    Update a user by id
    """
    db_operations = DatabaseCRUD(db)
    user = db_operations.update_row(User, user_id, user)
    return user


@user_router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_user(user_id: str, db: Session = Depends(get_db)):  # noqa
    """
    Delete a user by id
    """
    db_operations = DatabaseCRUD(db)
    db_operations.delete_by_id(User, user_id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
