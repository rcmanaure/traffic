from sqlalchemy import Column, ForeignKey, String

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .base import ModelBase, Base
from src.utils.db_utils import Constants


class Role(Base, ModelBase):
    __tablename__ = "roles"
    name = Column(
        String(Constants.MAX_LENGTH_NAME),
        nullable=False,
        unique=True,
    )
    description = Column(String(Constants.MAX_LENGTH_DESCRIPTION))
    # user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    user = relationship(
        "User",
        back_populates="role",
        # lazy="joined",
    )
    permissions = relationship("Permission", back_populates="roles")


class Permission(Base, ModelBase):
    __tablename__ = "permissions"
    name = Column(
        String(Constants.MAX_LENGTH_NAME), unique=True, nullable=False
    )
    description = Column(String(Constants.MAX_LENGTH_DESCRIPTION))
    role_id = Column(UUID(as_uuid=True), ForeignKey("roles.id"))
    roles = relationship("Role", back_populates="permissions")
