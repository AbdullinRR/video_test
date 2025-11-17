from fastapi import APIRouter, UploadFile, File, Depends
from app.services.video import VideoService


router = APIRouter(prefix="/analyze", tags=["analyze"])

@router.post("/", summary="принимает видео, анализирует, возвращает результат")
async def start_analyze(
    file: UploadFile = File(...),
    service: VideoService = Depends()
):
    result = await service.process_video(file)
    return result
