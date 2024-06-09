from pydantic import BaseModel

from enum import Enum


class RoleName(str, Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"
    CUSTOMER = "customer"
    CLEANER = "cleaner"


class RoleDTO(BaseModel):
    name: RoleName
    description: str
    # permissions: list[str]
    # user_id: str
