# 🔧 Windows環境セットアップガイド

Windows環境でKishax G Projectを開発・ビルドするための完全ガイド

## 🚀 Windows開発者向け最速セットアップ

**🚨 重要**: Windows環境では `pip install -r requirements.txt` でエラーが発生します。以下の個別インストール手順を使用してください。

### ステップ1: 基本的なセットアップ
```bash
# 1. リポジトリクローン
git clone https://github.com/Kishax/g-workspace.git
cd g-workspace

# 2. Python仮想環境作成・有効化
python -m venv venv
venv\Scripts\activate  # Windowsの場合

# 3. pipを最新版に更新
python -m pip install --upgrade pip
```

### ステップ2: コアパッケージの個別インストール（必須）
```bash
# ⚠️ 重要: pip install -r requirements.txt は使用しない！

# 1. 基本Webフレームワーク（プリビルド版のみ）
pip install fastapi uvicorn sqlalchemy alembic python-multipart requests

# 2. 機械学習・データ分析パッケージ（プリビルド版強制）
pip install scikit-learn==1.7.0 --only-binary=all
pip install pandas --only-binary=all

# 3. UI フレームワーク（プリビルド版強制）
pip install streamlit --only-binary=all
pip install flet --only-binary=all

# 4. Fletビルド用依存関係
pip install pyinstaller
```

### ステップ3: 残りパッケージの追加インストール（オプション）
```bash
# データベース接続
pip install psycopg-binary

# 認証・セキュリティ（必要に応じて）
pip install python-jose[cryptography] passlib[bcrypt]

# 外部サービス（必要に応じて）
pip install boto3 celery redis openai

# テスト・開発ツール
pip install pytest pytest-asyncio httpx
```

### ⚠️ 絶対に避けるべきこと
```bash
# ❌ これは絶対にしない（Windowsでエラーになる）
pip install -r requirements.txt

# ❌ ソースからのビルドを強制しない
pip install streamlit --no-binary=streamlit

# ❌ 古いバージョンを固定しない  
pip install scikit-learn==1.3.2
```

## ⚠️ よくある問題と解決策

### 問題1: scikit-learn文字コードエラー
```
UnicodeDecodeError: 'cp932' codec can't decode byte 0x97
```

**即効解決法：**
```bash
# Python 3.13対応のプリビルド版を使用
pip install scikit-learn==1.7.0 --only-binary=all
```

### 問題2: pydantic-coreビルドエラー
```
Cargo, the Rust package manager, is not installed
```

**即効解決法：**
```bash
# より新しいプリビルド版を使用
pip install pydantic>=2.11.0 --only-binary=all
```

### 問題3: pandas/streamlitビルドエラー
```bash
# プリビルド版のみを使用してビルドを回避
pip install pandas>=2.2.0 --only-binary=all
pip install streamlit --only-binary=all
```

### 問題4: psycopg2-binary PostgreSQLエラー
```
Error: pg_config executable not found
```

**即効解決法：**
```bash
# requirements.txtで既にpsycopg-binaryに変更済み
# 追加作業不要
```

### 問題5: PyInstallerエラー (Fletビルド時)
```
Please install PyInstaller module to use flet pack command: No module named 'PyInstaller'
```

**即効解決法：**
```bash
pip install pyinstaller
```

### 問題6: numpy/streamlitビルドエラー（一括インストール時）
```
ERROR: Unknown compiler(s): [['icl'], ['cl'], ['cc'], ['gcc'], ['clang'], ['clang-cl'], ['pgcc']]
WARNING: Failed to activate VS environment: Could not parse vswhere.exe output
```

**即効解決法：**
```bash
# ❌ これを避ける
pip install -r requirements.txt

# ✅ 代わりにこれを使用
pip install streamlit --only-binary=all
pip install pandas --only-binary=all
pip install scikit-learn==1.7.0 --only-binary=all
```

**根本原因**: numpy（streamlitの依存関係）がMesonビルドシステムでコンパイラを見つけられない

**完全解決法（Visual Studio Build Tools設定）:**
```bash
# 1. Visual Studio Build Tools 2022をインストール
winget install Microsoft.VisualStudio.2022.BuildTools

# 2. インストール時に以下を選択:
# - C++ build tools ワークロード
# - Windows 10/11 SDK
# - MSVC v143 コンパイラツールセット

# 3. 環境変数確認
where cl  # cl.exeが見つかればOK

# 4. 再試行
pip install -r requirements.txt
```

## 🏗️ Windows EXEビルド完全ガイド

### PyInstallerのインストール

**簡単インストール（推奨）:**
```bash
# PyInstallerはプリビルド版があるので、Windowsでも簡単
pip install pyinstaller

# インストール確認
pyinstaller --version
```

**特徴:**
- ✅ コンパイラ不要（プリビルド版あり）
- ✅ Python 3.13対応
- ✅ Fletと完全互換性
- ✅ 単体実行ファイル生成可能

### Fletアプリの完全ビルド手順

#### 方法1: Makefileを使用（推奨）
```bash
# 1. 依存関係確認
pip list | grep -E "(flet|pyinstaller)"

# 2. ビルド実行
make build-windows

# 3. 成果物確認
ls flet_app/dist/Kishax-G.exe
```

#### 方法2: 手動ビルド
```bash
# 1. Fletアプリディレクトリに移動
cd flet_app

# 2. 手動ビルド（詳細ログ付き）
flet pack main.py --name "Kishax-G" --verbose

# 3. 成果物確認
dir dist\Kishax-G.exe
```

#### 方法3: カスタムビルド（高度）
```bash
cd flet_app

# アイコン付きビルド
flet pack main.py --name "Kishax-G" --icon assets/icon.ico --verbose

# 追加ファイル含めてビルド
flet pack main.py --name "Kishax-G" --add-data "assets;assets" --verbose

# ワンファイルモード（推奨）
flet pack main.py --name "Kishax-G" --onefile --verbose
```

### ビルド成功後の確認

**生成されるファイル:**
```
flet_app/
├── dist/
│   ├── Kishax-G.exe          # メイン実行ファイル
│   └── _internal/            # 依存関係（--onefileでない場合）
├── build/                    # ビルド一時ファイル
└── Kishax-G.spec            # PyInstaller設定ファイル
```

**実行ファイルの特徴:**
- **サイズ**: 約 50-100MB
- **配布**: 単体実行ファイルとして配布可能
- **依存関係**: Python環境不要で実行可能
- **起動時間**: 初回起動は数秒かかる場合あり

### ビルドエラーと解決法

#### エラー1: PyInstallerが見つからない
```
Please install PyInstaller module to use flet pack command: No module named 'PyInstaller'
```

**解決法:**
```bash
pip install pyinstaller
```

#### エラー2: モジュールが見つからない
```
ModuleNotFoundError: No module named 'XXX'
```

**解決法:**
```bash
# 不足モジュールを追加インストール
pip install XXX

# または.specファイルを編集してhidden imports追加
# hiddenimports=['XXX']
```

#### エラー3: ビルドサイズが大きすぎる
```bash
# 不要な依存関係を除外
flet pack main.py --name "Kishax-G" --exclude-module numpy --verbose

# または軽量版ビルド
flet pack main.py --name "Kishax-G" --strip --verbose
```

### ビルドトラブルシューティング

#### キャッシュクリア（問題発生時）
```bash
cd flet_app

# ビルドキャッシュクリア
rmdir /s /q build dist
del Kishax-G.spec

# 完全クリーンビルド
flet pack main.py --name "Kishax-G" --verbose
```

#### 詳細デバッグ
```bash
# 詳細ログでデバッグ
flet pack main.py --name "Kishax-G" --verbose --debug

# PyInstaller直接実行（高度）
pyinstaller --onefile --windowed main.py --name "Kishax-G"
```

#### パフォーマンス最適化
```bash
# 起動速度重視（ファイル分散）
flet pack main.py --name "Kishax-G" --verbose

# サイズ重視（ワンファイル）
flet pack main.py --name "Kishax-G" --onefile --verbose

# 軽量化（不要モジュール除外）
flet pack main.py --name "Kishax-G" --exclude-module matplotlib --exclude-module pandas --verbose
```

### ビルド後のテスト

```bash
# 1. 実行ファイルテスト
flet_app/dist/Kishax-G.exe

# 2. 別PCでテスト（Python未インストール環境）
# 実行ファイルをコピーして動作確認

# 3. 配布用ZIP作成
cd flet_app/dist
tar -a -c -f Kishax-G-Windows.zip Kishax-G.exe
```

## 🛠️ 高度なセットアップ（コンパイラが必要な場合）

もしプリビルド版で解決しない場合のみ、以下のコンパイラをインストール：

### Visual Studio Build Tools 2022
```bash
# wingetでインストール（推奨）
winget install Microsoft.VisualStudio.2022.BuildTools

# または手動ダウンロード
# https://visualstudio.microsoft.com/ja/downloads/#build-tools-for-visual-studio-2022
```

**重要な設定:**
- 「C++ build tools」ワークロードを選択
- Windows 10/11 SDK を含める
- MSVC v143 コンパイラツールセットを含める

### Rust コンパイラ
```bash
# rustupでインストール
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# 環境変数の更新（コマンドプロンプトを再起動）
# または PowerShellで
$env:PATH += ";$env:USERPROFILE\.cargo\bin"

# インストール確認
cargo --version
rustc --version
```

### PostgreSQL（pg_configが必要な場合）
```bash
# Chocolateyでインストール（管理者権限が必要）
choco install postgresql

# または手動ダウンロード
# https://www.postgresql.org/download/windows/

# 環境変数PATHにPostgreSQLのbinディレクトリを追加
# 例: C:\Program Files\PostgreSQL\16\bin
```

## 💡 Windows環境のベストプラクティス

### 推奨アプローチ
1. **プリビルド版優先**: `--only-binary=all` を常に使用
2. **個別インストール**: `pip install -r requirements.txt` ではなく個別インストール
3. **最新版使用**: Python 3.13対応の最新パッケージを選択
4. **仮想環境必須**: システムPythonへの直接インストールは避ける

### 避けるべきこと
- ❌ 古いバージョンの固定（例: scikit-learn==1.3.2）
- ❌ 一括インストール時のビルドエラー放置
- ❌ コンパイラインストール前の強行突破
- ❌ システムPythonへの直接インストール

### 開発環境推奨設定
```bash
# 開発用の追加ツール
pip install black isort mypy  # コードフォーマッター・型チェック
pip install jupyter notebook  # 開発・実験用

# Git設定（初回のみ）
git config --global core.autocrlf true  # Windows改行コード対応
```

## 🎯 動作確認済み構成

**Python**: 3.13.3  
**OS**: Windows 10/11 (WSL2でも動作確認済み)  
**アーキテクチャ**: x64

**インストール成功パッケージ:**
```
fastapi                   0.116.1
flet                      0.28.3
pandas                    2.3.1
pydantic                  2.11.7
pyinstaller               6.11.1
scikit-learn              1.7.0
streamlit                 1.46.1
uvicorn                   0.35.0
```

## 🔄 継続的開発フロー

### 日常的な開発作業
```bash
# 1. 最新コードを取得
git pull origin develop

# 2. 仮想環境有効化
venv\Scripts\activate

# 3. 依存関係更新（必要に応じて）
pip install --upgrade pip
pip install -U fastapi uvicorn streamlit flet

# 4. 開発開始
uvicorn app.main:app --reload
```

### リリース前の確認作業
```bash
# 1. テスト実行
pytest

# 2. コードフォーマット
black . && isort .

# 3. 型チェック
mypy app/

# 4. ローカルビルドテスト
make build-windows

# 5. ビルド成果物確認
flet_app/dist/Kishax-G.exe
```

## 📚 関連リンク

- [メインREADME](./README.md) - プロジェクト概要・基本セットアップ
- [Fletアプリストア配布](./README.md#-アプリストア配布) - Microsoft Store配布手順
- [Flet公式ドキュメント](https://flet.dev/) - Fletフレームワーク詳細
- [FastAPI公式ドキュメント](https://fastapi.tiangolo.com/) - FastAPI詳細

## 🆘 トラブルシューティング

### よくあるエラーと対処法

**エラー**: `'python' is not recognized as an internal or external command`
```bash
# Python PATH設定確認
where python
# Pythonを再インストールし、「Add Python to PATH」をチェック
```

**エラー**: `Microsoft Visual C++ 14.0 is required`
```bash
# Visual Studio Build Tools 2022をインストール
winget install Microsoft.VisualStudio.2022.BuildTools
```

**エラー**: `error: Microsoft Visual C++ 14.0 or greater is required`
```bash
# 既存のVisual Studioを更新
# または上記のBuild Toolsをインストール
```

**エラー**: `flet: command not found`
```bash
# Fletを再インストール
pip uninstall flet
pip install flet
```

**その他の問題**: 
[GitHub Issues](https://github.com/Kishax/g-workspace/issues) で報告・検索してください。