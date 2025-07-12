# Kishax G Project - フルスタックPython

Google Workspace代替システムのフルスタックPython実装

## 📋 プロジェクト概要

フルスタックPythonアーキテクチャを採用し、Web・モバイル・デスクトップすべてをPythonで統一開発できるGoogle Workspace代替システムです。

## 🚀 実装されたプロジェクトベースでできること

### 📁 **構造化されたプロジェクト**
- モジュール化されたPythonアプリケーション構造
- FastAPI、Streamlit、Fletの3つのアプリケーション層

### 🛠️ **開発環境**
- `docker-compose up` でフルスタック環境を一発起動
- PostgreSQL + Redis + Celery の完全なバックエンド
- 本格的なプロダクション構成

### 🌐 **3つのフロントエンド**
1. **FastAPI**: RESTful APIサーバー (ポート8000)
2. **Streamlit**: Web管理画面 (ポート8501)  
3. **Flet**: デスクトップ/モバイルアプリ

### 📧 **Google Workspaceライクな機能**
- メール送受信システム（Amazon SES統合）
- ファイル管理システム（AWS S3統合）
- ユーザー認証（Discord OAuth2）
- サーバー監視機能

### 🤖 **AI/ML統合**
- OpenAI APIによるスパム検出
- scikit-learnによる機械学習
- 非同期AI処理（Celery）

### ⚡ **すぐに始められること**
```bash
# 環境変数設定後
docker-compose up -d

# または個別起動
pip install -r requirements.txt
uvicorn app.main:app --reload
streamlit run streamlit_app/main.py
python flet_app/main.py
```

**次に実装するなら**: 認証機能、メール送信、ファイルアップロード等の具体的な機能実装ができます。

## 📁 プロジェクト構造

```
kishax-g-python/
├── app/                    # FastAPI バックエンド
│   ├── models/            # SQLAlchemy モデル
│   ├── schemas/           # Pydantic スキーマ
│   ├── api/               # API エンドポイント
│   ├── services/          # ビジネスロジック
│   ├── utils/             # ユーティリティ
│   └── workers/           # Celery タスク
├── tests/                 # テスト
├── streamlit_app/         # Streamlit Web管理画面
├── flet_app/              # Flet モバイル・デスクトップ対応
├── alembic/               # データベースマイグレーション
├── requirements.txt       # Python依存関係
├── Dockerfile            # Docker設定
└── docker-compose.yml    # Docker Compose設定
```

## 🛠️ 開発環境

### 使用技術スタック

- **Backend**: FastAPI + SQLAlchemy + PostgreSQL
- **Frontend Web**: Streamlit
- **Frontend Mobile/Desktop**: Flet (Flutter + Python)
- **Cache**: Redis
- **Task Queue**: Celery
- **AI/ML**: OpenAI API + scikit-learn
- **File Storage**: AWS S3
- **Email**: Amazon SES
- **Auth**: Discord OAuth2
- **Container**: Docker + Docker Compose
- **Monitoring**: Prometheus + Grafana
- **LSP (Language Server Protocol)**: Pyright
- **コードフォーマッター**: Ruff (Python)
- **YAML/YMLフォーマッター**: Prettier
- **Git Flow**: 自動化ワークフロー対応

### 開発ツール要件

- Python 3.9+
- Node.js 18+
- Git

## 🚀 セットアップ手順

### ⚡ 最速起動（Docker使用）

#### 1. リポジトリクローン
```bash
git clone https://github.com/Kishax/g-workspace.git
cd g-workspace
```

#### 2. 環境変数設定
```bash
# .env ファイルを作成
cp .env.example .env

# 最低限の設定で編集
DATABASE_URL=postgresql://user:pass@db:5432/kishax_g
REDIS_URL=redis://redis:6379
JWT_SECRET_KEY=super_secret_key_for_development_only
DEBUG=true
```

#### 3. Docker起動
```bash
docker-compose up -d
```

#### 4. アクセス
- **FastAPI**: http://localhost:8000/docs
- **Streamlit管理画面**: http://localhost:8501

#### ⚠️ 注意点
- `app/models/`でインポートエラーが発生する可能性があります
- 一部のサービス（AWS、Discord、OpenAI）は環境変数なしだとエラーになります

#### 🛠️ 問題が発生したら
```bash
# ログ確認
docker-compose logs -f

# 個別サービス確認
docker-compose logs web
docker-compose logs streamlit
```

### 💡 環境変数の詳細

#### 🔧 **最低限必要（ローカル開発）**
```env
# データベース（Docker使用時は不要）
DATABASE_URL=postgresql://user:pass@localhost:5432/kishax_g
REDIS_URL=redis://localhost:6379

# JWT（必須・任意の長い文字列）
JWT_SECRET_KEY=your_very_long_secret_key_here_12345
```

#### 🌐 **外部サービス（オプション）**

**Discord OAuth2（認証機能使用時のみ）**
- Discord Developer Portal で作成が必要
```env
DISCORD_CLIENT_ID=your_discord_client_id
DISCORD_CLIENT_SECRET=your_discord_client_secret
```

**AWS（メール・ファイル機能使用時のみ）**
- AWS アカウントが必要
```env
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_S3_BUCKET=your-s3-bucket
```

**OpenAI（AI機能使用時のみ）**
```env
OPENAI_API_KEY=your_openai_api_key
```

### 🔧 詳細セットアップ（ローカル開発）

#### 1. リポジトリクローン

```bash
git clone https://github.com/Kishax/g-workspace.git
cd g-workspace
```

### 2. 開発ツールのインストール

#### Pyright (LSP)

```bash
# npm経由でインストール
npm install -g pyright

# または、pipx経由でインストール
pipx install pyright
```

#### Ruff (コードフォーマッター)

```bash
# pip経由でインストール
pip install ruff

# または、pipx経由でインストール
pipx install ruff
```

#### Prettier (YAML/YMLフォーマッター)

```bash
# プロジェクトローカルにインストール
npm install --save-dev prettier

# または、グローバルにインストール
npm install -g prettier
```

### 3. エディタ設定

#### VSCode設定

VSCodeを使用する場合、以下の拡張機能をインストールしてください：

- **Pylance** (Pyright統合)
- **Ruff** (コードフォーマッター)
- **Prettier - Code formatter**

詳細な設定は `.vscode/settings.json` を参照してください。

#### Cursor設定

Cursorを使用する場合、以下の拡張機能をインストールしてください：

- **Pylance**
- **Ruff**
- **Prettier**

詳細な設定は `.cursor/settings.json` を参照してください。

#### Neovim設定

Neovimを使用する場合、私のNeovimの設定を参考にしてください：
(だれも使わないと思うけど！！)
[takayamaekawa/nvim](https://github.com/takayamaekawa/nvim)

## 📝 コーディング規約

### Git Flow

このプロジェクトでは Git Flow を採用しています：

- **main**: 本番環境用ブランチ
- **develop**: 開発用ブランチ
- **feature/\***: 新機能開発用ブランチ
- **fix/\***: バグ修正用ブランチ
- **hotfix/\***: 緊急修正用ブランチ

### コミットメッセージ規約

```
type: 説明文

例:
feat: 新機能を追加
fix: バグを修正
docs: ドキュメントを更新
style: コードスタイルを修正
refactor: コードをリファクタリング
test: テストを追加
chore: その他の作業
```

### コードフォーマット

#### Python

```bash
# コードフォーマット
ruff format .

# リント
ruff check .

# 自動修正
ruff check --fix .
```

#### YAML/YML

```bash
# フォーマット
prettier --write "**/*.{yml,yaml}"

# チェック
prettier --check "**/*.{yml,yaml}"
```

## 🔧 開発コマンド

### 基本的な開発コマンド

```bash
# 開発環境の同期（ローカル変更を保持）
make sync

# 開発環境の強制同期（ローカル変更を破棄）
make sync-force

# テスト実行
make test

# コードフォーマット
make format

# リント実行
make lint
```

### Git同期コマンドの違い

#### `make sync` vs `make sync-force`

**`make sync`（推奨）:**
- `git pull --rebase`を使用
- ローカルの変更を保持してリモートの変更を統合
- 競合が発生した場合は手動で解決が必要
- 安全な同期方法

**`make sync-force`（注意が必要）:**
- `git reset --hard`を使用
- ローカルの変更を完全に破棄してリモートと同期
- 競合は発生しないが、未保存の作業が失われる
- 開発環境をリセットしたい場合に使用

```bash
# 通常の同期（ローカル変更を保持）
make sync

# 強制同期（ローカル変更を破棄、注意！）
make sync-force
```

### その他の便利なコマンド

```bash
# 現在の状況確認
make status

# 新しいfeatureブランチ作成
make new-feature NAME=feature-name

# 新しいfixブランチ作成
make new-fix NAME=fix-name

# コミット実行
make commit MSG="feat: 新機能を追加"

# ブランチをpush
make push

# PR作成前の最終確認
make pr-ready

# マージ済みブランチの削除
make cleanup

# 開発フロー確認
make workflow
```

