FROM python:3.11-slim

# 作業ディレクトリ
WORKDIR /app

# システムの依存関係
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Python の依存関係
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコード
COPY ./app /app

# 実行
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]