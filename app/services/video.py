import cv2
import tempfile
import time

from fastapi import Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.repositories.video import VideoRepository
from app.services.metrics import metrics


class VideoService:

    def __init__(self, session: AsyncSession = Depends(get_db)):
        self.repo = VideoRepository(session)

    async def process_video(self, file: UploadFile):
        start = time.time()

        try:
            # сохраняем во временный файл
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                tmp.write(await file.read())
                tmp_path = tmp.name

            movement = self._detect_movement(tmp_path)

            # сохранение результата
            record = await self.repo.create(
                filename=file.filename,
                movement=movement
            )

            # метрики: успешно обработанное видео
            metrics.total_videos.inc()

            # метрики: время обработки
            metrics.processing_time.observe(time.time() - start)

            return {
                "id": record.id,
                "filename": record.filename,
                "movement": record.movement,
                "created_at": record.created_at
            }

        except Exception as e:
            # метрики: ошибка
            metrics.errors.inc()
            raise

    def _detect_movement(self, path: str) -> bool:
        cap = cv2.VideoCapture(path)
        ret, frame1 = cap.read()
        ret, frame2 = cap.read()

        while cap.isOpened():
            diff = cv2.absdiff(frame1, frame2)
            gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

            if thresh.sum() > 0:
                return True

            frame1 = frame2
            ret, frame2 = cap.read()

            if not ret:
                break

        return False
