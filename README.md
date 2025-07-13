# Kishax G Project - フルスタックPython

Google Workspace代替システムのフルスタックPython実装

## 📋 プロジェクト概要

フルスタックPythonアーキテクチャを採用し、Web・モバイル・デスクトップすべてをPythonで統一開発できるGoogle Workspace代替システムです。

## 🚀 実装されたプロジェクトベースでできること

### 📁 **構造化されたプロジェクト**
- モジュール化されたPythonアプリケーション構造
- FastAPI、Streamlit、Fletの3つのアプリケーション層

### 🛠️ **開発環境**
- ハイブリッド構成：インフラ（Docker）+ アプリ（ローカル）
- PostgreSQL + Redis の安定インフラ
- ホットリロード対応の高速開発環境

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
# 1. 環境変数設定
cp .env.example .env

# 2. インフラ起動（Docker）
docker compose up db redis -d

# 3. 依存関係インストール
pip install -r requirements.txt

# 4. アプリケーション起動
uvicorn app.main:app --reload        # FastAPI
streamlit run streamlit_app/main.py  # Streamlit  
python flet_app/main.py             # Flet
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

### ⚡ 最速起動（推奨）

#### 1. リポジトリクローン
```bash
git clone https://github.com/Kishax/g-workspace.git
cd g-workspace
```

#### 2. 環境変数設定
```bash
# .env ファイルを作成（テンプレートから）
cp .env.example .env

# 必要に応じて .env を編集
# 最低限の設定は既に含まれているのでそのまま使用可能
```

#### 3. インフラ起動（Docker）
```bash
# PostgreSQL + Redis のみ起動（アプリはローカル実行）
docker compose up db redis -d
```

#### 4. アプリケーション起動（ローカル）

**Windows環境の場合（推奨）:**
```bash
# ⚠️ 重要: pip install -r requirements.txt はWindowsでエラーになります

# Python依存関係インストール（個別インストール推奨）
pip install fastapi uvicorn sqlalchemy alembic python-multipart requests
pip install scikit-learn==1.7.0 --only-binary=all
pip install pandas --only-binary=all
pip install streamlit --only-binary=all
pip install flet --only-binary=all

# または安全版を使用
pip install -r requirements-windows-safe.txt
# 上記の後に個別で: pip install streamlit --only-binary=all など

# FastAPI サーバー起動
uvicorn app.main:app --reload

# Streamlit 管理画面起動（別ターミナル）
streamlit run streamlit_app/main.py

# Flet デスクトップアプリ起動（別ターミナル）
python flet_app/main.py
```

**その他環境の場合:**
```bash
# Python依存関係インストール
pip install -r requirements.txt

# FastAPI サーバー起動
uvicorn app.main:app --reload

# Streamlit 管理画面起動（別ターミナル）
streamlit run streamlit_app/main.py

# Flet デスクトップアプリ起動（別ターミナル）
python flet_app/main.py
```

#### 5. アクセス
- **FastAPI**: http://localhost:8000/docs
- **Streamlit管理画面**: http://localhost:8501
- **PostgreSQL**: localhost:5432
- **Redis**: localhost:6379

#### 💡 ハイブリッド構成の利点
- **安定性**: インフラはDocker、アプリはローカルで最適なパフォーマンス
- **開発効率**: ホットリロード・デバッグが高速
- **依存関係**: パッケージ競合やネットワーク問題を回避
- **簡単**: `docker compose up -d` だけではアプリは起動しません

#### ❓ `docker compose up -d` だけを実行すると？
- ✅ PostgreSQL（ポート5432）のみ起動
- ✅ Redis（ポート6379）のみ起動  
- ❌ アプリケーション（FastAPI/Streamlit/Flet）は起動しません

### 🐳 Docker管理コマンド

#### 起動状況確認
```bash
# 現在のコンテナ状況を確認
docker compose ps

# すべてのDockerコンテナを確認（他プロジェクト含む）
docker ps
```

#### インフラ停止
```bash
# プロジェクトのコンテナを停止・削除
docker compose down

# 特定サービスのみ停止
docker compose stop db redis
```

#### システムクリーンアップ
```bash
# 未使用のコンテナ・ネットワーク・イメージを削除
docker system prune -f

# ボリュームも含めて完全クリーンアップ（注意：データが削除されます）
docker system prune -a --volumes -f
```

#### よく使うパターン
```bash
# 完全リセット（開発環境のトラブル時）
docker compose down
docker system prune -f
docker compose up db redis -d

# 起動確認
docker compose ps
```

## 🐛 Fletアプリのデバッグ方法

### 🎯 デバッグモード別の特徴

| モード | 用途 | 実機テスト | コマンド |
|--------|------|------------|----------|
| **デスクトップ** | PC開発・デバッグ | ❌ | `make flet-debug` |
| **ブラウザ** | 実機テスト・共有 | ✅ | `make flet-web` |
| **シンプル** | 動作確認・学習 | ✅ | `make flet-simple` |

### 🖥️ デスクトップモードでのデバッグ

PCでの高速開発・デバッグに最適：

```bash
# メインアプリをデスクトップで起動
make flet-debug

# または直接実行
python flet_app/main.py
```

**特徴:**
- ✅ 高速起動・レスポンス
- ✅ デバッグ出力がターミナルに表示
- ✅ ホットリロード（コード変更時の再起動）
- ❌ 実機での確認はできない

### 🌐 ブラウザモード（実機テスト）

スマホ・タブレットでの実機テストに最適：

```bash
# メインアプリをブラウザモードで起動
make flet-web

# または直接実行（WSL2環境）
python -c "import flet as ft; from flet_app.main import main; ft.app(target=main, view=ft.WEB_BROWSER, port=8080)"
```

**アクセス方法:**
1. **PC**: http://localhost:8080
2. **実機**: http://[PCのIPアドレス]:8080

**実機でのアクセス手順:**
```bash
# 1. PCのIPアドレスを確認
ip addr show eth0 | grep inet  # WSL2の場合

# 2. スマホ・タブレットでアクセス
# 例: http://192.168.1.100:8080
```

**特徴:**
- ✅ 実機での動作確認
- ✅ タッチ操作・レスポンシブデザインのテスト
- ✅ チーム共有が簡単
- ❌ デスクトップより若干重い

### 🔍 シンプルデバッグテスト

動作確認・学習用の軽量テストアプリ：

```bash
# シンプルなテストアプリを起動
make flet-simple

# または直接実行
python flet_debug_simple.py
```

**特徴:**
- ✅ 最小構成でのテスト
- ✅ Fletの基本動作確認
- ✅ デバッグ出力の確認
- ✅ 実機テスト可能（ブラウザモード）

### 🛠️ トラブルシューティング

#### WSL2でGUIエラーが出る場合

デスクトップモードで以下のようなエラーが出る場合：

```
qt.qpa.plugin: Could not find the Qt platform plugin "wayland"
```

**対処法**: ブラウザモードを使用
```bash
# GUIエラーを回避してブラウザで確認
make flet-web
```

#### ポート競合エラーの場合

```bash
# ポート使用状況を確認
lsof -i :8080

# プロセスを終了
kill -9 [PID]

# または別ポートを使用
python -c "import flet as ft; from flet_app.main import main; ft.app(target=main, view=ft.WEB_BROWSER, port=8081)"
```

#### 実機からアクセスできない場合

1. **ファイアウォール確認**:
   ```bash
   # Windows側でポート8080を開放
   # Windows設定 > ネットワークとインターネット > Windows Defender ファイアウォール
   ```

2. **WSL2ネットワーク確認**:
   ```bash
   # WSL2のIPアドレス確認
   hostname -I
   ```

3. **同じWi-Fiネットワークに接続確認**

### 📱 実機テストのベストプラクティス

#### 開発フロー
```bash
# 1. デスクトップで高速開発
make flet-debug
# コード編集・デバッグ

# 2. 実機で動作確認
make flet-web
# スマホでhttp://[IP]:8080にアクセス

# 3. 問題があればデスクトップに戻る
```

#### 実機テスト項目
- ✅ タッチ操作の反応性
- ✅ 画面サイズ・レスポンシブ対応
- ✅ スクロール動作
- ✅ 文字サイズ・読みやすさ
- ✅ ネットワーク処理（ローディング等）

## 📦 クロスプラットフォームビルド

Fletアプリを各プラットフォーム用のネイティブアプリとしてビルドできます。

### 🎯 対応プラットフォーム

| プラットフォーム | 出力形式 | 配布方法 | ビルド環境 | コマンド | 対応状況 |
|----------------|----------|----------|-----------|----------|----------|
| **Android** | `.apk` | Google Play / サイドロード | Android Studio + SDK | `make build-android` | ⚠️ 今後対応予定 |
| **iOS** | `.ipa` | App Store / TestFlight | macOS + Xcode | `make build-ios` | ⚠️ 今後対応予定 |
| **macOS** | `.app` | App Store / 直接配布 | macOS | `make build-macos` | ✅ 対応済み |
| **Windows** | `.exe` | Microsoft Store / 直接配布 | Windows | `make build-windows` | ✅ 対応済み |
| **Linux** | `実行ファイル` | 直接配布 | Linux | `make build-linux` | ✅ 対応済み |
| **Web** | `PWA` | Webホスティング | 全環境 | `make build-web` | ✅ 対応済み |

**注記**: 現在のFletバージョンでは、モバイルアプリ（Android/iOS）のネイティブビルドは未対応です。代替案としてWebアプリ（PWA）での配布を推奨します。

### 🔍 ビルド環境チェック

現在の環境でビルド可能なプラットフォームを確認：

```bash
# ビルド環境をチェック
make build-check
```

### 🛠️ 環境別セットアップ

#### Android開発環境

```bash
# 1. Android Studioをインストール
# https://developer.android.com/studio

# 2. Android SDKの設定
# Android Studio > SDK Manager > Android SDK

# 3. 環境変数設定
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools

# 4. APKビルド
make build-android
```

**出力**: `flet_app/build/apk/`

#### iOS開発環境（macOSのみ）

```bash
# 1. Xcodeをインストール
# App Storeからインストール

# 2. Xcode Command Line Toolsをインストール
xcode-select --install

# 3. IPAビルド
make build-ios
```

**出力**: `flet_app/build/ipa/`

#### Web PWA

```bash
# 全環境で利用可能
make build-web
```

**出力**: `flet_app/build/web/`

**配布方法:**
- Netlify, Vercel等にデプロイ
- PWAとしてホーム画面追加可能

### 🚀 ビルド例

#### 1. Android APK作成
```bash
# APKビルド（デバッグ版）
make build-android

# リリース版（署名が必要）
cd flet_app
flet build apk --release
```

#### 2. Web PWA作成
```bash
# PWAビルド
make build-web

# ローカルでプレビュー
cd flet_app/build/web
python -m http.server 8080
# http://localhost:8080 でアクセス
```

#### 3. 複数プラットフォーム同時ビルド
```bash
# 現在の環境で利用可能な全プラットフォーム
make build-linux build-web

# macOSの場合
make build-macos build-ios build-web
```

### 🚀 ビルドファイルの実行

#### Linux実行ファイル
```bash
# ビルド済みファイルを実行
make run-linux

# ビルド → 実行（一連の流れ）
make build-run-linux

# 手動実行
./flet_app/dist/Kishax-G
```

**出力先**: `flet_app/dist/Kishax-G` (約60MB)

#### Web PWA
```bash
# ローカルサーバーで起動
make run-web

# ビルド → 実行（一連の流れ）
make build-run-web

# 手動実行
cd flet_app
python -m http.server 8080 --directory dist
# ブラウザで http://localhost:8080 にアクセス
```

**出力先**: `flet_app/dist/` (Web ファイル一式)

### 📱 アプリストア配布

#### Google Play Store（Android）

1. **開発者アカウント作成**
   - Google Play Console登録（$25）

2. **リリース版APK作成**
   ```bash
   cd flet_app
   flet build apk --release
   ```

3. **アプリ署名・アップロード**
   - Play Console > アプリ作成 > APKアップロード

#### Apple App Store（iOS）

1. **開発者アカウント作成**
   - Apple Developer Program登録（$99/年）

2. **リリース版IPA作成**
   ```bash
   cd flet_app
   flet build ipa --release
   ```

3. **App Store Connect**
   - Xcode > Archive > Distribute App

### 🛠️ トラブルシューティング

#### Androidビルドエラー

```bash
# SDKパスエラーの場合
echo $ANDROID_HOME  # 設定確認

# Gradle権限エラーの場合
cd flet_app
chmod +x gradlew
```

#### iOSビルドエラー

```bash
# Xcodeライセンス確認
sudo xcodebuild -license accept

# 証明書エラーの場合
# Xcode > Preferences > Accounts > Sign In
```

#### 一般的なビルドエラー

```bash
# Fletキャッシュクリア
cd flet_app
rm -rf build/
flet build [platform] --verbose
```

### 💡 ビルド最適化

#### APKサイズ削減

```bash
# ProGuard有効化（ビルド設定）
cd flet_app
flet build apk --release --obfuscate
```

#### PWA最適化

```bash
# 圧縮ビルド
cd flet_app
flet build web --release
```

### 🔧 ビルド設定ファイル

主要な設定ファイルがプロジェクトに自動生成されます：

- `flet_app/pubspec.yaml` - Flutter/Dart依存関係
- `flet_app/android/` - Android固有設定
- `flet_app/ios/` - iOS固有設定
- `flet_app/web/` - Web固有設定

## 🚀 アプリストア配布

### 📱 配布対応ストア

| ストア | プラットフォーム | 手数料 | 審査期間 | 設定ファイル |
|--------|----------------|--------|----------|-------------|
| **Google Play** | Android | 30% | 1-3日 | `store-configs/google-play/` |
| **App Store** | iOS/macOS | 30% | 1-2日 | `store-configs/app-store/` |
| **Microsoft Store** | Windows | 30% | 1-3営業日 | `store-configs/microsoft-store/` |
| **Snap Store** | Linux | 無料 | 即時 | `store-configs/snap-store/` |

### 🎯 自動配布システム

#### GitHub Actions による自動ビルド・配布

```bash
# リリースタグを作成して全プラットフォーム自動ビルド
make create-tag VERSION=v1.0.0

# 進行状況確認
make release-status
```

**自動実行される処理:**
1. **6プラットフォーム同時ビルド** (Linux, Web, Windows, macOS, Android, iOS)
2. **GitHub Releases への自動アップロード**
3. **配布用パッケージの作成**

#### 手動リリース（現在の環境のみ）

```bash
# 現在の環境で可能なビルドを実行
make release

# 環境自動判定でパッケージ作成
make package-current
```

### 📦 ストア別配布手順

#### 🟢 Google Play Store (Android)
```bash
# 設定確認
cat store-configs/google-play/README.md

# 主な手順
1. Google Play Console アカウント作成 ($25)
2. 署名キー作成
3. APKビルド: make build-android
4. Play Console アップロード
5. 審査・公開 (1-3日)
```

#### 🟣 Apple App Store (iOS/macOS)
```bash
# 設定確認
cat store-configs/app-store/README.md

# 主な手順 (macOS環境必須)
1. Apple Developer Program 登録 ($99/年)
2. 証明書・プロビジョニングプロファイル作成
3. IPAビルド: make build-ios
4. App Store Connect アップロード
5. 審査・公開 (1-2日)
```

#### 🟦 Microsoft Store (Windows)
```bash
# 設定確認
cat store-configs/microsoft-store/README.md

# 主な手順 (Windows環境必須)
1. Microsoft Partner Center 登録 ($19)
2. MSIXパッケージ作成
3. EXEビルド: make build-windows
4. Partner Center アップロード
5. 認定・公開 (1-3営業日)
```

#### 🟠 Snap Store (Linux)
```bash
# 設定確認
cat store-configs/snap-store/README.md

# 主な手順 (無料・即時)
1. Snapcraft アカウント作成 (無料)
2. snapcraft ツールインストール
3. Snapパッケージビルド
4. Snap Store アップロード
5. 即時公開
```

### 🔄 継続的配布フロー

#### 1. 開発 → テスト
```bash
# 機能開発
make new-feature NAME=new-ui
# 開発作業...
make commit MSG="feat: 新UI機能を追加"

# デバッグ・テスト
make flet-debug    # ローカルテスト
make flet-web      # 実機テスト
```

#### 2. ビルド → 検証
```bash
# ローカルビルドテスト
make build-web     # 軽量ビルドで動作確認
make build-linux   # 現在環境でのビルド確認
```

#### 3. リリース → 配布
```bash
# バージョンタグ作成 → 自動ビルド開始
make create-tag VERSION=v1.0.0

# GitHub Actions で全プラットフォーム自動ビルド
# ↓
# GitHub Releases に配布ファイル自動アップロード
# ↓
# 各ストアへ手動アップロード（将来的に自動化予定）
```

### 📊 配布状況の監視

#### GitHub での確認
```bash
# リリース状況確認
make release-status

# 直接確認
# Actions: https://github.com/Kishax/g-workspace/actions
# Releases: https://github.com/Kishax/g-workspace/releases
```

#### ストア別Analytics
- **Google Play Console**: インストール数、クラッシュ率
- **App Store Connect**: ダウンロード数、レビュー  
- **Microsoft Partner Center**: 使用状況、収益
- **Snap Store**: アクティブユーザー、地域統計

### 💡 配布戦略

#### フェーズ1: オープンソース配布
```bash
# GitHub Releases で全プラットフォーム配布
make create-tag VERSION=v1.0.0
```

#### フェーズ2: ストア展開
1. **Snap Store** (無料・即時) → Linux ユーザー獲得
2. **Google Play** (Android) → モバイルユーザー拡大
3. **Microsoft Store** (Windows) → 企業ユーザー獲得
4. **App Store** (iOS/macOS) → Apple エコシステム参入

#### フェーズ3: エンタープライズ
- カスタムビルド提供
- オンプレミス展開サポート
- 企業向けライセンスモデル

## 📢 Slack通知設定

### 🔧 PR作成時のSlack通知
新しいワークフローにより、PR作成・更新時に自動でSlack通知を送信します。

```bash
# 通知対象イベント
- PR作成 (opened)
- PR更新 (synchronize) 
- PR再オープン (reopened)
- PRマージ/クローズ (closed)
```

### ⚙️ 設定手順

#### 1. Slack Webhook URL取得
1. https://api.slack.com/apps にアクセス
2. 「Create New App」→「From scratch」
3. App名とワークスペースを設定
4. 「Incoming Webhooks」を有効化
5. 「Add New Webhook to Workspace」でチャンネル選択
6. 生成されたWebhook URLをコピー

#### 2. GitHub シークレット設定
1. GitHubリポジトリ > Settings > Secrets and variables > Actions
2. 「New repository secret」
3. Name: `SLACK_WEBHOOK_URL`
4. Secret: 上記で取得したWebhook URL

### 📱 通知内容
- **基本情報**: PR タイトル、作成者、ブランチ
- **統計**: 変更ファイル数、追加/削除行数
- **リンク**: PR の直接リンク
- **自動チェック結果**: ブランチ名・コミットメッセージ規約

### 🛠️ フォールバック機能
Slack設定が未完了の場合、GitHub PR コメントで通知されます。

### 💡 環境変数の詳細

`.env.example`ファイルには設定項目が明確に分類されています：

#### 🔧 **必須設定（最低限必要）**
```env
DATABASE_URL=postgresql://user:pass@localhost:5432/kishax_g
REDIS_URL=redis://localhost:6379
JWT_SECRET_KEY=your_very_long_secret_key_here_please_change_this
DEBUG=true
ALLOWED_ORIGINS=["http://localhost:3000","http://localhost:8501"]
ENABLE_METRICS=true
```

#### 🌐 **外部サービス設定（オプション）**
これらの機能を使用する場合のみ、コメントアウトを外して設定：

- **Discord OAuth2**: 認証機能用
- **AWS S3**: ファイル管理機能用  
- **Amazon SES**: メール送信機能用
- **OpenAI API**: AI機能用

#### ⚙️ **設定のポイント**
- **コピーするだけ**: `cp .env.example .env` で基本設定完了
- **段階的拡張**: 必要な機能に応じて外部サービス設定を追加
- **セキュリティ**: JWT_SECRET_KEYは必ず変更してください

## 🔧 Windows環境での追加セットアップ

**Windows開発者の方**: Windows環境特有の問題・解決策・最適化手順については、専用ガイドをご確認ください。

📋 **[Windows環境セットアップガイド](./WINDOWS-SETUP.md)**
- Windows開発者向け最速セットアップ手順
- よくある問題と即効解決法
- Fletアプリ Windows EXEビルド方法  
- コンパイラ設定・トラブルシューティング

💡 **Windows用追加ファイル:**
- `requirements-windows-safe.txt` - コンパイラ不要の安全版パッケージリスト

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
- **chore/\***: メンテナンス・雑務用ブランチ
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

