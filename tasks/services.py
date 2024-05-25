from datetime import datetime, timezone

from sqlalchemy import delete, insert, select, update

from base.base import BaseService
from database import session
from tasks.models import Task


class TaskService(BaseService):
    model = Task

    @classmethod
    def add(cls, **data):
        """Adding new task and show it"""
        data["created_at"] = datetime.now(timezone.utc)
        data["updated_at"] = datetime.now(timezone.utc)
        query = insert(cls.model).values(**data)
        session.execute(query)
        session.commit()
        return cls.find_last()

    @classmethod
    def update(cls, model_id: int, **data):
        """Update data in task and show updated task"""
        data["updated_at"] = datetime.now(timezone.utc)

        query = update(cls.model).filter_by(id=model_id).values(**data)
        session.execute(query)
        session.commit()
        return TaskService.find_by_id(model_id=model_id)

    @classmethod
    def delete(cls, model_id):
        """Delete task"""
        query = delete(cls.model).filter_by(id=model_id)
        session.execute(query)
        session.commit()

    @classmethod
    def find_last(cls):
        """Find last add task"""
        query = select(cls.model).order_by(cls.model.id.desc()).limit(1)
        result = session.execute(query)
        session.commit()

        return result.mappings().one_or_none()

    @classmethod
    def is_valid(cls, update_flag: int, **data):
        """Validation for import task depends on "PUT" or "POST" methods"""
        invalid_data = ("id", "created_at", "updated_at")
        result = 0
        if not update_flag and "title" not in data:
            result = 1
        if update_flag and ("title" not in data and "description" not in data):
            result = 1
        for unit in data.keys():
            if unit in invalid_data:
                result = 1
        return result
