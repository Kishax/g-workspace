import flet as ft


class MailView(ft.UserControl):
  def __init__(self, page):
    super().__init__()
    self.page = page
    self.mail_list = []

  def build(self):
    return ft.Container(
      content=ft.Column(
        [
          ft.Text("📧 メール管理", size=24, weight=ft.FontWeight.BOLD),
          ft.Divider(),
          # メール送信フォーム
          ft.ExpansionTile(
            title=ft.Text("新規メール作成"),
            leading=ft.Icon(ft.icons.CREATE),
            controls=[
              ft.Container(
                content=ft.Column(
                  [
                    ft.TextField(label="宛先", hint_text="example@example.com"),
                    ft.TextField(label="件名"),
                    ft.TextField(
                      label="本文", multiline=True, min_lines=5, max_lines=10
                    ),
                    ft.Row(
                      [
                        ft.ElevatedButton(
                          "送信", icon=ft.icons.SEND, on_click=self.send_mail
                        ),
                        ft.OutlinedButton("下書き保存", icon=ft.icons.SAVE),
                      ],
                      alignment=ft.MainAxisAlignment.END,
                    ),
                  ]
                ),
                padding=10,
              )
            ],
          ),
          ft.Divider(),
          # メール一覧
          ft.Text("受信メール", size=18, weight=ft.FontWeight.BOLD),
          ft.Container(
            content=ft.Column(
              [
                self.create_mail_item(
                  "john@example.com",
                  "会議の件",
                  "来週の会議についてご連絡いたします...",
                  "2025-07-12 10:30",
                ),
                self.create_mail_item(
                  "alice@example.com",
                  "プロジェクト進捗",
                  "プロジェクトの進捗状況を報告します...",
                  "2025-07-12 09:15",
                ),
                self.create_mail_item(
                  "bob@example.com",
                  "お疲れさまです",
                  "いつもお疲れさまです。今日は...",
                  "2025-07-11 18:45",
                ),
              ],
              scroll=ft.ScrollMode.AUTO,
            ),
            height=400,
            border=ft.border.all(1, ft.colors.OUTLINE),
            border_radius=10,
          ),
        ],
        scroll=ft.ScrollMode.AUTO,
      ),
      padding=20,
      expand=True,
    )

  def create_mail_item(self, sender, subject, preview, time):
    return ft.Container(
      content=ft.ListTile(
        leading=ft.CircleAvatar(
          content=ft.Text(sender[0].upper()), bgcolor=ft.colors.PRIMARY
        ),
        title=ft.Text(subject, weight=ft.FontWeight.BOLD),
        subtitle=ft.Column(
          [
            ft.Text(f"From: {sender}", size=12),
            ft.Text(preview, size=12, max_lines=1),
            ft.Text(time, size=10, color=ft.colors.ON_SURFACE_VARIANT),
          ],
          spacing=2,
        ),
        on_click=self.open_mail,
      ),
      border=ft.border.only(bottom=ft.BorderSide(1, ft.colors.OUTLINE_VARIANT)),
      padding=ft.padding.symmetric(vertical=5),
    )

  def send_mail(self, e):
    # TODO: メール送信実装
    self.page.show_snack_bar(ft.SnackBar(content=ft.Text("メールを送信しました")))

  def open_mail(self, e):
    # TODO: メール詳細表示実装
    self.page.show_snack_bar(
      ft.SnackBar(content=ft.Text("メール詳細画面は実装予定です"))
    )
