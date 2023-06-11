import uuid
from typing import Any

from app.db import Base
from sqlalchemy import Column, String
from pydantic import BaseModel


class VideoUpload:
    def __init__(self, author_id, video, name):
        self.id = str(uuid.uuid4())
        self.author_id = str(author_id)
        self.video = video
        self.name = name


class FileUploadResponse(BaseModel):
    video: str


class FileUploadRequest(BaseModel):
    name: str
    video: str


class VideoInDb(Base):
    __tablename__ = 'video'
    id = Column(String, primary_key=True, index=True)
    author_id = Column(String, primary_key=False, index=False)
    video_url = Column(String, primary_key=False, index=False)
    name = Column(String, primary_key=False, index=True)

    def __init__(self, upload: VideoUpload, **kw: Any):
        super().__init__(**kw)
        self.id = upload.id
        self.author_id = upload.author_id
        self.name = upload.name
        self.video_url = upload.video


class VideoDto:
    def __init__(self, name, video):
        self.name = name
        self.video = video