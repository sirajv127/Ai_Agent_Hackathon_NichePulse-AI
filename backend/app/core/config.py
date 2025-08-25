from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    GEMINI_API_KEY: str
    BACKEND_CORS_ORIGINS: List[str] = ['http://localhost:3000']

    class Config:
        env_file = ".env"

settings = Settings()