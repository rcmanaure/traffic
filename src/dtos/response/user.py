from uuid import UUID
from pydantic import BaseModel
from typing import Optional


from .role import RoleResponseDTO


class UserResponseDTO(BaseModel):
    id: UUID
    email: str
    first_name: str
    last_name: str
    username: str
    address: str
    city: str
    zipcode: str
    contact_number: str
    role: Optional[RoleResponseDTO] = None

    class Config:
        from_attributes = True
