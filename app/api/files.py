from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.file_service import FileService
from app.services.auth_service import AuthService
from app.schemas.file import FileResponse
from app.models.user import User

router = APIRouter()

@router.post("/upload", response_model=FileResponse)
async def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user)
):
    """ファイルアップロード"""
    return await FileService.upload_file(file, current_user, db)

@router.get("/", response_model=list[FileResponse])
async def get_files(
    db: Session = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user)
):
    """ファイル一覧取得"""
    return await FileService.get_files(current_user, db)

@router.get("/{file_id}")
async def download_file(
    file_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user)
):
    """ファイルダウンロード"""
    return await FileService.download_file(file_id, current_user, db)

@router.delete("/{file_id}")
async def delete_file(
    file_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user)
):
    """ファイル削除"""
    return await FileService.delete_file(file_id, current_user, db)