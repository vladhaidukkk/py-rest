from typing import Annotated, Sequence

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import db_helper
from app.core.db.models import User
from app.core.schemas.user import UserRead
from app.crud.users import get_all_users

router = APIRouter(tags=["Users"])


@router.get("", response_model=list[UserRead])
async def get_users(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> Sequence[User]:
    return await get_all_users(session)
