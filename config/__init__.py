from config.config import Settings

settings = Settings()


def init_cfg(app):
    """Config flask"""
    app.config["SQLALCHEMY_DATABASE_URI"] = settings.get_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["API_URL"] = "http://localhost:5000"
