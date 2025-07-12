# Microsoft Store 配布設定

## 📋 必要な準備

### 1. Microsoft Partner Center
- **登録料**: $19 (個人) / $99 (企業)
- **登録URL**: https://partner.microsoft.com/dashboard/
- **要件**: Microsoft アカウント

### 2. 開発者アカウント登録
```
1. Partner Center にサインイン
2. 「プログラム」> 「Windows & Xbox」
3. 開発者登録を完了
4. 税務情報と支払い情報を設定
```

### 3. Windows環境でのビルド
```bash
# Windows 環境で実行
cd flet_app
flet build windows --verbose

# または MSIX パッケージ作成
flet build msix --verbose
```

## 📝 アプリ情報設定

### アプリ基本情報
- **アプリ名**: Kishax G
- **パッケージ名**: com.kishax.g-workspace
- **カテゴリ**: 生産性
- **年齢区分**: 3+ (全年齢)

### 説明文
**短い説明** (200文字以内):
```
オープンソースのGoogle Workspace代替アプリ。メール、ファイル管理、ダッシュボードを統合した生産性向上ツール。
```

**詳細説明**:
```
Kishax Gは、現代の働き方に最適化されたオープンソースの生産性向上アプリケーションです。

🚀 主な機能
• 統合メール管理 - 複数アカウントを一元管理
• ファイル管理システム - クラウドストレージ統合
• リアルタイムダッシュボード - KPI可視化
• AI支援機能 - スパム検出と自動分類
• セキュア認証 - Discord OAuth2統合

🌟 特徴
• オープンソース - 完全な透明性と信頼性
• クロスプラットフォーム - Windows、Web、モバイル対応
• プライバシー重視 - ユーザーデータの完全制御
• 高度なカスタマイズ - 組織のニーズに合わせて調整可能

💼 対象ユーザー
• 中小企業の生産性向上
• フリーランサーの業務効率化
• オープンソース愛好者
• プライバシーを重視するユーザー

🔧 技術仕様
• Python/Flet フレームワーク
• FastAPI バックエンド
• PostgreSQL データベース
• Redis キャッシュシステム
• Docker コンテナ対応
```

## 🎨 アプリアセット

### アプリアイコン
- **サイズ**: 
  - 44x44 px
  - 50x50 px  
  - 150x150 px
  - 310x310 px
- **フォーマット**: PNG
- **背景**: 透明または単色

### スクリーンショット
- **サイズ**: 1366x768 px 以上
- **枚数**: 最低1枚、最大10枚
- **フォーマット**: PNG, JPEG
- **内容**: 主要機能のデモンストレーション

### Store Listing Assets
```
screenshots/
├── dashboard_view.png      # ダッシュボード画面
├── email_management.png   # メール管理画面  
├── file_browser.png       # ファイル管理画面
├── settings_panel.png     # 設定画面
└── mobile_responsive.png  # レスポンシブデザイン
```

## 🛠️ パッケージング

### Package.appxmanifest 設定
```xml
<?xml version="1.0" encoding="utf-8"?>
<Package xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  <Identity Name="com.kishax.g-workspace" 
            Publisher="CN=Kishax" 
            Version="1.0.0.0" />
  
  <Properties>
    <DisplayName>Kishax G</DisplayName>
    <PublisherDisplayName>Kishax</PublisherDisplayName>
    <Description>Google Workspace代替オープンソースアプリ</Description>
    <Logo>Assets\Logo.png</Logo>
  </Properties>
  
  <Dependencies>
    <TargetDeviceFamily Name="Windows.Universal" 
                        MinVersion="10.0.17763.0" 
                        MaxVersionTested="10.0.22000.0" />
  </Dependencies>
  
  <Applications>
    <Application Id="KishaxG" 
                 Executable="kishax_g.exe" 
                 EntryPoint="Windows.FullTrustApplication">
      <uap:VisualElements DisplayName="Kishax G"
                          Description="Workspace Alternative"
                          BackgroundColor="transparent"
                          Square150x150Logo="Assets\Logo.png"
                          Square44x44Logo="Assets\SmallLogo.png">
      </uap:VisualElements>
    </Application>
  </Applications>
</Package>
```

## 📤 提出プロセス

### 1. アプリパッケージ準備
```bash
# MSIX パッケージ作成
cd flet_app
flet build msix --release

# パッケージ検証
# Windows App Certification Kit でテスト
```

### 2. Partner Center 提出
```
1. Partner Center > アプリ概要
2. 「新しいアプリ」をクリック
3. アプリ名を予約
4. パッケージをアップロード
5. Store listing 情報入力
6. 価格設定（無料）
7. 提出
```

### 3. 認定プロセス
- **自動テスト**: セキュリティ、パフォーマンス
- **手動レビュー**: コンテンツ、機能
- **認定期間**: 通常1-3営業日

## 💰 価格設定

### 無料アプリ
- **基本料金**: $0.00
- **アプリ内課金**: なし
- **広告**: なし

### 市場別価格
- **すべての市場**: 無料
- **特定地域**: 利用可能に設定

## 🔍 認定要件

### 技術要件
- **Windows 10/11 対応**
- **x64/x86 アーキテクチャ**
- **最小システム要件明記**
- **適切なパフォーマンス**

### コンテンツ要件
- **適切な年齢区分**
- **説明文と機能の一致**
- **著作権遵守**
- **プライバシーポリシー**

## 🔄 更新プロセス

```bash
# バージョンアップ
cd flet_app
flet build msix --release \
    --build-name=1.0.1 \
    --build-number=2

# Partner Center で新しいパッケージをアップロード
```

## ⚠️ 注意事項

### よくある認定失敗理由
- **アプリがクラッシュする**
- **説明文と実際の機能が異なる**
- **セキュリティ要件を満たさない**
- **パフォーマンスが低い**

### ベストプラクティス
- **詳細なテストを実施**
- **正確な説明文を記載**
- **ユーザビリティを重視**
- **定期的な更新**