from pydantic import BaseModel, EmailStr
from typing import Optional

from src.dtos.request.role import RoleName


class OficialDTO(BaseModel):
    email: EmailStr
    username: str
    password: str
    badge: str
    # role_id: Optional[RoleName] = RoleName.OFFICIAL
