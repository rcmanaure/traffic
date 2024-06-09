from pydantic import BaseModel


class InfractionDTO(BaseModel):
    plate: str    
    description: str
    user_id: str
