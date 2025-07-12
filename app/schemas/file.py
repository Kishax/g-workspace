from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FileBase(BaseModel):
    filename: str
    is_public: bool = False

class FileCreate(FileBase):
    original_filename: str
    file_size: int
    content_type: str

class FileResponse(FileBase):
    id: int
    kid: int
    original_filename: str
    file_path: str
    file_size: int
    content_type: str
    s3_key: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True