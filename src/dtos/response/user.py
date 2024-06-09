from uuid import UUID
from pydantic import BaseModel
from typing import Optional

# from src.dtos.response.vehicle import VehicleResponseDTO


from .role import RoleResponseDTO


class UserResponseDTO(BaseModel):
    id: UUID
    email: str    
    name: str
    name: str
    role: Optional[RoleResponseDTO] = None
    # vehicle: Optional[VehicleResponseDTO] = None

    class Config:
        from_attributes = True
