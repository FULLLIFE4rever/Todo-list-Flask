from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class STaskInfo(BaseModel):
    """Schema for task"""

    id: Optional[int]
    title: str
    description: str | None = None
    created_at: datetime
    updated_at: datetime


class STasksInfo(BaseModel):
    """Schema for list all tasks"""

    tasks: list[STaskInfo]
