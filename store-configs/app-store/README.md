# Apple App Store 配布設定

## 📋 必要な準備

### 1. Apple Developer Program
- **年間費用**: $99
- **登録URL**: https://developer.apple.com/programs/
- **要件**: macOS環境必須

### 2. 開発環境セットアップ
```bash
# Xcode インストール（App Storeから）
# Command Line Tools インストール
xcode-select --install

# 証明書とプロビジョニングプロファイル設定
# Xcode > Preferences > Accounts > Sign In
```

### 3. App Store Connect 設定
- **URL**: https://appstoreconnect.apple.com/
- **Bundle ID**: com.kishax.g-workspace
- **App ID登録**: Developer Portal

## 📝 アプリ情報設定

### アプリ基本情報
- **アプリ名**: Kishax G
- **サブタイトル**: Workspace Alternative
- **カテゴリ**: Productivity
- **価格**: 無料

### 説明文
```
Kishax Gは、Google Workspaceの代替として設計されたオープンソースの生産性向上アプリです。

主な機能:
• 統合メール管理
• クラウドファイル管理  
• リアルタイムダッシュボード
• AI支援による自動化
• セキュアな認証システム

特徴:
• オープンソース - 完全な透明性
• クロスプラットフォーム対応
• プライバシー重視の設計
• 高度なカスタマイズ性

企業から個人まで、あらゆる生産性ニーズに対応します。
```

### キーワード
```
productivity, workspace, email, files, opensource, python, collaboration, dashboard, security
```

## 🛠️ ビルド設定

### iOS固有設定
```bash
# iOS用ビルド（macOSのみ）
cd flet_app
flet build ipa --release \
    --build-name=1.0.0 \
    --build-number=1
```

### Info.plist 設定
```xml
<key>CFBundleDisplayName</key>
<string>Kishax G</string>
<key>CFBundleIdentifier</key>
<string>com.kishax.g-workspace</string>
<key>CFBundleVersion</key>
<string>1</string>
<key>CFBundleShortVersionString</key>
<string>1.0.0</string>
<key>NSCameraUsageDescription</key>
<string>ファイルアップロード用の写真撮影に使用します</string>
<key>NSPhotoLibraryUsageDescription</key>
<string>ファイルアップロード用の写真選択に使用します</string>
```

## 📱 アプリアイコン要件

### アイコンサイズ（すべて必須）
- **iPhone**: 60pt (120px, 180px)
- **iPad**: 76pt (152px, 228px)
- **App Store**: 1024pt (1024px)

### デザインガイドライン
- **角丸なし**（iOSが自動適用）
- **透明背景なし**
- **テキストなし**
- **シンプルで認識しやすいデザイン**

## 📸 スクリーンショット要件

### iPhone (必須)
- **6.7"**: 1290×2796 px
- **6.5"**: 1242×2688 px
- **5.5"**: 1242×2208 px

### iPad (推奨)
- **12.9"**: 2048×2732 px
- **11"**: 1668×2388 px

## 📤 提出プロセス

### 1. Archive作成
```bash
# Xcode でアーカイブ
# Product > Archive
# Organizer > Distribute App > App Store Connect
```

### 2. App Store Connect
1. https://appstoreconnect.apple.com/ にログイン
2. 「マイApp」> 「新規App」
3. アプリ情報入力
4. ビルドをアップロード
5. 審査用情報入力

### 3. 審査準備
- **プライバシーポリシー**: 必須URL
- **サポートURL**: 問い合わせ先
- **審査メモ**: テストアカウント等

## 🔍 審査プロセス

### タイムライン
- **準備中**: 24時間以内
- **審査中**: 24-48時間
- **承認**: 即座に公開可能
- **リジェクト**: 修正後再提出

### よくあるリジェクト理由
- **機能不足**: 基本機能が動作しない
- **クラッシュ**: アプリが起動しない
- **ガイドライン違反**: UI/UXガイドライン
- **メタデータ**: 説明文とアプリ内容の不一致

## 🔄 更新プロセス

```bash
# バージョンアップ
cd flet_app
flet build ipa --release \
    --build-name=1.0.1 \
    --build-number=2

# App Store Connect で新バージョン作成
# 新しいビルドをアップロード
```

## ⚠️ 重要事項

### 証明書管理
- **開発証明書**: 1年有効
- **配布証明書**: 1年有効  
- **プロビジョニングプロファイル**: 定期更新必要

### コンプライアンス
- **輸出コンプライアンス**: 暗号化使用の申告
- **広告識別子**: 使用していない場合は「いいえ」
- **第三者コンテンツ**: オープンソースライセンス記載

### 費用
- **Developer Program**: $99/年
- **App Store 手数料**: 売上の30%（無料アプリは0%）