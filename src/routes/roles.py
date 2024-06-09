from fastapi import APIRouter, Depends, status
from fastapi_filter import FilterDepends
from sqlalchemy.orm import Session
from fastapi.responses import Response
from src.db import get_db
from src.dtos.request.error_msg import ErrorMsgDTO
from src.filters.role_filter import RoleFilter
from src.routes.base_crud import DatabaseCRUD
from fastapi_pagination import Page
from src.dtos.request.role import RoleDTO
from src.dtos.response.role import RoleResponseDTO
from src.models.roles_permissions import Role


tag = "roles"
role_router = APIRouter(
    prefix=f"/{tag}",
    tags=[tag],
    # dependencies=[Depends(oauth2_scheme)],
)


@role_router.post(
    "/",
    response_model=RoleResponseDTO,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"model": ErrorMsgDTO},
        500: {"model": ErrorMsgDTO},
    },
)
def create_role(
    role: RoleDTO, db: Session = Depends(get_db)  # noqa
) -> RoleResponseDTO:
    db_operations = DatabaseCRUD(db)
    role = db_operations.create_row(Role, role)
    return role


@role_router.get(
    "/",
    response_model=Page[RoleResponseDTO],
    response_model_exclude_none=False,
)
def get_roles(
    role_filter: RoleFilter = FilterDepends(RoleFilter),  # noqa
    db: Session = Depends(get_db),  # noqa
) -> Page[RoleResponseDTO]:  # noqa
    db_operations = DatabaseCRUD(db)
    roles = db_operations.get_all(Role, role_filter)
    return roles


@role_router.get("/{role_id}")  # noqa
def get_role(role_id: str, db: Session = Depends(get_db)):  # noqa
    """
    Get a role by id
    """
    db_operations = DatabaseCRUD(db)
    role = db_operations.get_by_id(Role, role_id)
    return role


@role_router.put("/{role_id}")
def update_role(
    role_id: str, role: RoleDTO, db: Session = Depends(get_db)  # noqa
):  # noqa
    db_operations = DatabaseCRUD(db)
    role = db_operations.update_row(Role, role_id, role)
    return role


@role_router.delete("/{role_id}")
def delete_role(role_id: str, db: Session = Depends(get_db)):  # noqa
    db_operations = DatabaseCRUD(db)
    db_operations.delete_by_id(Role, role_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
