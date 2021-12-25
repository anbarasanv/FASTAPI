from pydantic import BaseSettings

# from dotenv import load_dotenv

# loading environment variables from the .env file
# load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"


settings = Settings()
