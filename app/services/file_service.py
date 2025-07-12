import boto3
from botocore.exceptions import ClientError
from sqlalchemy.orm import Session
from fastapi import UploadFile
from app.config import settings
from app.models.file import File
from app.models.user import User

class FileService:
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            region_name=settings.AWS_REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )
    
    @staticmethod
    async def upload_file(file: UploadFile, user: User, db: Session):
        """ファイルアップロード"""
        # TODO: S3アップロード実装
        pass
    
    @staticmethod
    async def get_files(user: User, db: Session):
        """ファイル一覧取得"""
        # TODO: ファイル一覧取得実装
        pass
    
    @staticmethod
    async def download_file(file_id: int, user: User, db: Session):
        """ファイルダウンロード"""
        # TODO: ファイルダウンロード実装
        pass
    
    @staticmethod
    async def delete_file(file_id: int, user: User, db: Session):
        """ファイル削除"""
        # TODO: ファイル削除実装
        pass