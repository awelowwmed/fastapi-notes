from datetime import datetime

from pydantic import BaseModel


class NoteCreateSchemas(BaseModel):
    text: str


class NoteReadShemas(BaseModel):
    id: int
    text: str
    datetime: datetime
    complited: bool

    class Congig:
        from_attridutes = True


class NoteUpdateSchemas(BaseModel):
    text: str 
    complite: bool