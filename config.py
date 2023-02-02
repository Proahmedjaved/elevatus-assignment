"""
This file is used to store the configuration of the application.

The configuration is stored in a class that inherits from the BaseSettings class
from the pydantic library.

The configuration is loaded from the .env file using pydantic BaseSettings class.
"""
import secrets
from pydantic import BaseSettings


class Settings(BaseSettings):

    """
        This class is used to store the configuration of the application.

    """

    # The name of the application
    APP_NAME: str = "Elevatus Assignment"

    # The version of the application
    APP_VERSION: str = "0.1.0"

    MONGO_CONNECTION_STRING: str
    MONGO_DB_NAME: str

    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_HOURS: int = 12

    class Config:
        env_file = ".env"


settings = Settings()
