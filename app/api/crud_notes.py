from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Note

from .schemas import NoteCreateSchemas


async def get_all_notes(
    session: AsyncSession, limit_cnt: int = None, offset_cnt: int = None
):
    query = select(Note)

    if limit_cnt is not None:
        query = query.limit(limit_cnt)

    if offset_cnt is not None:
        query = query.offset(offset_cnt)

    result = await session.execute(query)

    return result.scalars().all()


async def create_note(session: AsyncSession, note_data: NoteCreateSchemas):
    new_note = Note(text=note_data)
    session.add(new_note)
    await session.commit()
    await session.refresh(new_note)
    return new_note


async def update_note(session: AsyncSession, note_id: int, new_task: str):
    query = (
        update(Note)
        .where(Note.id == note_id)
        .values(text=new_task.text, complite=new_task.complite)
    )
    await session.execute(query)
    await session.commit()
    return {"status": f"Note with {note_id} successful update."}


async def delete_note(session: AsyncSession, note_id: int):
    query = delete(Note).where(Note.id == note_id)
    await session.execute(query)
    await session.commit()
    return {"status": f"Note with {note_id} successful delete."}
