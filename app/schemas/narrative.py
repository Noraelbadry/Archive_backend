from pydantic import BaseModel
from typing import Optional

class NarrativeResponse(BaseModel):
    narrative_id: int
    artifact_id:  int
    language:     str
    emotion_tag:  str
    content:      str
    is_approved:  int

    class Config:
        from_attributes = True