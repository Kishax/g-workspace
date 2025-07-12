import streamlit as st
import requests
from datetime import datetime
import pandas as pd

# 設定
API_BASE_URL = "http://localhost:8000/api"

st.set_page_config(
    page_title="Kishax G Project Admin",
    page_icon="🔧",
    layout="wide"
)

def main():
    st.title("🔧 Kishax G Project 管理画面")
    
    # サイドバー
    st.sidebar.title("メニュー")
    page = st.sidebar.selectbox(
        "ページを選択",
        ["ダッシュボード", "メール管理", "ファイル管理", "サーバー管理", "ユーザー管理"]
    )
    
    if page == "ダッシュボード":
        show_dashboard()
    elif page == "メール管理":
        show_mail_management()
    elif page == "ファイル管理":
        show_file_management()
    elif page == "サーバー管理":
        show_server_management()
    elif page == "ユーザー管理":
        show_user_management()

def show_dashboard():
    """ダッシュボード表示"""
    st.header("📊 ダッシュボード")
    
    # メトリクス表示
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("総メール数", "1,234", "12")
    
    with col2:
        st.metric("アクティブユーザー", "23", "2")
    
    with col3:
        st.metric("サーバー稼働率", "99.9%", "0.1%")
    
    with col4:
        st.metric("ストレージ使用量", "45GB", "2GB")
    
    # グラフ表示
    st.subheader("📈 メール送信統計")
    
    # サンプルデータ
    chart_data = pd.DataFrame({
        'day': pd.date_range('2025-07-01', periods=30),
        'emails': [10, 15, 12, 8, 20, 25, 18, 22, 16, 14] * 3
    })
    
    st.line_chart(chart_data.set_index('day'))

def show_mail_management():
    """メール管理画面"""
    st.header("📧 メール管理")
    
    # メール一覧
    st.subheader("受信メール")
    
    # APIからデータ取得（実際の実装）
    mails = get_mails_from_api()
    
    if mails:
        df = pd.DataFrame(mails)
        st.dataframe(df)
    else:
        st.info("メールがありません")
    
    # メール送信フォーム
    st.subheader("メール送信")
    
    with st.form("send_mail_form"):
        to_email = st.text_input("宛先")
        subject = st.text_input("件名")
        body = st.text_area("本文")
        
        if st.form_submit_button("送信"):
            if to_email and subject and body:
                send_mail_via_api(to_email, subject, body)
                st.success("メールを送信しました")
            else:
                st.error("すべてのフィールドを入力してください")

def show_file_management():
    """ファイル管理画面"""
    st.header("📁 ファイル管理")
    st.info("ファイル管理機能は実装予定です")

def show_server_management():
    """サーバー管理画面"""
    st.header("🖥️ サーバー管理")
    st.info("サーバー管理機能は実装予定です")

def show_user_management():
    """ユーザー管理画面"""
    st.header("👥 ユーザー管理")
    st.info("ユーザー管理機能は実装予定です")

def get_mails_from_api():
    """API からメール一覧を取得"""
    try:
        response = requests.get(f"{API_BASE_URL}/mails/")
        if response.status_code == 200:
            return response.json()["mails"]
        return []
    except:
        return []

def send_mail_via_api(to_email, subject, body):
    """API でメール送信"""
    try:
        response = requests.post(
            f"{API_BASE_URL}/mails/send",
            json={
                "to": to_email,
                "subject": subject,
                "body": body
            }
        )
        return response.status_code == 200
    except:
        return False

if __name__ == "__main__":
    main()