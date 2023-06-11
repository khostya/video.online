import json.encoder

from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi.responses import Response
from fastapi import Depends

from app.user.user import User, current_active_user
from app.like.schemas import VideoLike
from app.like.usecase import LikeUseCase

like_router = InferringRouter()


@cbv(like_router)
class LikeRouter:
    def __init__(self):
        self.useCase = LikeUseCase()

    @like_router.post("/video/{video_id}/like", response_class=Response)
    async def like_video(self, video_id: str, user: User = Depends(current_active_user)):
        create = VideoLike(str(user.id), video_id)
        await self.useCase.create_like(create)
        return Response(status_code=201)

    @like_router.post("/video/{video_id}/dislike", response_class=Response)
    async def dislike_video(self, video_id: str, user: User = Depends(current_active_user)):
        like = VideoLike(str(user.id), video_id)
        ok = await self.useCase.delete_like(like)
        if not ok:
            return Response(status_code=409)

        return Response(status_code=200)

    @like_router.get("/video/{video_id}/is_liked", response_class=Response)
    async def is_liked(self, video_id: str, user: User = Depends(current_active_user)):
        like = VideoLike(str(user.id), video_id)
        like = await self.useCase.get_like(like)
        response = {'is_liked': True if like is not None else False}
        return Response(status_code=200, content=json.encoder.JSONEncoder().encode(response))
