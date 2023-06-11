import json

from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi.responses import Response, RedirectResponse
from fastapi import File, Form, UploadFile, Depends
from typing import Annotated
from app.user.user import User, get_user_manager, get_jwt_strategy
from app.video.schemas import VideoUpload
from app.video.videousecase import VideoUseCase
from fastapi_users.jwt import  decode_jwt
video_router = InferringRouter()


@cbv(video_router)
class VideoRouter:
    def __init__(self):
        self.useCase = VideoUseCase()

        self.userManager = get_user_manager()
        self.jwtStrategy = get_jwt_strategy()

    @video_router.get("/{id}", response_class=Response)
    async def getById(self, id):
        video = self.useCase.get_by_id(id)
        return Response(status_code=201, content=video)

    @video_router.get("/", response_class=Response)
    async def get(self):
        videos = self.useCase.get()
        return Response(status_code=201, content=videos)

    ## очень очень очень очень плохо
    @video_router.post("/video", response_class=Response)
    async def upload(self, name: Annotated[str, Form()], file: Annotated[UploadFile, File()],
                   jwtoken: Annotated[str, Form()]):
        try:
            token = jwtoken.split(' ')[1]
            jwtstr = self.jwtStrategy
            data = decode_jwt(
                token, jwtstr.decode_key, jwtstr.token_audience, algorithms=[jwtstr.algorithm])
            user_id = data.get('sub')
        except:
            return Response(status_code=401)
        upload = VideoUpload(user_id, '', name)
        url = self.useCase.upload_file(file, upload.id)
        upload.video = url
        await self.useCase.create_video(upload)

        return Response(status_code=303, content=url, headers={'Location': 'http://localhost:8000/'})
