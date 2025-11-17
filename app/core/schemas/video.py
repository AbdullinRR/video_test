from pydantic import BaseModel
from datetime import datetime

class VideoResultOut(BaseModel):
    id: int
    filename: str
    movement: bool
    created_at: datetime

    class Config:
        orm_mode = True
