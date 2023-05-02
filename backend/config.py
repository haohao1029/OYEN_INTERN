from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE: str = "database.db"

class Config:
    env_file = ".env"


settings = Settings()
