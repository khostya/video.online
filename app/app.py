from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.account.router import account_router
from app.db import create_db_and_tables
from app.user.routers import *
from app.site.router import template_router
from app.video.router import video_router

app = FastAPI()

app.mount('/static', StaticFiles(directory='./static'), name="static")

app.include_router(auth_router, prefix="/auth/jwt", tags=["auth"])

app.include_router(register_router, prefix="/auth", tags=["auth"],)

app.include_router(reset_password_router, prefix="/auth", tags=["auth"])

app.include_router(verify_router, prefix="/auth", tags=["auth"])

app.include_router(users_router, prefix="/users", tags=["users"])

app.include_router(template_router, tags=["templates"])

app.include_router(account_router, tags=["account"])

app.include_router(video_router, tags=["video"])


@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()
