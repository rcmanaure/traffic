from src.utils.db_utils import Constants
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, String, Integer

from .base import ModelBase, Base


class Listing(Base, ModelBase):
    __tablename__ = "listings"
    title = Column(String(Constants.MAX_LENGTH_TITLE), nullable=False)
    body = Column(String, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    status = Column(String(Constants.MAX_LENGTH), nullable=False)
    address = Column(String(Constants.MAX_LENGTH_ADDRESS), nullable=False)
    room_size = Column(Integer, nullable=False)
