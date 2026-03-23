from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models.contact import ContactMessage
from app.schemas.contact import ContactCreate, ContactResponse

router = APIRouter(prefix="/contact", tags=["Contact"])

@router.post("/", response_model=ContactResponse)
async def send_message(
    payload: ContactCreate,
    request: Request,
    db: AsyncSession = Depends(get_db)
):
    new_message = ContactMessage(
        sender_name  = payload.sender_name,
        sender_email = payload.sender_email,
        message      = payload.message,
        ip_address   = request.client.host
    )
    db.add(new_message)
    await db.commit()
    await db.refresh(new_message)
    return new_message