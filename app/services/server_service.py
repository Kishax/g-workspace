from sqlalchemy.orm import Session
from app.models.server import Server

class ServerService:
    @staticmethod
    async def get_servers(db: Session):
        """サーバー一覧取得"""
        # TODO: サーバー一覧取得実装
        pass
    
    @staticmethod
    async def get_server(server_id: int, db: Session):
        """サーバー詳細取得"""
        # TODO: サーバー詳細取得実装
        pass
    
    @staticmethod
    async def ping_server(server_id: int, db: Session):
        """サーバーPing実行"""
        # TODO: サーバーPing実装
        pass