# Kishax G Project - フルスタックPython

Google Workspace代替システムのフルスタックPython実装

## 📋 プロジェクト概要

フルスタックPythonアーキテクチャを採用し、Web・モバイル・デスクトップすべてをPythonで統一開発できるGoogle Workspace代替システムです。

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

### 1. リポジトリクローン

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

