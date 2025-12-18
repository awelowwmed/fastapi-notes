from pydantic import BaseModel


class NoteCreateSchemas(BaseModel):
    text: str 


class NoteReadShemas(BaseModel):
    id: int 
    text: str 

    class Congig:
        from_attridutes = True