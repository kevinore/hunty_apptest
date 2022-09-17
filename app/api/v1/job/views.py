from uuid import UUID
from starlette.responses import JSONResponse
from app.core.handlers import ProcessHandler
from fastapi.encoders import jsonable_encoder
from app.core.responses import response_format
from app.api.v1.job.serializers import Job
from fastapi import APIRouter, Response, status, Request

router = APIRouter()


@router.get(
    "/job",
    description="Return job information",
    response_class=JSONResponse,
    tags=["Job"],
)
def list_user(request: Request, response: Response):
    """
    Return user information
    """
    result = ProcessHandler.get_jobs(**request.query_params)
    response.status_code = status.HTTP_200_OK
    return response_format(
        {
            "success": True,
            "message": "Job information",
            "data": result
        }
    )


@router.post(
    "/job",
    description="Create a new job",
    response_class=JSONResponse,
    tags=["Job"],
)
def create_user(model: Job, response: Response):
    """
    Create a new Job
    """
    model_dict = jsonable_encoder(model)
    result = ProcessHandler.create_job(model_dict)
    response.status_code = status.HTTP_201_CREATED
    return response_format(
        {
            "success": True,
            "message": "Job created successfully",
            "data": result
        }
    )


@router.put(
    "/job/{uuid}",
    description="Update job",
    response_class=JSONResponse,
    tags=["Job"],
)
def job_user(model: Job, response: Response, uuid: UUID):
    """
    Update Job
    """
    model_dict = jsonable_encoder(model)
    result = ProcessHandler.update_job(uuid, model_dict)
    response.status_code = status.HTTP_202_ACCEPTED
    return response_format(
        {
            "success": True,
            "message": "Job updated successfully",
            "data": result
        }
    )


@router.delete(
    "/job/delete/{uuid}",
    description="Delete job",
    response_class=JSONResponse,
    tags=["Job"],
)
def delete_job(response: Response, uuid: UUID):
    """
    Delete Job
    """
    result = ProcessHandler.delete_job(uuid)
    response.status_code = status.HTTP_202_ACCEPTED
    return response_format(
        {
            "success": True,
            "message": "Job deleted successfully",
            "data": result
        }
    )


@router.get(
    "/job/filter/{uuid}",
    description="Return job by filter (skills, experience) based on user info",
    response_class=JSONResponse,
    tags=["Job"],
)
def filter_job(response: Response, uuid: UUID):
    """
    Return job
    """
    result = ProcessHandler.filter_job(uuid)
    response.status_code = status.HTTP_200_OK
    return response_format(
        {
            "success": True,
            "message": "Job information",
            "data": result
        }
    )