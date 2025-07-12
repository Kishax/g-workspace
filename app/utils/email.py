import boto3
from botocore.exceptions import ClientError
from app.config import settings

class EmailUtil:
    def __init__(self):
        self.ses_client = boto3.client(
            'ses',
            region_name=settings.SES_REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )
    
    def send_email(self, to_addresses, subject, body, html_body=None):
        """メール送信"""
        try:
            message = {
                'Subject': {'Data': subject, 'Charset': 'UTF-8'},
                'Body': {'Text': {'Data': body, 'Charset': 'UTF-8'}}
            }
            
            if html_body:
                message['Body']['Html'] = {'Data': html_body, 'Charset': 'UTF-8'}
            
            response = self.ses_client.send_email(
                Source=settings.SES_FROM_EMAIL,
                Destination={'ToAddresses': to_addresses},
                Message=message
            )
            return response
        except ClientError as e:
            raise Exception(f"Email sending failed: {str(e)}")
    
    def verify_email_identity(self, email):
        """メールアドレス認証"""
        try:
            response = self.ses_client.verify_email_identity(EmailAddress=email)
            return response
        except ClientError as e:
            raise Exception(f"Email verification failed: {str(e)}")