from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import settings

engine = create_engine(settings.get_url)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


class Base(DeclarativeBase):
    """Alembic/Alcheemy Base class"""

    pass
