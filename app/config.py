from pydantic_settings import BaseSettings
from typing import List, Optional


class Settings(BaseSettings):
  # ===========================================
  # 必須設定（最低限必要）
  # ===========================================
  DATABASE_URL: str
  REDIS_URL: str
  JWT_SECRET_KEY: str

  # ===========================================
  # 基本設定（デフォルト値あり）
  # ===========================================
  DEBUG: bool = False
  ALLOWED_ORIGINS: List[str] = []
  ENABLE_METRICS: bool = True
  JWT_ALGORITHM: str = "HS256"
  JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440

  # ===========================================
  # 外部サービス設定（オプション）
  # ===========================================
  # Discord OAuth2（認証機能使用時のみ）
  DISCORD_CLIENT_ID: Optional[str] = None
  DISCORD_CLIENT_SECRET: Optional[str] = None
  DISCORD_REDIRECT_URI: Optional[str] = None

  # AWS（ファイル・メール機能使用時のみ）
  AWS_ACCESS_KEY_ID: Optional[str] = None
  AWS_SECRET_ACCESS_KEY: Optional[str] = None
  AWS_REGION: Optional[str] = None
  AWS_S3_BUCKET: Optional[str] = None

  # Amazon SES（メール送信機能使用時のみ）
  SES_REGION: Optional[str] = None
  SES_FROM_EMAIL: Optional[str] = None

  # OpenAI（AI機能使用時のみ）
  OPENAI_API_KEY: Optional[str] = None

  class Config:
    env_file = ".env"


settings = Settings()
