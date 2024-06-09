from pydantic import BaseModel, EmailStr
from typing import Optional

from src.dtos.request.role import RoleName


class UserDTO(BaseModel):
    email: EmailStr
    username: str
    password: str
    # role_id: RoleName = RoleName.USER


class UserUpdateDTO(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    # role_id: Optional[RoleName] = None

    class Config:
        from_attributes = True

