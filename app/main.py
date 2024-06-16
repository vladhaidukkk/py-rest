from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.api import router as api_router
from app.core.config import settings
from app.core.db import db_helper


@asynccontextmanager
async def lifespan(_app: FastAPI):
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
