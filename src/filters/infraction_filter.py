from typing import Optional


from src.models.infraction import Infraction
from fastapi_filter.contrib.sqlalchemy import Filter


class InfractionFilter(Filter):
    plate: Optional[str] = None
    user_id: Optional[str] = None
    order_by: list[str] = ["timestamp"]
    search: Optional[str] = None

    class Constants(Filter.Constants):
        model = Infraction
        search_model_fields = [
            "plate",
        ]
