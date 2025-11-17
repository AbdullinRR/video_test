from fastapi import APIRouter

from .metrics import router as metrics_router
from .analyze import router as analyze_router


router = APIRouter(prefix="/v1")
router.include_router(metrics_router)
router.include_router(analyze_router)




