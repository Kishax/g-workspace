from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.services.mail_service import MailService
from app.services.auth_service import AuthService
from app.schemas.mail import MailCreate, MailResponse, MailListResponse
from app.models.user import User

router = APIRouter()


@router.post("/send", response_model=MailResponse)
async def send_mail(
  mail: MailCreate,
  db: Session = Depends(get_db),
  current_user: User = Depends(AuthService.get_current_user),
):
  """メール送信"""
  return await MailService.send_mail(mail, current_user, db)


@router.get("/", response_model=MailListResponse)
async def get_mails(
  folder: str = Query("inbox"),
  page: int = Query(1, ge=1),
  limit: int = Query(20, ge=1, le=100),
  db: Session = Depends(get_db),
  current_user: User = Depends(AuthService.get_current_user),
):
  """メール一覧取得"""
  return await MailService.get_mails(current_user, folder, page, limit, db)


@router.get("/{mail_id}", response_model=MailResponse)
async def get_mail(
  mail_id: int,
  db: Session = Depends(get_db),
  current_user: User = Depends(AuthService.get_current_user),
):
  """メール詳細取得"""
  return await MailService.get_mail(mail_id, current_user, db)


@router.put("/{mail_id}/read")
async def mark_as_read(
  mail_id: int,
  db: Session = Depends(get_db),
  current_user: User = Depends(AuthService.get_current_user),
):
  """既読マーク"""
  return await MailService.mark_as_read(mail_id, current_user, db)
