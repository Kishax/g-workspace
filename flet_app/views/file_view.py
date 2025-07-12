import flet as ft

class FileView(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.files = []
    
    def build(self):
        return ft.Container(
            content=ft.Column([
                ft.Text("📁 ファイル管理", size=24, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                
                # ファイルアップロード
                ft.Row([
                    ft.ElevatedButton(
                        "ファイルアップロード",
                        icon=ft.icons.UPLOAD_FILE,
                        on_click=self.upload_file
                    ),
                    ft.OutlinedButton(
                        "フォルダ作成",
                        icon=ft.icons.CREATE_NEW_FOLDER
                    ),
                ]),
                
                ft.Divider(),
                
                # ファイル一覧
                ft.Text("ファイル一覧", size=18, weight=ft.FontWeight.BOLD),
                ft.Container(
                    content=ft.Column([
                        self.create_file_item("📄 document.pdf", "2.5 MB", "2025-07-12 10:30"),
                        self.create_file_item("📊 report.xlsx", "1.2 MB", "2025-07-11 15:20"),
                        self.create_file_item("🖼️ image.png", "450 KB", "2025-07-10 09:15"),
                        self.create_file_item("📝 readme.txt", "15 KB", "2025-07-09 14:45"),
                    ], scroll=ft.ScrollMode.AUTO),
                    height=400,
                    border=ft.border.all(1, ft.colors.OUTLINE),
                    border_radius=10,
                )
            ], scroll=ft.ScrollMode.AUTO),
            padding=20,
            expand=True
        )
    
    def create_file_item(self, name, size, date):
        return ft.Container(
            content=ft.ListTile(
                title=ft.Text(name),
                subtitle=ft.Text(f"{size} • {date}"),
                trailing=ft.Row([
                    ft.IconButton(
                        icon=ft.icons.DOWNLOAD,
                        tooltip="ダウンロード",
                        on_click=self.download_file
                    ),
                    ft.IconButton(
                        icon=ft.icons.DELETE,
                        tooltip="削除",
                        on_click=self.delete_file
                    ),
                ], tight=True),
                on_click=self.open_file
            ),
            border=ft.border.only(bottom=ft.BorderSide(1, ft.colors.OUTLINE_VARIANT)),
            padding=ft.padding.symmetric(vertical=5)
        )
    
    def upload_file(self, e):
        # TODO: ファイルアップロード実装
        self.page.show_snack_bar(ft.SnackBar(content=ft.Text("ファイルアップロード機能は実装予定です")))
    
    def download_file(self, e):
        # TODO: ファイルダウンロード実装
        self.page.show_snack_bar(ft.SnackBar(content=ft.Text("ファイルをダウンロードしました")))
    
    def delete_file(self, e):
        # TODO: ファイル削除実装
        self.page.show_snack_bar(ft.SnackBar(content=ft.Text("ファイルを削除しました")))
    
    def open_file(self, e):
        # TODO: ファイル詳細表示実装
        self.page.show_snack_bar(ft.SnackBar(content=ft.Text("ファイル詳細画面は実装予定です")))