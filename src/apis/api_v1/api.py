from fastapi import APIRouter

from src.api.api_v1.endpoints import miragte_down

api_router = APIRouter()
api_router.include_router(login.router, tags=["mi"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
