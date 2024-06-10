from pydantic import BaseModel


class InfractionDTO(BaseModel):
    plate: str
    description: str
