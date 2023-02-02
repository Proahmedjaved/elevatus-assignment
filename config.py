"""
This file is used to store the configuration of the application.

The configuration is stored in a class that inherits from the BaseSettings class
from the pydantic library.

The configuration is loaded from the .env file using pydantic BaseSettings class.
"""
from pydantic import BaseSettings


class Settings(BaseSettings):
    # The name of the application
    APP_NAME: str = "Elevatus Assignment"

    # The version of the application
    APP_VERSION: str = "0.1.0"

    MONGO_CONNECTION_STRING: str
    MONGO_DB_NAME: str

    class Config:
        env_file = ".env"


settings = Settings()
