from typing import Optional
from uuid import UUID
from pydantic import BaseModel

from src.dtos.response.user import UserResponseDTO

# from src.dtos.response.user import UserResponseDTO


# class ResponseDTO(UserResponseDTO):
#     user: Optional[UserResponseDTO] = None

#     class Config:
#         from_attributes = True


class VehicleResponseDTO(BaseModel):
    id: UUID
    plate: str
    model: str
    brand: str
    # user: Optional[BasicUserResponseDTO] = None
    user: Optional[UserResponseDTO] = None

    class Config:
        from_attributes = True
