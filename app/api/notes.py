from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.api import crud_notes
from app.core.config import get_session
from .schemas import NoteCreateSchemas, NoteReadShemas


router = APIRouter(prefix="/notes", tags=["Notes"])


@router.get('/')
async def get_lst_notes(session: AsyncSession = Depends(get_session)):
    return await crud_notes.get_all_notes(session)


@router.post('/create_note')
async def create_note(session: AsyncSession = Depends(get_session), note_in: NoteCreateSchemas):
    return await crud_notes.create_note(session, note_in)