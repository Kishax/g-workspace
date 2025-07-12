# Google Play Store 配布設定

## 📋 必要な準備

### 1. Google Play Console アカウント
- **登録料**: $25 (一回限り)
- **登録URL**: https://play.google.com/console/

### 2. アプリ署名証明書の作成
```bash
# キーストア作成
keytool -genkey -v -keystore kishax-g-release-key.keystore \
    -alias kishax-g-key \
    -keyalg RSA \
    -keysize 2048 \
    -validity 10000

# 証明書情報をメモ
# - キーストアパスワード
# - キーエイリアス: kishax-g-key
# - キーパスワード
```

### 3. リリース用APK作成
```bash
# プロジェクトルートで実行
cd flet_app

# リリース用署名APK作成
flet build apk --release \
    --build-name=1.0.0 \
    --build-number=1
```

## 📝 アプリ情報設定

### アプリ基本情報
- **アプリ名**: Kishax G - Workspace Alternative
- **短い説明**: Google Workspace代替のオープンソース生産性アプリ
- **完全な説明**: 

```
Kishax Gは、Google Workspaceの機能を統合したオープンソースの生産性向上アプリです。

🚀 主な機能:
• メール管理 - 複数アカウント対応
• ファイル管理 - クラウドストレージ統合
• ダッシュボード - 一元管理画面
• AI統合 - スパム検出と分析
• セキュア認証 - Discord OAuth2

🌐 クロスプラットフォーム:
Pythonベースで開発され、Web、モバイル、デスクトップで統一体験を提供します。

🔒 プライバシー重視:
オープンソースで透明性を保ち、ユーザーデータの完全制御を実現します。
```

### カテゴリ
- **カテゴリ**: 仕事効率化
- **タグ**: productivity, workspace, email, files, opensource

### スクリーンショット要件
- **携帯電話**: 最低2枚、最大8枚
- **7インチタブレット**: 最低1枚、最大5枚  
- **10インチタブレット**: 最低1枚、最大5枚
- **サイズ**: JPGまたはPNG、24ビット、アルファチャンネルなし

## 🛠️ ビルド設定

### android/app/build.gradle
```gradle
android {
    compileSdkVersion 34
    
    defaultConfig {
        applicationId "com.kishax.g_workspace"
        minSdkVersion 21
        targetSdkVersion 34
        versionCode 1
        versionName "1.0.0"
    }
    
    signingConfigs {
        release {
            keyAlias 'kishax-g-key'
            keyPassword 'YOUR_KEY_PASSWORD'
            storeFile file('kishax-g-release-key.keystore')
            storePassword 'YOUR_KEYSTORE_PASSWORD'
        }
    }
    
    buildTypes {
        release {
            signingConfig signingConfigs.release
            minifyEnabled true
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        }
    }
}
```

## 📤 アップロード手順

### 1. APKテスト
```bash
# APKをデバイスでテスト
adb install flet_app/build/apk/app-release.apk
```

### 2. Play Console アップロード
1. https://play.google.com/console/ にログイン
2. 「アプリを作成」をクリック
3. アプリ情報を入力
4. APKをアップロード（内部テスト → 審査 → 本番）

### 3. 審査プロセス
- **内部テスト**: 即座に利用可能
- **審査期間**: 通常1-3日
- **本番公開**: 審査通過後24時間以内

## 🔄 更新プロセス

```bash
# バージョンアップ
cd flet_app
flet build apk --release \
    --build-name=1.0.1 \
    --build-number=2

# Play Console で新バージョンをアップロード
```

## ⚠️ 注意事項

- **キーストアファイルは絶対に紛失しないこと**（更新不可能になる）
- **パスワードを安全に保管**
- **初回審査は時間がかかる場合がある**
- **ポリシー違反に注意**（プライバシーポリシー必須）