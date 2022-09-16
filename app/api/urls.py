from fastapi import APIRouter
from app.api.v1.core import views as core
from app.api.v1.job import views as job
from app.api.v1.users import views as user

routers = APIRouter()

routers.include_router(
    core.router,
    prefix="/api/v1"
)

routers.include_router(
    job.router,
    prefix="/api/v1"
)

routers.include_router(
    user.router,
    prefix="/api/v1"
)