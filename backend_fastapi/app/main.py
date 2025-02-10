from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import Settings
from app.utils.logger import logger_config

from app.api import apiRouter 

from app.db import conn
from app.data import seed_data_generator

logger = logger_config(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    conn.create_db_and_tables()
    seed_data_generator.create_seeds()
    logger.info("startup: triggered")
    yield
    logger.info("shutdown: triggered")


def create_app(settings: Settings):
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        docs_url="/",
        description=settings.DESCRIPTION,
        lifespan=lifespan,
    )

    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


    app.include_router(apiRouter)

    return app