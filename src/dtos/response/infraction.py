from uuid import UUID
from pydantic import BaseModel


class InfractionResponseDTO(BaseModel):
    id: UUID
    plate: str
    description: str
    timestamp: str
    vehicle_id: UUID

    class Config:
        from_attributes = True