from celery import Celery
from app.services.ai_service import AIService
from app.config import settings

celery_app = Celery("ai_tasks", broker=settings.REDIS_URL, backend=settings.REDIS_URL)


@celery_app.task
def spam_check_task(text):
  """非同期スパムチェックタスク"""
  return AIService.check_spam_with_ml(text)


@celery_app.task
def analyze_email_sentiment_task(text):
  """メール感情分析タスク"""
  # TODO: 感情分析実装
  return {"sentiment": "neutral", "confidence": 0.5}


@celery_app.task
def generate_email_summary_task(text):
  """メール要約生成タスク"""
  # TODO: 要約生成実装
  return {"summary": "メールの要約", "keywords": ["重要", "確認"]}
