from sqlalchemy import (
    Column, Integer, SmallInteger, BigInteger, String, Text, Boolean, DateTime, ForeignKey
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base
    
    class AudioFile(Base):
    __tablename__ = "audio_files"

    audio_id      = Column(Integer, primary_key=True, index=True)
    narrative_id  = Column(Integer, ForeignKey("narratives.narrative_id", ondelete="CASCADE"), nullable=False)
    file_path     = Column(String(500), nullable=False)
    tts_engine    = Column(String(100))
    voice_id      = Column(String(100))
    is_primary    = Column(Boolean, default=False)

    narrative = relationship("Narrative", back_populates="audio_files")
    scan_sessions = relationship("ScanSession", back_populates="audio_file")