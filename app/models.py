from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from .database import Base


class Note(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(nullable=False)
    created_at = Mapped[datetime] = mapped_column(default=datetime.utcnow)
    complited = Mapped[bool] = mapped_column(default=False)
