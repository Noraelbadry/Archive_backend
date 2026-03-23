from sqlalchemy import Column, Integer, SmallInteger, String, Text, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class Narrative(Base):
    __tablename__ = "narratives"
    __table_args__ = {"schema": "public"}

    narrative_id   = Column(Integer, primary_key=True, autoincrement=True)
    artifact_id    = Column(Integer, ForeignKey("public.artifacts.artifact_id", ondelete="CASCADE"), nullable=False)
    language       = Column(String(10), default='en')
    emotion_tag    = Column(String(50))
    prompt_version = Column(String(50))
    llm_model      = Column(String(100))
    content        = Column(Text, nullable=False)
    word_count     = Column(SmallInteger)
    is_approved    = Column(Boolean, default=False)
    created_at     = Column(TIMESTAMP, server_default=func.now())