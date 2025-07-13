import flet as ft


class DashboardView(ft.UserControl):
  def __init__(self, page):
    super().__init__()
    self.page = page

  def build(self):
    return ft.Container(
      content=ft.Column(
        [
          ft.Text("📊 ダッシュボード", size=24, weight=ft.FontWeight.BOLD),
          ft.Divider(),
          # メトリクスカード
          ft.Row(
            [
              self.create_metric_card("総メール数", "1,234", "+12"),
              self.create_metric_card("アクティブユーザー", "23", "+2"),
              self.create_metric_card("サーバー稼働率", "99.9%", "+0.1%"),
              self.create_metric_card("ストレージ使用量", "45GB", "+2GB"),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
          ),
          ft.Divider(),
          ft.Text("📈 システム状況", size=18, weight=ft.FontWeight.BOLD),
          # システム状況
          ft.Container(
            content=ft.Column(
              [
                ft.ListTile(
                  leading=ft.Icon(ft.icons.CHECK_CIRCLE, color=ft.colors.GREEN),
                  title=ft.Text("API サーバー"),
                  subtitle=ft.Text("正常稼働中"),
                ),
                ft.ListTile(
                  leading=ft.Icon(ft.icons.CHECK_CIRCLE, color=ft.colors.GREEN),
                  title=ft.Text("データベース"),
                  subtitle=ft.Text("正常稼働中"),
                ),
                ft.ListTile(
                  leading=ft.Icon(ft.icons.WARNING, color=ft.colors.ORANGE),
                  title=ft.Text("メールサービス"),
                  subtitle=ft.Text("一部遅延あり"),
                ),
              ]
            ),
            bgcolor=ft.colors.SURFACE_VARIANT,
            border_radius=10,
            padding=10,
          ),
        ],
        scroll=ft.ScrollMode.AUTO,
      ),
      padding=20,
      expand=True,
    )

  def create_metric_card(self, title, value, change):
    return ft.Container(
      content=ft.Column(
        [
          ft.Text(title, size=12, color=ft.colors.ON_SURFACE_VARIANT),
          ft.Text(value, size=24, weight=ft.FontWeight.BOLD),
          ft.Text(
            change,
            size=12,
            color=ft.colors.GREEN if change.startswith("+") else ft.colors.RED,
          ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
      ),
      bgcolor=ft.colors.SURFACE_VARIANT,
      border_radius=10,
      padding=20,
      width=180,
      height=120,
    )
