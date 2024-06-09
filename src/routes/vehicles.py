from fastapi import APIRouter, Depends, status
from fastapi_filter import FilterDepends
from sqlalchemy.orm import Session
from fastapi.responses import Response
from src.db import get_db
from src.dtos.request.error_msg import ErrorMsgDTO
from src.filters.vehicle_filter import VehicleFilter
from src.routes.base_crud import DatabaseCRUD
from fastapi_pagination import Page
from src.dtos.request.vehicle import VehicleDTO
from src.dtos.response.vehicle import VehicleResponseDTO
from src.models.vehicle import Vehicle


tag = "vehicles"
vehicle_router = APIRouter(
    prefix=f"/{tag}",
    tags=[tag],
    # dependencies=[Depends(oauth2_scheme)],
)


@vehicle_router.post(
    "/",
    response_model=VehicleResponseDTO,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"model": ErrorMsgDTO},
        500: {"model": ErrorMsgDTO},
    },
)
def create(
    role: VehicleDTO, db: Session = Depends(get_db)  # noqa
) -> VehicleResponseDTO:
    db_operations = DatabaseCRUD(db)
    role = db_operations.create_row(Vehicle, role)
    return role


@vehicle_router.get(
    "/",
    response_model=Page[VehicleResponseDTO],
    response_model_exclude_none=False,
)
def get_all_rows(
    filter: VehicleFilter = FilterDepends(VehicleFilter),  # noqa
    db: Session = Depends(get_db),  # noqa
) -> Page[VehicleResponseDTO]:  # noqa
    db_operations = DatabaseCRUD(db)
    roles = db_operations.get_all(Vehicle, filter)
    return roles


@vehicle_router.get("/{vehicle_id}")  # noqa
def get(vehicle_id: str, db: Session = Depends(get_db)):  # noqa
    """
    Get a role by id
    """
    db_operations = DatabaseCRUD(db)
    role = db_operations.get_by_id(Vehicle, vehicle_id)
    return role


@vehicle_router.put("/{vehicle_id}")
def update(
    vehicle_id: str, role: VehicleDTO, db: Session = Depends(get_db)  # noqa
):  # noqa
    db_operations = DatabaseCRUD(db)
    role = db_operations.update_row(Vehicle, vehicle_id, role)
    return role


@vehicle_router.delete("/{vehicle_id}")
def delete(vehicle_id: str, db: Session = Depends(get_db)):  # noqa
    db_operations = DatabaseCRUD(db)
    db_operations.delete_by_id(Vehicle, vehicle_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
