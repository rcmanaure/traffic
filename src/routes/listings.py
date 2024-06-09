from typing import Dict
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db import get_db
from src.config.settings import settings

listings_router = APIRouter(prefix="/listings")


@listings_router.get("")
def get_listings(
    db: Session = Depends(get_db),  # noqa
    token: str = Depends(settings.TOKEN_MANAGER),  # noqa
) -> Dict[str, str]:
    return {"token": token}
