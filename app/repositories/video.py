from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.models.video import VideoResult


class VideoRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, filename: str, movement: bool) -> VideoResult:
        video = VideoResult(filename=filename, movement=movement)
        self.session.add(video)
        await self.session.commit()
        await self.session.refresh(video)
        return video

    async def get(self, video_id: int):
        stmt = select(VideoResult).where(VideoResult.id == video_id)
        return await self.session.scalar(stmt)
