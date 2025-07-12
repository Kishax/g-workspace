import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_mails_unauthorized():
    """未認証でのメール取得テスト"""
    response = client.get("/api/mails/")
    assert response.status_code == 401

def test_send_mail_unauthorized():
    """未認証でのメール送信テスト"""
    response = client.post("/api/mails/send", json={
        "to": "test@example.com",
        "subject": "テスト",
        "body": "テストメール"
    })
    assert response.status_code == 401