from sqlalchemy import delete, insert, select

from database import session


class BaseService:
    """Стандартные запросы к Базе данных"""

    model = None

    @classmethod
    def find_by_id(cls, model_id: int):
        """Find model by id"""
        query = select(cls.model.__table__.columns).filter_by(id=model_id)
        result = session.execute(query)
        return result.mappings().one_or_none()

    @classmethod
    def find_all(cls, *filters):
        """Select all from table"""
        query = select(cls.model.__table__.columns).filter(*filters)
        result = session.execute(query)
        return result.mappings().all()

    @classmethod
    def add(cls, **data):
        """Add to table new row"""
        query = insert(cls.model).values(**data).returning(cls.model)
        result = session.execute(query)
        session.commit()
        return result

    @classmethod
    def delete(cls, **filter_by):
        """Remove by parametrs"""
        query = delete(cls.model).filter_by(**filter_by)
        session.execute(query)
        session.commit()
