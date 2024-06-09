from pydantic import BaseModel



class VehicleDTO(BaseModel):
    plate: str
    model: str
    brand: str
    user_id: str

