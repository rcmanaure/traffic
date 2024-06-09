from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.utils.db_utils import get_sqlalchemy_database_url
from .models.base import Base

SQLALCHEMY_DATABASE_URL = get_sqlalchemy_database_url()

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(engine)
Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
