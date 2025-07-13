from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.server_service import ServerService
from app.services.auth_service import AuthService
from app.models.user import User

router = APIRouter()


@router.get("/")
async def get_servers(
  db: Session = Depends(get_db),
  current_user: User = Depends(AuthService.get_current_user),
):
  """サーバー一覧取得"""
  return await ServerService.get_servers(db)


@router.get("/{server_id}")
async def get_server(
  server_id: int,
  db: Session = Depends(get_db),
  current_user: User = Depends(AuthService.get_current_user),
):
  """サーバー詳細取得"""
  return await ServerService.get_server(server_id, db)


@router.post("/{server_id}/ping")
async def ping_server(
  server_id: int,
  db: Session = Depends(get_db),
  current_user: User = Depends(AuthService.get_current_user),
):
  """サーバーPing実行"""
  return await ServerService.ping_server(server_id, db)
