import os
from dotenv import load_dotenv
from typing import Dict, Any
from pydantic import BaseSettings, validator, ValidationError

class Settings(BaseSettings):
    # Database Configuration
    DB_HOST: str = 'localhost'
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_POOL_SIZE: int = 5
    DB_MAX_OVERFLOW: int = 10
    DB_POOL_RECYCLE: int = 3600

    # Google API Configuration
    GOOGLE_API_KEY: str
    SEARCH_ENGINE_ID: str

    # Security Configuration
    SECRET_KEY: str
    DEBUG: bool = False
    ENVIRONMENT: str = 'development'

    # Rate Limiting
    RATE_LIMIT: int = 100
    RATE_LIMIT_WINDOW: int = 60

    @validator('SECRET_KEY')
    def validate_secret_key(cls, v):
        if len(v) < 32:
            raise ValueError('SECRET_KEY must be at least 32 characters')
        return v

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

# Load and validate configuration
try:
    load_dotenv()
    settings = Settings()
except ValidationError as e:
    raise RuntimeError(f"Configuration error: {e}") from e

DB_CONFIG = {
    'host': settings.DB_HOST,
    'user': settings.DB_USER,
    'password': settings.DB_PASSWORD,
    'database': settings.DB_NAME,
    'pool_size': settings.DB_POOL_SIZE,
    'max_overflow': settings.DB_MAX_OVERFLOW,
    'pool_recycle': settings.DB_POOL_RECYCLE
}
