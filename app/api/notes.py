from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api import crud_notes
from app.database import get_session

from .schemas import NoteCreateSchemas, NoteUpdateSchemas

router = APIRouter(prefix="/notes", tags=["Notes"])


@router.get("/")
async def get_lst_notes(session: AsyncSession = Depends(get_session)):
    return await crud_notes.get_all_notes(session)


@router.post("/create_note")
async def create_note(
    note_in: NoteCreateSchemas, session: AsyncSession = Depends(get_session)
):
    return await crud_notes.create_note(session, note_in.text)


@router.post('/update_note/{note_id}')
async def update_note(update_note: NoteUpdateSchemas, note_id: int, session: AsyncSession = Depends(get_session)):
    return await crud_notes.update_note(session, note_id, update_note)


@router.delete('/delete/{note_id}')
async def delete_note(note_id: int, session: AsyncSession = Depends(get_session)):
    return await crud_notes.delete_note(session, note_id)