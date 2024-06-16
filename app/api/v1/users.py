from typing import Annotated, Sequence

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import db_helper
from app.core.db.models import User
from app.core.schemas.user import UserCreate, UserRead
from app.crud import users as users_crud

router = APIRouter(tags=["Users"])


@router.get("", response_model=list[UserRead])
async def get_users(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> Sequence[User]:
    return await users_crud.get_all_users(session=session)


@router.post("", response_model=UserRead)
async def create_user(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    user_create: UserCreate,
) -> User:
    return await users_crud.create_user(session=session, user_create=user_create)
