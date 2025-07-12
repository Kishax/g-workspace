from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    kid: str
    username: str
    email: str
    avatar_url: Optional[str] = None

class UserCreate(UserBase):
    discord_id: str

class UserResponse(UserBase):
    id: int
    discord_id: str
    is_verified_maintainer: bool
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str