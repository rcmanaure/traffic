from fastapi import FastAPI

from src.routes.users import user_router
from src.routes.listings import listings_router
from src.routes.authentication import authentication_router
from src.utils.init_logger import setup_logger
from fastapi_pagination import add_pagination
from src.routes.roles import role_router

setup_logger()
app = FastAPI(
    title="FastAPI Documentation",
    description="API Documentation for FastAPI",
    version="0.1",
    swagger_ui_parameters={
        "filter": True,
        "tagsSorter": "alpha",
        "docExpansion": "none",
    },
)

add_pagination(app)

app.include_router(user_router)
app.include_router(listings_router)
app.include_router(authentication_router)
app.include_router(role_router)
