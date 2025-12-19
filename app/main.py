from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.notes import router as note_router

from .database import Base, db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

    await db_helper.engine.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(note_router)
