from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Base"

settings = Settings()
