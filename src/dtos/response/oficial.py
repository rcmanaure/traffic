from uuid import UUID
from pydantic import BaseModel
from typing import Optional






class OficialResponseDTO(BaseModel):
    id: UUID
    email: str
    username: str    
    badge: str

    class Config:
        from_attributes = True
