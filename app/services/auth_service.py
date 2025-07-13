from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import get_db
from app.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class AuthService:
  @staticmethod
  def get_discord_login_url():
    """Discord OAuth2 ログイン URL を生成"""
    discord_url = f"https://discord.com/api/oauth2/authorize"
    params = {
      "client_id": settings.DISCORD_CLIENT_ID,
      "redirect_uri": settings.DISCORD_REDIRECT_URI,
      "response_type": "code",
      "scope": "identify email",
    }
    return {
      "login_url": discord_url + "?" + "&".join([f"{k}={v}" for k, v in params.items()])
    }

  @staticmethod
  async def handle_discord_callback(code: str, db: Session):
    """Discord OAuth2 コールバック処理"""
    # TODO: Discord APIとの連携実装
    pass

  @staticmethod
  async def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
  ):
    """現在のユーザーを取得"""
    # TODO: JWT トークン検証実装
    pass
