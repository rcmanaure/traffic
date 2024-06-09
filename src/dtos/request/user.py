from pydantic import BaseModel, EmailStr
from typing import Optional

from src.dtos.request.role import RoleName


class UserDTO(BaseModel):
    email: EmailStr
    name: str
    password: str
    role_id: RoleName = RoleName.USER
    # vehicle_id: Optional[str] = None


class UserUpdateDTO(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = None 
    role_id: Optional[RoleName] = None

    class Config:
        from_attributes = True
