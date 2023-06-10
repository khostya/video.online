from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi.responses import Response
from fastapi import Form, UploadFile, Depends
from typing import Annotated
from app.user.user import User, current_active_user
from app.video.schemas import VideoUpload
from app.video.videousecase import VideoUseCase

video_router = InferringRouter()


@cbv(video_router)
class LikeRouter:
    def __init__(self):
        self.useCase = VideoUseCase()

    @video_router.post("/video/{id}/like", response_class=Response)
    async def like_video(self):
        pass

    @video_router.post("/video/{id}/dislike", response_class=Response)
    async def dislike_video(self):
        pass
