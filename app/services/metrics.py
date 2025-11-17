
from prometheus_client import Counter, Histogram


class MetricsService:
    def __init__(self):
        # сколько видео обработано успешно
        self.total_videos = Counter(
            "videos_processed_total",
            "total number of processed videos"
        )

        # ошибки
        self.errors = Counter(
            "videos_processing_errors_total",
            "total number of processing errors"
        )

        # время обработки
        self.processing_time = Histogram(
            "video_processing_duration_seconds",
            "time spent on processing a video"
        )


metrics = MetricsService()
