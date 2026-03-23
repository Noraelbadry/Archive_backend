from pydantic import BaseModel, EmailStr
from typing import Optional

class ContactCreate(BaseModel):
    sender_name:  str
    sender_email: EmailStr
    message:      str

class ContactResponse(BaseModel):
    message_id:  int
    sender_name: str

    class Config:
        from_attributes = True