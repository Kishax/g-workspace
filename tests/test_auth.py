import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_discord_login():
    """Discord ログイン URL 生成テスト"""
    response = client.get("/api/auth/discord/login")
    assert response.status_code == 200
    assert "login_url" in response.json()

def test_get_current_user_unauthorized():
    """未認証ユーザーテスト"""
    response = client.get("/api/auth/me")
    assert response.status_code == 401