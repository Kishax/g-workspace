import openai
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import os
from app.config import settings


class AIService:
  def __init__(self):
    openai.api_key = settings.OPENAI_API_KEY
    self.load_spam_model()

  def load_spam_model(self):
    """スパム検出モデルの読み込み"""
    model_path = "models/spam_model.pkl"
    if os.path.exists(model_path):
      with open(model_path, "rb") as f:
        self.spam_model = pickle.load(f)
    else:
      # 初期モデルの作成
      self.train_initial_model()

  @staticmethod
  async def check_spam(text: str) -> float:
    """スパム検出"""
    # OpenAI API を使用した高度な分析
    try:
      response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
          {
            "role": "system",
            "content": "You are a spam detection system. Analyze the email content and return a spam score between 0 and 1.",
          },
          {"role": "user", "content": f"Analyze this email: {text}"},
        ],
        max_tokens=50,
      )

      # スコアを抽出（簡略化）
      score_text = response.choices[0].message.content
      # 実際の実装では正規表現などでスコアを抽出
      return 0.1  # プレースホルダー

    except Exception as e:
      # フォールバック: 従来の機械学習モデル
      return AIService.check_spam_with_ml(text)

  @staticmethod
  def check_spam_with_ml(text: str) -> float:
    """機械学習モデルによるスパム検出"""
    # scikit-learn を使用した分類
    # 実装の詳細は省略
    return 0.1
