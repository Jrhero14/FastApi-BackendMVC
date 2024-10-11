from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.routes.api import router
from app.utilities.lifespan import lifespan

app = FastAPI(lifespan=lifespan)

app.include_router(router)
