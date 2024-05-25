import pytest

from app import create_app
from base import db


@pytest.fixture(scope="module")
def client(app):
    """Cliente de teste para interagir com o aplicativo"""
    return app.test_client()


@pytest.fixture(scope="module")
def app():
    """Instance of Main flask app"""
    app = create_app()

    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados para testes
        yield app
        db.session.remove()
        db.drop_all()
