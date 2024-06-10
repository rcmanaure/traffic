from typing import Optional
from pydantic import BaseModel


class AuthenticationUser(BaseModel):
    email: str
    username: str



class UserJwtPayload(BaseModel):
    id: str
    email: str
    username: str
    is_active: bool
    role_id: str
    role_name: str
    badge: Optional[str] = None

