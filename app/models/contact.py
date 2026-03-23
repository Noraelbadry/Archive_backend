from sqlalchemy import Column, Integer, String, Text, Boolean, TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base

class ContactMessage(Base):
    __tablename__ = "contact_messages"
    __table_args__ = {"schema": "public"}

    message_id   = Column(Integer, primary_key=True, autoincrement=True)
    sender_name  = Column(String(150), nullable=False)
    sender_email = Column(String(200), nullable=False)
    message      = Column(Text, nullable=False)
    is_read      = Column(Boolean, default=False)
    is_replied   = Column(Boolean, default=False)
    reply_text   = Column(Text)
    ip_address   = Column(String(45))
    submitted_at = Column(TIMESTAMP, server_default=func.now())
    replied_at   = Column(TIMESTAMP, server_default=func.now())