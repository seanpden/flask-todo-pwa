from flaskdemo.models.Base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean


class Todo(Base):
    __tablename__ = "todo"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    assignee: Mapped[str] = mapped_column(String(50))
    status: Mapped[bool] = mapped_column(Boolean())

    def __repr__(self) -> str:
        return f"Todo(id=({self.id!r}, title={self.title!r}, assignee={self.assignee!r}, status={self.status!r}))"
