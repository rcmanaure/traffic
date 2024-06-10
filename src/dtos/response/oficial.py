from uuid import UUID
from pydantic import BaseModel


class OficialResponseDTO(BaseModel):
    id: UUID
    email: str
    username: str
    badge: str

    class Config:
        from_attributes = True
