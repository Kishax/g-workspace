# Git-Flow開発用Makefile
# 使い方: make <コマンド名>

.PHONY: help setup status branch-list

# デフォルト: ヘルプを表示
help:
	@echo "=== Git-Flow開発用コマンド ==="
	@echo "setup        : 初期設定（pullの動作をrebaseに設定）"
	@echo "status       : 現在の状況確認"
	@echo "sync         : developブランチを最新に同期"
	@echo "new-feature  : 新しいfeatureブランチを作成（NAME=ブランチ名）"
	@echo "new-fix      : 新しいfixブランチを作成（NAME=ブランチ名）"
	@echo "commit       : コミット実行（MSG=メッセージ）"
	@echo "push         : 現在のブランチをpush"
	@echo "pr-ready     : PR用の最終確認"
	@echo "cleanup      : マージ済みブランチの削除"
	@echo "emergency    : developブランチをリモートから強制復元"
	@echo ""
	@echo "=== Fletデバッグコマンド ==="
	@echo "flet-debug   : Fletアプリをデスクトップモードで起動"
	@echo "flet-web     : Fletアプリをブラウザモードで起動（実機テスト可能）"
	@echo "flet-simple  : シンプルなデバッグテスト"
	@echo ""
	@echo "=== Fletビルドコマンド ==="
	@echo "build-android   : Android APKビルド"
	@echo "build-ios       : iOS IPAビルド (macOSのみ)"
	@echo "build-macos     : macOS APPビルド (macOSのみ)"
	@echo "build-windows   : Windows EXEビルド (Windowsのみ)"
	@echo "build-linux     : Linux AppImageビルド"
	@echo "build-web       : Web PWAビルド"
	@echo "build-check     : ビルド環境チェック"
	@echo ""
	@echo "=== 配布・リリースコマンド ==="
	@echo "release         : 現在環境でリリースビルド"
	@echo "package-current : 現在環境用パッケージ作成"
	@echo "create-tag      : リリースタグ作成 (VERSION=v1.0.0)"
	@echo "release-status  : リリース状況確認"
	@echo ""
	@echo "=== 実行コマンド ==="
	@echo "run-linux       : Linux実行ファイルを起動"
	@echo "run-web         : Web PWAをローカルサーバーで起動"
	@echo "build-run-linux : ビルド→Linux実行"
	@echo "build-run-web   : ビルド→Web実行"
	@echo ""
	@echo "=== 使用例 ==="
	@echo "make new-feature NAME=user-login"
	@echo "make commit MSG=\"feat: ユーザーログイン機能を追加\""
	@echo "make new-fix NAME=issue-123"
	@echo "make flet-web  # 実機でhttp://localhost:8080にアクセス"

# 初期設定
setup:
	@echo "🔧 Git設定を初期化中..."
	git config pull.rebase true
	git config --global init.defaultBranch main
	@echo "✅ 設定完了！pullは自動的にrebaseされます"

# 現在の状況確認
status:
	@echo "📊 現在の状況"
	@echo "ブランチ:"
	git branch -v
	@echo ""
	@echo "ステータス:"
	git status --short
	@echo ""
	@echo "最新3コミット:"
	git log --oneline -3

# ブランチ一覧表示
branch-list:
	@echo "📋 全ブランチ一覧"
	@echo "ローカル:"
	git branch
	@echo ""
	@echo "リモート:"
	git branch -r

# developブランチを最新に同期
sync:
	@echo "🔄 developブランチを最新に同期中..."
	git checkout develop
	git fetch origin
	git pull --rebase origin develop
	@echo "✅ developブランチが最新になりました"

# developブランチの完全同期
sync-force:
	@echo "🔄 developブランチを完全同期中..."
	git checkout develop
	git fetch origin
	git reset --hard origin/develop
	@echo "✅ developブランチがリモートと同期しました"

# 新しいfeatureブランチを作成
new-feature:
	@if [ -z "$(NAME)" ]; then \
		echo "❌ エラー: NAME=ブランチ名 を指定してください"; \
		echo "例: make new-feature NAME=user-login"; \
		exit 1; \
	fi
	@echo "🌟 新しいfeatureブランチを作成中..."
	git checkout develop
	git pull --rebase origin develop
	git checkout -b feature/$(NAME)
	@echo "✅ feature/$(NAME) ブランチを作成しました"

# 新しいfixブランチを作成
new-fix:
	@if [ -z "$(NAME)" ]; then \
		echo "❌ エラー: NAME=ブランチ名 を指定してください"; \
		echo "例: make new-fix NAME=issue-123"; \
		exit 1; \
	fi
	@echo "🔧 新しいfixブランチを作成中..."
	git checkout develop
	git pull --rebase origin develop
	git checkout -b fix/$(NAME)
	@echo "✅ fix/$(NAME) ブランチを作成しました"

# コミット実行（Git-Flow規約に従う）
commit:
	@if [ -z "$(MSG)" ]; then \
		echo "❌ エラー: MSG=\"メッセージ\" を指定してください"; \
		echo "例: make commit MSG=\"feat: 新機能を追加\""; \
		echo ""; \
		echo "📝 コミットメッセージの形式:"; \
		echo "feat: 新機能"; \
		echo "fix: バグ修正"; \
		echo "update: 更新"; \
		echo "docs: ドキュメント"; \
		echo "style: コードスタイル"; \
		echo "refactor: リファクタリング"; \
		echo "test: テスト"; \
		echo "chore: その他"; \
		exit 1; \
	fi
	@echo "💾 コミット実行中..."
	git add .
	git commit -m "$(MSG)"
	@echo "✅ コミット完了: $(MSG)"

# 現在のブランチをpush
push:
	@echo "📤 現在のブランチをpush中..."
	@BRANCH=$$(git branch --show-current); \
	git push -u origin $$BRANCH
	@echo "✅ pushが完了しました"

# PR用の最終確認
pr-ready:
	@echo "🔍 PR作成前の最終確認"
	@echo ""
	@echo "現在のブランチ:"
	@BRANCH=$$(git branch --show-current); echo "  $$BRANCH"
	@echo ""
	@echo "コミット履歴:"
	git log --oneline origin/develop..HEAD
	@echo ""
	@echo "変更ファイル:"
	git diff --name-status origin/develop..HEAD
	@echo ""
	@echo "✅ 確認完了！GitHub上でPRを作成してください"

# 作業ディレクトリのクリーンアップ
clean:
	@echo "🧹 作業ディレクトリをクリーンアップ中..."
	git clean -fd
	git reset --hard HEAD
	@echo "✅ クリーンアップ完了"

# マージ済みブランチの削除
cleanup:
	@echo "🗑️  マージ済みブランチを削除中..."
	git checkout develop
	git branch --merged | grep -v 'develop\|main' | xargs -n 1 git branch -d || true
	@echo "✅ ローカルブランチのクリーンアップ完了"

# 緊急時: developブランチをリモートから強制復元
emergency:
	@echo "🚨 緊急復元: developブランチをリモートから復元中..."
	@echo "警告: ローカルの変更は全て失われます！"
	@read -p "続行しますか？ (y/N): " confirm; \
	if [ "$$confirm" = "y" ] || [ "$$confirm" = "Y" ]; then \
		git fetch origin; \
		git checkout develop; \
		git reset --hard origin/develop; \
		echo "✅ developブランチを復元しました"; \
	else \
		echo "❌ キャンセルしました"; \
	fi

# git pull時の競合解決
fix-divergent:
	@echo "🔧 分岐したブランチを修正中..."
	git pull --rebase origin $$(git branch --show-current)
	@echo "✅ リベースが完了しました"

# リモートブランチの情報更新
fetch:
	@echo "📡 リモートブランチ情報を更新中..."
	git fetch --all --prune
	@echo "✅ リモート情報を更新しました"

# streamlit 管理画面起動
stream-web:
	@echo "📊 Streamlit 管理画面を起動中..."
	@echo "🌐 ブラウザで http://localhost:8501 にアクセス"
	streamlit run streamlit_app/main.py

# Fletデバッグ関連コマンド
flet-debug:
	@echo "🐛 Fletアプリをデスクトップモードでデバッグ起動中..."
	python flet_app/main.py

flet-web:
	@echo "🌐 Fletアプリをブラウザモードでデバッグ起動中..."
	@echo "📱 実機テスト: http://localhost:8080 にアクセス"
	python -c "import flet as ft; from flet_app.main import main; ft.app(target=main, view=ft.WEB_BROWSER, port=8080)"

flet-simple:
	@echo "🔍 Fletシンプルデバッグテスト起動中..."
	@echo "📱 実機テスト: http://localhost:8080 にアクセス"
	python flet_debug_simple.py

# Fletクロスプラットフォームビルドコマンド
build-android:
	@echo "📱 Android APKをビルド中..."
	@echo "📋 要件: Android Studio, Android SDK"
	@echo "❌ 現在のFletバージョンではサポートされていません"
	@echo "代替案: flet publish でWebアプリとして配布"

build-ios:
	@echo "📱 iOS IPAをビルド中..."
	@echo "📋 要件: macOS, Xcode"
	@echo "❌ 現在のFletバージョンではサポートされていません"
	@echo "代替案: flet publish でWebアプリとして配布"

build-macos:
	@echo "🖥️ macOS APPをビルド中..."
	@echo "📋 要件: macOS"
	cd flet_app && flet pack main.py --name "Kishax-G" --verbose

build-windows:
	@echo "🖥️ Windows EXEをビルド中..."
	@echo "📋 要件: Windows"
	cd flet_app && flet pack main.py --name "Kishax-G" --verbose

build-linux:
	@echo "🐧 Linux実行ファイルをビルド中..."
	cd flet_app && flet pack main.py --name "Kishax-G" --verbose

build-web:
	@echo "🌐 Web PWAをビルド中..."
	cd flet_app && flet publish main.py --verbose

# 全プラットフォーム対応状況確認
build-check:
	@echo "🔍 ビルド環境チェック中..."
	@echo ""
	@echo "=== Fletインストール状況 ==="
	@flet --version || echo "❌ Fletがインストールされていません: pip install flet"
	@echo ""
	@echo "=== プラットフォーム別要件 ==="
	@echo "📱 Android: Android Studio + Android SDK"
	@echo "📱 iOS: macOS + Xcode (macOSのみ)"
	@echo "🖥️ macOS: macOS環境"
	@echo "🖥️ Windows: Windows環境"
	@echo "🐧 Linux: 現在の環境で利用可能"
	@echo "🌐 Web: 全環境で利用可能"
	@echo ""
	@echo "📋 現在の環境:"
	@uname -s

# 配布用リリースコマンド
release:
	@echo "🚀 全プラットフォーム向けリリースビルド開始..."
	@echo "📋 注意: 各プラットフォーム固有の環境が必要です"
	@echo ""
	@$(MAKE) build-check
	@echo ""
	@echo "🏗️ 現在の環境で可能なビルドを実行中..."
	@$(MAKE) build-linux build-web
	@echo ""
	@echo "✅ リリースビルド完了！"
	@echo "📦 出力先:"
	@echo "   - Linux: flet_app/build/linux/"
	@echo "   - Web:   flet_app/build/web/"
	@echo ""
	@echo "🌐 GitHub Actions で全プラットフォームビルド:"
	@echo "   git tag v1.0.0 && git push origin v1.0.0"

# 現在の環境用パッケージ作成
package-current:
	@echo "📦 現在の環境用パッケージ作成中..."
	@OS=$$(uname -s); \
	case $$OS in \
		Linux) $(MAKE) build-linux build-web ;; \
		Darwin) $(MAKE) build-macos build-ios build-web ;; \
		MINGW*|CYGWIN*|MSYS*) $(MAKE) build-windows build-web ;; \
		*) echo "❌ 未対応の環境: $$OS" ;; \
	esac
	@echo "✅ パッケージ作成完了！"

# 全プラットフォームパッケージ作成（GitHub Actions用）
package-all:
	@echo "📦 全プラットフォームパッケージ作成..."
	@echo "⚠️ このコマンドはGitHub Actionsで実行されます"
	@echo ""
	@echo "手動実行する場合:"
	@echo "1. git tag v1.0.0"
	@echo "2. git push origin v1.0.0"
	@echo "3. GitHub Actions が自動実行されます"

# リリースタグ作成
create-tag:
	@if [ -z "$(VERSION)" ]; then \
		echo "❌ エラー: VERSION=バージョン を指定してください"; \
		echo "例: make create-tag VERSION=v1.0.0"; \
		exit 1; \
	fi
	@echo "🏷️ リリースタグ作成中: $(VERSION)"
	git tag $(VERSION)
	git push origin $(VERSION)
	@echo "✅ タグ作成完了！GitHub Actions でビルドが開始されます"
	@echo "📊 進行状況: https://github.com/Kishax/g-workspace/actions"

# リリース状況確認
release-status:
	@echo "📊 最新リリース状況確認..."
	@echo ""
	@echo "=== 最新タグ ==="
	@git tag --sort=-version:refname | head -5 || echo "タグなし"
	@echo ""
	@echo "=== GitHub Actions ==="
	@echo "🔗 https://github.com/Kishax/g-workspace/actions"
	@echo ""
	@echo "=== リリースページ ==="
	@echo "🔗 https://github.com/Kishax/g-workspace/releases"

# ビルドファイル実行コマンド
run-linux:
	@echo "🐧 Linux実行ファイルを起動中..."
	@if [ -f "flet_app/dist/Kishax-G" ]; then \
		echo "✅ 実行ファイルが見つかりました"; \
		cd flet_app/dist && ./Kishax-G; \
	else \
		echo "❌ 実行ファイルが見つかりません"; \
		echo "💡 まず make build-linux を実行してください"; \
	fi

run-web:
	@echo "🌐 Web PWAをローカルサーバーで起動中..."
	@if [ -f "flet_app/dist/index.html" ]; then \
		echo "✅ Webファイルが見つかりました"; \
		echo "📱 ブラウザで http://localhost:8080 にアクセスしてください"; \
		cd flet_app && python -m http.server 8080 --directory dist; \
	else \
		echo "❌ Webファイルが見つかりません"; \
		echo "💡 まず make build-web を実行してください"; \
	fi

# ビルド＋実行の一連コマンド
build-run-linux:
	@echo "🔄 Linux: ビルド → 実行"
	@$(MAKE) build-linux
	@$(MAKE) run-linux

build-run-web:
	@echo "🔄 Web: ビルド → 実行"
	@$(MAKE) build-web
	@$(MAKE) run-web

# 開発フロー確認
workflow:
	@echo "📋 Git-Flow開発フロー"
	@echo ""
	@echo "1️⃣  新機能開発:"
	@echo "   make new-feature NAME=機能名"
	@echo "   # 開発作業"
	@echo "   make commit MSG=\"feat: 機能の説明\""
	@echo "   make push"
	@echo "   # GitHub上でPR作成"
	@echo ""
	@echo "2️⃣  バグ修正:"
	@echo "   make new-fix NAME=issue番号"
	@echo "   # 修正作業"
	@echo "   make commit MSG=\"fix: 修正内容\""
	@echo "   make push"
	@echo "   # GitHub上でPR作成"
	@echo ""
	@echo "3️⃣  定期メンテナンス:"
	@echo "   make sync          # developを最新に"
	@echo "   make cleanup       # 不要ブランチ削除"
	@echo "   make fetch         # リモート情報更新"
