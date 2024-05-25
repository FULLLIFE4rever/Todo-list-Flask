from datetime import datetime, timezone

from sqlalchemy.orm import Mapped

from base import db
from database import Base


class Task(Base):
    """Table in SQL"""

    __tablename__ = "task"

    id: Mapped[int] = db.mapped_column(primary_key=True)
    title: Mapped[str] = db.mapped_column(db.String(100), nullable=False)
    description: Mapped[int] = db.mapped_column(
        db.String(100), default=None, nullable=True
    )
    created_at: Mapped[datetime] = db.mapped_column(
        db.DateTime, nullable=False, default=datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = db.mapped_column(
        db.DateTime,
        nullable=False,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )

    def to_dict(self):
        """Convert to dictionary for response"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def __str__(self):
        return f"Task {self.title}:{self.description}"
