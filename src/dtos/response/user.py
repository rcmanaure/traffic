from uuid import UUID
from pydantic import BaseModel
from typing import Optional

# from src.dtos.response.vehicle import VehicleResponseDTO


from .role import RoleResponseDTO


class UserResponseDTO(BaseModel):
    id: UUID
    email: str
    username: str
    username: str
    role: Optional[RoleResponseDTO] = None

    class Config:
        from_attributes = True
