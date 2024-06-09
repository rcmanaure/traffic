from pydantic import BaseModel, EmailStr
from typing import Optional

from src.dtos.request.role import RoleName


class UserDTO(BaseModel):
    email: EmailStr
    username: str
    password: str
    first_name: str
    last_name: str
    address: str
    city: str
    zipcode: str
    contact_number: str
    role_id: RoleName = RoleName.GUEST


class UserUpdateDTO(BaseModel):
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    zipcode: Optional[str] = None
    contact_number: Optional[str] = None
    role_id: Optional[RoleName] = None

    class Config:
        from_attributes = True
