from pydantic import BaseModel
from typing import Optional

class ArtifactResponse(BaseModel):
    artifact_id:   int
    museum_id:     Optional[int]
    name:          str
    origin:        Optional[str]
    period:        Optional[str]
    material:      Optional[str]
    description:   Optional[str]
  

    class Config:
        from_attributes = True