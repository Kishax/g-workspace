import boto3
from botocore.exceptions import ClientError
from app.config import settings
import uuid


class S3Util:
  def __init__(self):
    self.s3_client = boto3.client(
      "s3",
      region_name=settings.AWS_REGION,
      aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
      aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )
    self.bucket_name = settings.AWS_S3_BUCKET

  def upload_file(self, file_obj, original_filename, content_type):
    """ファイルアップロード"""
    try:
      # ユニークなファイル名を生成
      file_extension = original_filename.split(".")[-1]
      unique_filename = f"{uuid.uuid4()}.{file_extension}"
      s3_key = f"uploads/{unique_filename}"

      self.s3_client.upload_fileobj(
        file_obj, self.bucket_name, s3_key, ExtraArgs={"ContentType": content_type}
      )

      return {
        "filename": unique_filename,
        "s3_key": s3_key,
        "url": f"https://{self.bucket_name}.s3.{settings.AWS_REGION}.amazonaws.com/{s3_key}",
      }
    except ClientError as e:
      raise Exception(f"File upload failed: {str(e)}")

  def delete_file(self, s3_key):
    """ファイル削除"""
    try:
      self.s3_client.delete_object(Bucket=self.bucket_name, Key=s3_key)
      return True
    except ClientError as e:
      raise Exception(f"File deletion failed: {str(e)}")

  def generate_presigned_url(self, s3_key, expiration=3600):
    """署名付きURL生成"""
    try:
      response = self.s3_client.generate_presigned_url(
        "get_object",
        Params={"Bucket": self.bucket_name, "Key": s3_key},
        ExpiresIn=expiration,
      )
      return response
    except ClientError as e:
      raise Exception(f"Presigned URL generation failed: {str(e)}")
