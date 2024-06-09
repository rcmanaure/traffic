from uuid import UUID
from pydantic import BaseModel
from typing import Optional




from .role import RoleResponseDTO

class VehicleResponseDTOV2(BaseModel):
    id: UUID
    plate: str
    model: str
    brand: str

class UserResponseDTO(BaseModel):
    id: UUID
    email: str
    username: str
    # role: Optional[RoleResponseDTO] = None
    vehicle: Optional[list[VehicleResponseDTOV2]] = None

    class Config:
        from_attributes = True
