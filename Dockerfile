FROM python:3.11-slim

# 作業ディレクトリ
WORKDIR /app

# Python の依存関係のみ（システム依存関係をスキップ）
COPY requirements.txt .

# psycopg2-binaryを使用してコンパイル不要にする
RUN sed -i 's/psycopg2-binary/psycopg2-binary/g' requirements.txt && \
    pip install --no-cache-dir --index-url https://pypi.org/simple/ -r requirements.txt || \
    pip install --no-cache-dir -r requirements.txt

# アプリケーションコード
COPY ./app /app

# 実行
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]