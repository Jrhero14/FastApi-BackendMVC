from contextlib import asynccontextmanager

from fastapi import FastAPI

from database.config import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield
