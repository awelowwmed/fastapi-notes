from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from contextlib import asynccontextmanager

from .database import db_helper, Base
from .models import Note
from .schemas import NoteCreate, NoteRead


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

    await db_helper.engine.dispose()


app = FastAPI(lifespan=lifespan)


@app.post("/notes", response_model=NoteRead)
async def create_note(
    note_in: NoteCreate, session: AsyncSession = Depends(db_helper.get_db_session)
):
    # Превращаем схему Pydantic в модель SQLAlchemy
    new_note = Note(**note_in.model_dump())
    session.add(new_note)
    await session.commit()  # Сохраняем в базу
    await session.refresh(new_note)  # Получаем созданный ID
    return new_note


# 3. Ручка получения всех заметок (GET)
@app.get("/notes", response_model=list[NoteRead])
async def get_notes(session: AsyncSession = Depends(db_helper.get_db_session)):
    # Делаем асинхронный запрос SELECT
    stmt = select(Note).order_by(Note.id)
    result = await session.execute(stmt)
    return result.scalars().all()
