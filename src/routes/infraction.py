from fastapi import APIRouter, Depends, status
from fastapi_filter import FilterDepends
from sqlalchemy.orm import Session
from fastapi.responses import Response
from src.authentication.oauth_implementation import get_current_user
from src.db import get_db
from src.dtos.request.error_msg import ErrorMsgDTO
from src.filters.infraction_filter import InfractionFilter
from src.models.vehicle import Vehicle
from src.routes.base_crud import DatabaseCRUD
from fastapi_pagination import Page
from src.dtos.request.infraction import InfractionDTO
from src.dtos.response.infraction import InfractionResponseDTO
from src.models.infraction import Infraction

tag = "infractions"
infraction_router = APIRouter(
    prefix=f"/{tag}",
    tags=[tag],
    # dependencies=[Depends(get_current_user)],
)


@infraction_router.post(
    "/",
    response_model=InfractionResponseDTO,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"model": ErrorMsgDTO},
        500: {"model": ErrorMsgDTO},
    },
)
def create_infraction(
    infraction: InfractionDTO, db: Session = Depends(get_db)  # noqa
) -> InfractionResponseDTO:
    db_operations = DatabaseCRUD(db)
    vehicle = db_operations.get_by_field(Vehicle, "plate", infraction.plate)
    infraction = infraction.model_dump()
    infraction["vehicle_id"] = vehicle.id
    infraction = db_operations.create_row(Infraction, infraction)
    return infraction


@infraction_router.get(
    "/",
    response_model=Page[InfractionResponseDTO],
    response_model_exclude_none=False,
)
def get_infractions(
    infraction_filter: InfractionFilter = FilterDepends(InfractionFilter),  # noqa
    db: Session = Depends(get_db),  # noqa
) -> Page[InfractionResponseDTO]:
    
    db_operations = DatabaseCRUD(db)
    infractions = db_operations.get_all(Infraction, infraction_filter)
    return infractions


@infraction_router.get("/{infraction_id}")  # noqa
def get_infraction(infraction_id: str, db: Session = Depends(get_db)):
    """
    Get a infraction by id
    """
    db_operations = DatabaseCRUD(db)
    infraction = db_operations.get_by_id(Infraction, infraction_id)
    return infraction


@infraction_router.put("/{infraction_id}")
def update_infraction(
    infraction_id: str,
    infraction: InfractionDTO,
    db: Session = Depends(get_db),
) -> InfractionResponseDTO:
    db_operations = DatabaseCRUD(db)
    infraction = db_operations.update_row(Infraction, infraction_id, infraction)
    return infraction


@infraction_router.delete("/{infraction_id}")
def delete_infraction(infraction_id: str, db: Session = Depends(get_db)):
    db_operations = DatabaseCRUD(db)
    db_operations.delete_by_id(Infraction, infraction_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)