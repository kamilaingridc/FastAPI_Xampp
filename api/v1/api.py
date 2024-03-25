from fastapi import APIRouter

from api.v1.endpoints import carro

api_router = APIRouter()
api_router.include_router(carro.router, prefix="/carro", tags=["carros"])

