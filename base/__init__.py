from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def init_db(app):
    """Init for connection and migrations to DataBase"""
    db.init_app(app)
    migrate.init_app(app, db)
