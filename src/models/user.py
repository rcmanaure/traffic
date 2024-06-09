from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.orm import relationship


from src.models.roles_permissions import Role
from src.models.vehicle import Vehicle
from src.utils.db_utils import Constants
from sqlalchemy.dialects.postgresql import UUID
from .base import ModelBase, Base


class User(Base, ModelBase):
    __tablename__ = "users"
    username = Column(String(Constants.MAX_LENGTH_USERNAME), unique=True)
    email = Column(
        String(Constants.MAX_LENGTH_EMAIL),
        unique=True,
    )
    password = Column(String(Constants.MAX_LENGTH_PASSWORD), nullable=False)
    role_id = Column(UUID(as_uuid=True), ForeignKey("roles.id"))
    is_active = Column(Boolean, default=True)
    badge = Column(String(Constants.MAX_LENGTH), unique=True, nullable=True)

    role = relationship(
        Role,
        back_populates="user",
        lazy="joined",
    )

    vehicle = relationship(
        Vehicle,
        back_populates="user",   
        lazy="joined",     
    )
