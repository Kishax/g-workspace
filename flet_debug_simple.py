import flet as ft

def main(page: ft.Page):
    page.title = "Flet Debug Test"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # デバッグ出力
    print("🔍 Flet app started!")
    print(f"🔍 Page size: {page.window_width}x{page.window_height}")
    
    def button_click(e):
        print("🔍 Button clicked!")
        text.value = f"Hello from Flet! Clicked {counter.value} times"
        counter.value += 1
        page.update()
    
    counter = ft.Text("0", visible=False)
    text = ft.Text("Welcome to Flet Debug Test")
    button = ft.ElevatedButton("Click me!", on_click=button_click)
    
    page.add(
        ft.Column([
            ft.Text("🚀 Flet Debug Test App", size=30, weight=ft.FontWeight.BOLD),
            text,
            button,
            counter
        ])
    )

if __name__ == "__main__":
    print("🔍 Starting Flet app...")
    # Webモードで起動（実機テスト可能）
    ft.app(target=main, view=ft.WEB_BROWSER, port=8080)
    print("🔍 Flet app finished.")