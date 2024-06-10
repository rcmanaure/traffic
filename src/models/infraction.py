from sqlalchemy import Column, ForeignKey, String, TIMESTAMP, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from src.models.vehicle import Vehicle
from src.utils.db_utils import Constants
from .base import ModelBase, Base


class Infraction(Base, ModelBase):
    __tablename__ = "infractions"
    plate = Column(String(Constants.MAX_LENGTH), nullable=False)
    description = Column(String(Constants.MAX_LENGTH), nullable=False)
    vehicle_id = Column(UUID(as_uuid=True), ForeignKey("vehicles.id"))
    timestamp = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )

    vehicle = relationship(
        Vehicle,
        back_populates="infraction",
        lazy="joined",
    )
