from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # データベース
    DATABASE_URL: str
    
    # Discord OAuth2
    DISCORD_CLIENT_ID: str
    DISCORD_CLIENT_SECRET: str
    DISCORD_REDIRECT_URI: str
    
    # AWS
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str
    AWS_S3_BUCKET: str
    
    # Amazon SES
    SES_REGION: str
    SES_FROM_EMAIL: str
    
    # Redis
    REDIS_URL: str
    
    # JWT
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    
    # OpenAI
    OPENAI_API_KEY: str
    
    # その他
    DEBUG: bool = False
    ALLOWED_ORIGINS: List[str] = []
    ENABLE_METRICS: bool = True
    
    class Config:
        env_file = ".env"

settings = Settings()