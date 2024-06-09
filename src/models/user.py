from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from src.models.follows import Follow
from src.models.roles_permissions import Role
from src.utils.db_utils import Constants
from sqlalchemy.dialects.postgresql import UUID
from .base import ModelBase, Base


class User(Base, ModelBase):
    __tablename__ = "users"
    username = Column(String(Constants.MAX_LENGTH_USERNAME), unique=True)
    email = Column(
        String(Constants.MAX_LENGTH_EMAIL),
        unique=True,
        nullable=True,
    )
    password = Column(String(Constants.MAX_LENGTH_PASSWORD), nullable=False)
    address = Column(String(Constants.MAX_LENGTH_ADDRESS), nullable=False)
    city = Column(String(50), nullable=False)
    first_name = Column(String(Constants.MAX_LENGTH_NAME), nullable=False)
    last_name = Column(String(Constants.MAX_LENGTH_LASTNAME), nullable=False)
    zipcode = Column(String(5), nullable=False)
    contact_number = Column(String(Constants.MAX_LENGTH_PHONE), nullable=False)
    role_id = Column(UUID(as_uuid=True), ForeignKey("roles.id"))
    is_active = Column(Boolean, default=True)

    # One-to-many relationship with the role table
    role = relationship(
        Role,
        back_populates="user",
        lazy="joined",
    )
    # One-to-many relationship with the follows table
    follower = relationship(
        Follow,
        foreign_keys=Follow.follower_id,
        back_populates="follower_user",
    )
    followee = relationship(
        Follow,
        foreign_keys=Follow.followee_id,
        back_populates="followee_user",
    )
