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
	@echo "=== 使用例 ==="
	@echo "make new-feature NAME=user-login"
	@echo "make commit MSG=\"feat: ユーザーログイン機能を追加\""
	@echo "make new-fix NAME=issue-123"

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
