from app.video.schemas import VideoUpload, VideoInDb
from app.video.uploader import Uploader
from app.video import manager

class VideoUseCase:
    def __init__(self):
        self.uploader = Uploader()
        self.manager = manager.VideoManager()

    async def create_video(self, upload: VideoUpload):
        video = VideoInDb(upload)
        await self.manager.create(video)

    def upload_file(self, file, id):
        url = self.uploader.upload_file(file, id)
        return url

    async def get_by_id(self, id) -> VideoInDb:
        return await self.manager.get_by_id(id)

    async def get(self) -> list[VideoInDb]:
        return await self.manager.get()
