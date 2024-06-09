from pydantic import BaseModel


class AuthenticationUser(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    address: str
    city: str
    zipcode: str
    contact_number: str


class UserJwtPayload(BaseModel):
    id: str
    email: str
    username: str
    is_active: bool
    role_id: str
    role_name: str
    first_name: str
    last_name: str
    zipcode: str
    contact_number: str
    city: str
