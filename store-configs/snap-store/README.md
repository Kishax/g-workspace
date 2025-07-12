# Snap Store 配布設定

## 📋 必要な準備

### 1. Snapcraft アカウント
- **登録料**: 無料
- **登録URL**: https://snapcraft.io/
- **要件**: Ubuntu One アカウント

### 2. Snapcraft ツールのインストール
```bash
# Ubuntu/Debian
sudo apt install snapd snapcraft

# その他のLinux
sudo snap install snapcraft --classic

# ログイン
snapcraft login
```

## 🛠️ Snap パッケージビルド

### 1. snapcraft.yaml 確認
プロジェクトルートの `store-configs/snap-store/snapcraft.yaml` を確認

### 2. Snapパッケージビルド
```bash
# プロジェクトルートで実行
cp store-configs/snap-store/snapcraft.yaml .

# Snapビルド
snapcraft

# ローカルインストールテスト
sudo snap install --dangerous --devmode kishax-g_1.0.0_amd64.snap

# アプリ起動テスト
kishax-g
```

## 📤 Snap Store 提出

### 1. Store 登録
```bash
# アプリ名を登録
snapcraft register kishax-g

# アップロード
snapcraft upload kishax-g_1.0.0_amd64.snap

# リリース
snapcraft release kishax-g 1 stable
```

### 2. Store Listing 設定
```bash
# メタデータ設定
snapcraft set-metadata kishax-g \
    --summary="Google Workspace代替オープンソースアプリ" \
    --description="$(cat store-configs/snap-store/description.txt)"

# アイコン設定
snapcraft set-icon kishax-g assets/icon.png

# スクリーンショット追加
snapcraft set-screenshot kishax-g screenshot1.png
snapcraft set-screenshot kishax-g screenshot2.png
```

## 🎯 チャンネル管理

### チャンネルの種類
- **stable**: 本番リリース（推奨）
- **candidate**: リリース候補
- **beta**: ベータテスト
- **edge**: 開発版

### リリース管理
```bash
# ベータリリース
snapcraft release kishax-g 1 beta

# 安定版にプロモート
snapcraft release kishax-g 1 stable

# リビジョン確認
snapcraft list-revisions kishax-g
```

## 📊 Store 情報

### アプリ詳細
- **カテゴリ**: productivity
- **ライセンス**: オープンソース
- **価格**: 無料
- **対象年齢**: すべて

### 説明文 (description.txt)
```
Kishax Gは、Google Workspaceの代替として開発されたオープンソースの生産性向上アプリケーションです。

🚀 主な機能
• 統合メール管理 - 複数アカウントを一元管理
• ファイル管理システム - クラウドストレージとの連携
• リアルタイムダッシュボード - 業務状況の可視化
• AI支援機能 - スパム検出と自動分類
• セキュア認証 - Discord OAuth2統合

🌟 特徴
• オープンソース - 完全な透明性
• クロスプラットフォーム - Linux、Web、モバイル対応
• プライバシー重視 - ユーザーデータの完全制御
• 軽量設計 - 最小限のシステムリソース使用

💼 ユースケース
• 中小企業の業務効率化
• フリーランサーの生産性向上
• 開発チームのコラボレーション
• プライバシーを重視する組織

🔧 技術
Python/Fletフレームワークで構築され、モダンで使いやすいUIを提供します。
```

## 🔧 権限とインターフェース

### 必要な権限
```yaml
plugs:
  - home          # ホームディレクトリアクセス
  - network       # ネットワーク通信
  - network-bind  # サーバー機能
  - desktop       # デスクトップ統合
  - x11           # X11ディスプレイ
  - wayland       # Waylandディスプレイ
  - opengl        # グラフィック加速
  - audio-playback # 通知音
```

### セキュリティ
- **confinement: strict** - 厳格なサンドボックス
- **grade: stable** - 安定版品質

## 📈 Analytics とモニタリング

### メトリクス確認
```bash
# インストール数確認
snapcraft metrics kishax-g

# レビュー確認
snapcraft list-reviews kishax-g
```

### ストア統計
- **インストール数**
- **アクティブユーザー**
- **地域別統計**
- **バージョン別使用状況**

## 🔄 継続的配布

### GitHub Actions との連携
```yaml
# .github/workflows/snap-release.yml
name: Snap Release
on:
  push:
    tags: ['v*']

jobs:
  snap:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: snapcore/action-build@v1
    - uses: snapcore/action-publish@v1
      with:
        store_login: ${{ secrets.STORE_LOGIN }}
        snap: kishax-g_*.snap
        release: stable
```

### 自動更新
```bash
# 新バージョンビルド
snapcraft

# 自動アップロード・リリース
snapcraft upload kishax-g_1.0.1_amd64.snap --release=stable
```

## ⚠️ 注意事項

### ビルド要件
- **Linux環境**: Ubuntu 20.04+ 推奨
- **メモリ**: 最低2GB（ビルド時）
- **ディスク**: 最低5GB空き容量

### よくある問題
- **依存関係エラー**: stage-packages で解決
- **権限不足**: plugs に適切な権限追加
- **サイズ制限**: 不要ファイルを除外

### ベストプラクティス
- **小さなパッケージサイズ**: 不要な依存関係を除外
- **適切な権限**: 最小限の権限で動作
- **詳細な説明**: ユーザーが理解しやすい説明
- **定期的な更新**: セキュリティとバグ修正