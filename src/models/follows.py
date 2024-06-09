from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.types import String


from .base import ModelBase, Base


class Follow(Base, ModelBase):
    __tablename__ = "follows"
    follower_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    followee_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    follower_user = relationship(
        "User", back_populates="follower", foreign_keys=[follower_id]
    )
    followee_user = relationship(
        "User", back_populates="followee", foreign_keys=[followee_id]
    )
    status = Column(String(12))

    __table_args__ = (
        UniqueConstraint("follower_id", "followee_id", name="unique_follows"),
    )
