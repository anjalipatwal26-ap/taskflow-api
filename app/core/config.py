import os
from dotenv import load_dotenv

load_dotenv()  # reads the .env file and loads its values into the environment

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./taskflow.db")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "change-this-secret")
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
settings = Settings()