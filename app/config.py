from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_NAME: str = "mockdb"
    DB_USER: str = "root"
    DB_PASSWORD: str = ""
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306

    class Config:
        env_file = ".env"


settings = Settings()
