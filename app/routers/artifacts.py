from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db
from app.models.artifact import Artifact
from app.models.part import ArtifactPart

router = APIRouter(prefix="/artifacts", tags=["Artifacts"])

# GET all artifacts — homepage
@router.get("/")
async def get_all_artifacts(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Artifact).where(Artifact.is_active == True)
    )
    artifacts = result.scalars().all()
    return artifacts  # ← THIS WAS MISSING

# GET one artifact — detail page
@router.get("/{artifact_id}")
async def get_artifact(artifact_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Artifact).where(Artifact.artifact_id == artifact_id)
    )
    artifact = result.scalar_one_or_none()
    if not artifact:
        raise HTTPException(status_code=404, detail="Artifact not found")
    return artifact  # ← THIS WAS MISSING

# GET parts only
@router.get("/{artifact_id}/parts")
async def get_artifact_parts(artifact_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(ArtifactPart).where(
            ArtifactPart.artifact_id == artifact_id,
            ArtifactPart.is_active == True
        ).order_by(ArtifactPart.sort_order)
    )
    return result.scalars().all()


