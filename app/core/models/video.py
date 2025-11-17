from sqlalchemy import Integer, Boolean, String, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models import Base


class VideoResult(Base):
    __tablename__ = "videos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    filename: Mapped[str] = mapped_column(String, nullable=False)
    movement = mapped_column(Boolean, nullable=False)
    created_at = mapped_column(DateTime(timezone=True), default=func.now(), server_default=func.now())