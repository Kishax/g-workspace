import boto3
from botocore.exceptions import ClientError
from sqlalchemy.orm import Session
from app.config import settings
from app.models.mail import Mail
from app.models.user import User
from app.services.ai_service import AIService

class MailService:
    def __init__(self):
        self.ses_client = boto3.client(
            'ses',
            region_name=settings.SES_REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )
    
    @staticmethod
    async def send_mail(mail_data, user: User, db: Session):
        """メール送信"""
        # スパムチェック
        spam_score = await AIService.check_spam(mail_data.body)
        if spam_score > 0.8:
            raise HTTPException(
                status_code=400,
                detail="メールがスパムとして検出されました"
            )
        
        # SES でメール送信
        try:
            service = MailService()
            response = service.ses_client.send_email(
                Source=settings.SES_FROM_EMAIL,
                Destination={'ToAddresses': [mail_data.to]},
                Message={
                    'Subject': {'Data': mail_data.subject},
                    'Body': {'Text': {'Data': mail_data.body}}
                }
            )
            
            # データベースに保存
            db_mail = Mail(
                kid=user.id,
                from_address=settings.SES_FROM_EMAIL,
                to_address=mail_data.to,
                subject=mail_data.subject,
                body=mail_data.body,
                status="sent",
                spam_score=spam_score
            )
            db.add(db_mail)
            db.commit()
            db.refresh(db_mail)
            
            return db_mail
            
        except ClientError as e:
            raise HTTPException(
                status_code=500,
                detail=f"メール送信エラー: {str(e)}"
            )
    
    @staticmethod
    async def get_mails(user: User, folder: str, page: int, limit: int, db: Session):
        """メール一覧取得"""
        # TODO: メール一覧取得実装
        pass
    
    @staticmethod
    async def get_mail(mail_id: int, user: User, db: Session):
        """メール詳細取得"""
        # TODO: メール詳細取得実装
        pass
    
    @staticmethod
    async def mark_as_read(mail_id: int, user: User, db: Session):
        """既読マーク"""
        # TODO: 既読マーク実装
        pass