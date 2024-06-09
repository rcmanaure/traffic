from typing import Optional


from src.models.vehicle import Vehicle
from fastapi_filter.contrib.sqlalchemy import Filter


class VehicleFilter(Filter):
    plate: Optional[str] = None
    model: Optional[str] = None
    brand: Optional[str] = None
    order_by: list[str] = ["created_at"]
    search: Optional[str] = None

    class Constants(Filter.Constants):
        model = Vehicle
        search_model_fields = [
            "plate",
            "model",
            "brand",
        ]
