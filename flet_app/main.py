import flet as ft
from views.mail_view import MailView
from views.file_view import FileView
from views.dashboard_view import DashboardView


def main(page: ft.Page):
  page.title = "Kishax G Project"
  page.theme_mode = ft.ThemeMode.LIGHT
  page.padding = 0

  # ナビゲーションレール
  def on_navigation_change(e):
    selected_index = e.control.selected_index
    page.clean()

    if selected_index == 0:
      page.add(DashboardView(page))
    elif selected_index == 1:
      page.add(MailView(page))
    elif selected_index == 2:
      page.add(FileView(page))

    page.update()

  # 初期画面設定
  navigation_rail = ft.NavigationRail(
    selected_index=0,
    label_type=ft.NavigationRailLabelType.ALL,
    min_width=100,
    min_extended_width=200,
    destinations=[
      ft.NavigationRailDestination(
        icon=ft.icons.DASHBOARD,
        selected_icon=ft.icons.DASHBOARD,
        label="ダッシュボード",
      ),
      ft.NavigationRailDestination(
        icon=ft.icons.EMAIL, selected_icon=ft.icons.EMAIL, label="メール"
      ),
      ft.NavigationRailDestination(
        icon=ft.icons.FOLDER, selected_icon=ft.icons.FOLDER, label="ファイル"
      ),
    ],
    on_change=on_navigation_change,
  )

  # レイアウト
  page.add(
    ft.Row(
      [
        navigation_rail,
        ft.VerticalDivider(width=1),
        ft.Column(
          [DashboardView(page)], alignment=ft.MainAxisAlignment.START, expand=True
        ),
      ],
      expand=True,
    )
  )


if __name__ == "__main__":
  ft.app(target=main)
