from fastapi import APIRouter
from app.core.responses import response_format


router = APIRouter()


@router.get(
    "/job",
    description="Return jobs information",
    tags=["Jobs"],
)
def job():
    return response_format(
        {
            'success': True,
            'message': 'Hunty test app',
            'data': "job"
        }
    )




