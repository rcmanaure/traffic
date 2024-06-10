from typing import Optional  # noqa
from uuid import UUID
from pydantic import BaseModel

from src.dtos.response.user import UserResponseDTO  # noqa


class VehicleResponseDTO(BaseModel):
    id: UUID
    plate: str
    model: str
    brand: str
    # user: Optional[UserResponseDTO] = None

    class Config:
        from_attributes = True
