from app.video.schemas import VideoInDb
from app.db import async_session_maker
from sqlalchemy import select

class VideoManager:

    async def get(self):
        async with async_session_maker() as session:
            result = await session.scalars(select(VideoInDb))
            return [user for user in result]

    async def create(self, video: VideoInDb):
        async with async_session_maker() as session:
            session.add(video)

            await session.commit()

    ## очень плохо
    async def get_by_id(self, id):
        videos = await self.get()
        video = list(filter(lambda x: x.id == id, videos))
        if len(video) == 0:
            return None
        return video[0]
