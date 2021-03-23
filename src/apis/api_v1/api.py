from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(professtional.router, prefix="/professtional", tags=["professtional"])
