from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.auth_service import AuthService
from app.schemas.user import UserResponse, TokenResponse
from app.models.user import User

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/discord/login")
async def discord_login():
  """Discord OAuth2 ログイン URL を生成"""
  return AuthService.get_discord_login_url()


@router.get("/discord/callback")
async def discord_callback(code: str, db: Session = Depends(get_db)):
  """Discord OAuth2 コールバック処理"""
  return await AuthService.handle_discord_callback(code, db)


@router.get("/me", response_model=UserResponse)
async def get_current_user(current_user: User = Depends(AuthService.get_current_user)):
  """現在のユーザー情報を取得"""
  return current_user


@router.post("/logout")
async def logout(current_user: User = Depends(AuthService.get_current_user)):
  """ログアウト"""
  return {"message": "Successfully logged out"}
