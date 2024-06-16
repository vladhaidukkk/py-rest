from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db.models import User
from app.core.schemas.user import UserCreate


async def get_all_users(session: AsyncSession) -> Sequence[User]:
    query = select(User).order_by(User.id)
    result = await session.scalars(query)
    return result.all()


async def create_user(session: AsyncSession, user_create: UserCreate) -> User:
    user = User(
        username=user_create.username,
        password=user_create.password.get_secret_value(),
    )
    session.add(user)
    await session.commit()
    return user
