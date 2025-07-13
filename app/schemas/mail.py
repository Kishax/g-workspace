from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Any


class MailBase(BaseModel):
  to_address: str
  subject: str
  body: str
  html_body: Optional[str] = None


class MailCreate(MailBase):
  attachments: Optional[List[Any]] = []


class MailResponse(MailBase):
  id: int
  kid: int
  from_address: str
  attachments: Optional[List[Any]] = []
  sent_at: datetime
  received_at: Optional[datetime] = None
  status: str
  is_read: bool
  folder: str
  spam_score: int

  class Config:
    from_attributes = True


class MailListResponse(BaseModel):
  mails: List[MailResponse]
  total: int
  page: int
  limit: int
