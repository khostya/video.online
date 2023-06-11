from app.like.schemas import VideoLike
from app.db import async_session_maker
from sqlalchemy import select


## очень плохо
class LikeManager:
    async def get(self) -> list[VideoLike]:
        async with async_session_maker() as session:
            result = await session.scalars(select(VideoLike))
            return [like for like in result]

    async def create(self, like: VideoLike):
        async with async_session_maker() as session:
            session.add(like)

            await session.commit()

    async def get_likes_count(self, video_id: str) -> int:
        likes = await self.get()
        likes = list(filter(lambda x: x.video_id == video_id, likes))
        return len(likes)

    async def get_like(self, like: VideoLike) -> VideoLike:
        likes = await self.get()
        likes = list(filter(lambda x: x.video_id == like.video_id, likes))
        like = list(filter(lambda x: x.user_id == like.user_id, likes))
        return None if len(like) == 0 else like[0]

    async def delete(self, like):
        async with async_session_maker() as session:
            likes = await self.get()
            like = list(filter(lambda x: x.user_id == like.user_id and x.video_id == like.video_id, likes))
            if len(like) == 0:
                return
            like = like[0]
            await session.delete(like)
            await session.commit()
            return True
