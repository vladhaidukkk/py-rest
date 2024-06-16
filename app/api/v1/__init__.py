from fastapi import APIRouter

from app.api.v1.users import router as users_router
from app.core.config import settings

router = APIRouter()
router.include_router(users_router, prefix=settings.api.v1.users)
