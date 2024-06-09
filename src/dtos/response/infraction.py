from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel

from src.dtos.response.vehicle import VehicleResponseDTO


class InfractionResponseDTO(BaseModel):
    id: UUID
    plate: str
    description: str
    timestamp: datetime
    # vehicle_id: UUID
    vehicle: Optional[VehicleResponseDTO] = None

    class Config:
        from_attributes = True