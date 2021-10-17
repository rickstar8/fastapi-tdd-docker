# project/app/api/ping.py

from fastapi import APIRouter, Depends

from app.config import Settings, get_settings

router = APIRouter()


@router.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "cheese",
        "environment": settings.environment,
        "testing": settings.testing,
    }
