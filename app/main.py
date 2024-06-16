import uvicorn
from fastapi import FastAPI

from app.api import router as api_router

app = FastAPI()
app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)
