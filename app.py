from flask import Flask

from base import init_db
from config import init_cfg
from tasks.routers import tasks_route


def create_app():
    app = Flask(__name__)
    init_cfg(app)
    init_db(app)
    app.register_blueprint(tasks_route)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
