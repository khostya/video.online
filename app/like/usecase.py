from app.like.schemas import VideoLike
from app.like.manager import LikeManager


class LikeUseCase:
    def __init__(self):
        self.manager = LikeManager()

    async def create_like(self, like: VideoLike):
        await self.manager.create(like)

    async def get_likes_count(self, video_id) -> int:
        return await self.manager.get_likes_count(video_id)

    async def delete_like(self, like: VideoLike) -> list[VideoLike]:
        return await self.manager.delete(like)

    async def get_like(self, like):
        return await self.manager.get_like(like)
