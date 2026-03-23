from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db
from app.models.narrative import Narrative
from app.schemas.narrative import NarrativeResponse

router = APIRouter(prefix="/narratives", tags=["Narratives"])

@router.get("/{artifact_id}", response_model=list[NarrativeResponse])
async def get_narratives(artifact_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Narrative).where(
            Narrative.artifact_id == artifact_id,
            Narrative.is_approved == 1
        )
    )
    return result.scalars().all()