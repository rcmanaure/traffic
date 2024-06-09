from typing import Optional


from src.models.roles_permissions import Role
from fastapi_filter.contrib.sqlalchemy import Filter


class RoleFilter(Filter):
    name: Optional[str] = None
    order_by: list[str] = ["created_at"]
    search: Optional[str] = None

    class Constants(Filter.Constants):
        model = Role
        search_model_fields = [
            "name",
        ]
