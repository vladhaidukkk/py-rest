from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db.models import User


async def get_all_users(session: AsyncSession) -> Sequence[User]:
    query = select(User).order_by(User.id)
    result = await session.scalars(query)
    return result.all()
