from pydantic import BaseModel, EmailStr



class OficialDTO(BaseModel):
    email: EmailStr
    username: str
    password: str
    badge: str
