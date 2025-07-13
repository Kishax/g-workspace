from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer
from prometheus_fastapi_instrumentator import Instrumentator

from app.api import auth, mails, files, servers
from app.database import engine, Base
from app.config import settings

# FastAPI アプリケーション
app = FastAPI(
  title="Kishax G Project API",
  description="Google Workspace Alternative System",
  version="1.0.0",
  docs_url="/docs" if settings.DEBUG else None,
  redoc_url="/redoc" if settings.DEBUG else None,
)

# CORS設定
app.add_middleware(
  CORSMiddleware,
  allow_origins=settings.ALLOWED_ORIGINS,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# Prometheus メトリクス
if settings.ENABLE_METRICS:
  Instrumentator().instrument(app).expose(app)

# データベース初期化
Base.metadata.create_all(bind=engine)

# ルーター登録
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(mails.router, prefix="/api/mails", tags=["mails"])
app.include_router(files.router, prefix="/api/files", tags=["files"])
app.include_router(servers.router, prefix="/api/servers", tags=["servers"])
