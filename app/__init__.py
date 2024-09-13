from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlmodel import SQLModel
from starlette.middleware.cors import CORSMiddleware

from app.api import api_route
from config.setting import settings
from core.db import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield
    # todo 清理操作


def create_app():
    app = FastAPI(lifespan=lifespan)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # List of allowed origins
        allow_credentials=True,
        allow_methods=["*"],  # List of allowed methods
        allow_headers=["*"],  # List of allowed headers
    )

    app.include_router(api_route, prefix=settings.API_V1_STR)

    return app
