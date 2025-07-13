from celery import Celery
from app.utils.email import EmailUtil
from app.config import settings

celery_app = Celery(
  "email_tasks", broker=settings.REDIS_URL, backend=settings.REDIS_URL
)


@celery_app.task
def send_email_task(to_addresses, subject, body, html_body=None):
  """非同期メール送信タスク"""
  email_util = EmailUtil()
  return email_util.send_email(to_addresses, subject, body, html_body)


@celery_app.task
def send_bulk_email_task(recipients, subject, body, html_body=None):
  """一括メール送信タスク"""
  email_util = EmailUtil()
  results = []

  for recipient in recipients:
    try:
      result = email_util.send_email([recipient], subject, body, html_body)
      results.append({"recipient": recipient, "status": "sent", "result": result})
    except Exception as e:
      results.append({"recipient": recipient, "status": "failed", "error": str(e)})

  return results
