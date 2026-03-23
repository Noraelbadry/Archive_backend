from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db
from app.models.museum import Museum
from app.schemas.museum import MuseumResponse

router = APIRouter(prefix="/museums", tags=["Museums"])

@router.get("/{museum_id}", response_model=MuseumResponse)
async def get_museum(museum_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Museum).where(Museum.museum_id == museum_id)
    )
    museum = result.scalar_one_or_none()
    if not museum:
        raise HTTPException(status_code=404, detail="Museum not found")
    return museum