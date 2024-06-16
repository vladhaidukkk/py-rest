from contextlib import asynccontextmanager
from typing import AsyncGenerator

import uvicorn
from fastapi import FastAPI

from app.api import router as api_router
from app.core.config import settings
from app.core.db import db_helper
from app.core.db.models import Base


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, None]:
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await db_helper.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router, prefix=settings.api.prefix)

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=settings.run.reload,
    )
