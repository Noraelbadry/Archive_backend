from sqlalchemy import (
    Column, Integer, SmallInteger, BigInteger, String, Text, Boolean, DateTime, ForeignKey
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base

class ScanSession(Base):
    __tablename__ = "scan_sessions"

    session_id     = Column(BigInteger, primary_key=True, index=True)
    artifact_id    = Column(Integer, ForeignKey("artifacts.artifact_id"), nullable=False)
    narrative_id   = Column(Integer, ForeignKey("narratives.narrative_id"), nullable=True)
    audio_id       = Column(Integer, ForeignKey("audio_files.audio_id"), nullable=True)
    visitor_token  = Column(String(64))
    device_type    = Column(String(50))
    browser        = Column(String(100))
    emotion_chosen = Column(emotion_enum)
    duration_sec   = Column(SmallInteger)
    scanned_at     = Column(DateTime, server_default=func.now())

    artifact   = relationship("Artifact", back_populates="scan_sessions")
    narrative  = relationship("Narrative", back_populates="scan_sessions")
    audio_file = relationship("AudioFile", back_populates="scan_sessions")
    
    
