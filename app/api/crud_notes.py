from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Note

from .schemas import NoteCreateSchemas


async def get_all_notes(session: AsyncSession):
    result = await session.execute(select(Note))
    return result.scalars().all()


async def create_note(session: AsyncSession, note_data: NoteCreateSchemas):
    new_note = Note(text=note_data)
    session.add(new_note)
    await session.commit()
    await session.refresh(new_note)
    return new_note


async def update_note(session: AsyncSession, note_id: int, new_task: str):
    query = update(Note).where(Note.id == note_id).values(text=new_task.text, complite=new_task.complite)
    await session.execute(query)
    await session.commit()


async def delete_note(session: AsyncSession, note_id: int):
    query = delete(Note).where(Note.id == note_id)
    await session.execute(query)
    await session.commit()
