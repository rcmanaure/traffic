from typing import Optional

from fastapi import Query  # noqa
from pydantic import Field  # noqa

from fastapi_filter import FilterDepends, with_prefix  # noqa
from fastapi_filter.contrib.sqlalchemy import Filter

from src.models.user import User


class UserFilter(Filter):
    email: Optional[str] = None
    username: Optional[str] = None
    username__ilike: Optional[str] = None
    username__like: Optional[str] = None
    username__neq: Optional[str] = None
    # TODO: create a location model to handle city, address, etc.
    # city: Optional[str] = None
    # address: Optional[AddressFilter] = FilterDepends(with_prefix("address", AddressFilter))
    # age__lt: Optional[int] = None
    # age__gte: int = Field(Query(description="this is a nice description"))
    """Required field with a custom description.

    See: https://github.com/tiangolo/fastapi/issues/4700 for why we need to wrap `Query` in `Field`.
    """
    order_by: list[str] = ["created_at"]
    search: Optional[str] = None

    class Constants(Filter.Constants):
        model = User
        search_model_fields = [
            "username",
            "city",
        ]
