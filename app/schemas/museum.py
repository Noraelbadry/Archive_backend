from pydantic import BaseModel
from typing import Optional

class MuseumResponse(BaseModel):
    museum_id:    int
    name:         str
    city:         Optional[str]
    country:      Optional[str]
    founded_year: Optional[int]
    description:  Optional[str]
    website_url:  Optional[str]
    email:        Optional[str]
    

    class Config:
        from_attributes = True