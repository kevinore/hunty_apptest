from fastapi import APIRouter
from app.core.responses import response_format

router = APIRouter()


@router.get(
    "/",
    description="/",
    tags=["/"],
)
def root():
    return response_format(
        {
            "success": True,
            "message": "Service running successfully",
            "data": {}
        }
    )


