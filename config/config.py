from functools import cached_property
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    """Настроки Enviroment(Окружения)"""

    MYSQL_PASSWORD: str
    MYSQL_USER: str
    MYSQL_PORT: int

    DB_HOST: str
    DB_NAME: str

    TEST_MODE: bool = False

    @cached_property
    def get_url(self):
        url = (
            f"mysql+mysqlconnector://{self.MYSQL_USER}:"
            f"{self.MYSQL_PASSWORD}@{self.DB_HOST}:"
            f"{self.MYSQL_PORT}/{self.DB_NAME}"
        )
        return url

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
