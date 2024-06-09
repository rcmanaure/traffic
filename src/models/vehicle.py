from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import UUID


from src.utils.db_utils import Constants
from .base import ModelBase, Base


class Vehicle(Base, ModelBase):
    __tablename__ = "vehicles"
    plate = Column(String(Constants.MAX_LENGTH), unique=True)
    model = Column(String(Constants.MAX_LENGTH))
    brand = Column(String(Constants.MAX_LENGTH))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    user = relationship(
        "User",
        back_populates="vehicle",    
        lazy="joined",    
    )

