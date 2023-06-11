from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates

from app.like.usecase import LikeUseCase
from app.video.schemas import VideoDto
from app.video.videousecase import VideoUseCase
templates = Jinja2Templates(directory="templates")


template_router = InferringRouter()
video_use_case = VideoUseCase()
like_use_case = LikeUseCase()


@template_router.get("/video/{id}", response_class=HTMLResponse)
async def video(request: Request, id: str):
    video = await video_use_case.get_by_id(id)
    if video is None:
        return templates.TemplateResponse("video.html", {"request": request, "video": video})
    count = await like_use_case.get_likes_count(id)
    dto = VideoDto(video.name, video.video_url)
    return templates.TemplateResponse("video.html", {"request": request, "video": dto, 'count': count})


@cbv(template_router)
class TemplateRouter:
    def __init__(self):
        self.video_use_case = VideoUseCase()

    @template_router.get("/login", response_class=HTMLResponse)
    async def login(self, request: Request):
        return templates.TemplateResponse("login.html", {"request": request})

    @template_router.get("/registration", response_class=HTMLResponse)
    async def video(self, request: Request):
        return templates.TemplateResponse("registration.html", {"request": request})

    @template_router.get("/", response_class=HTMLResponse)
    async def index(self, request: Request):
        videos = await self.video_use_case.get()
        videos_dto = []
        for video in videos:
            videos_dto.append(VideoDto(video.name, video.video_url))

        return templates.TemplateResponse("index.html", {"request": request, "videos": videos_dto})

    @template_router.get("/upload", response_class=HTMLResponse)
    async def upload(self, request: Request):
        return templates.TemplateResponse("upload.html", {"request": request})




