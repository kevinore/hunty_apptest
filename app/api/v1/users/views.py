from uuid import UUID
from starlette.responses import JSONResponse
from app.core.handlers import ProcessHandler
from fastapi.encoders import jsonable_encoder
from app.core.responses import response_format
from app.api.v1.users.serializers import User
from fastapi import APIRouter, Response, status, Request

router = APIRouter()


@router.get(
    "/user",
    description="Return user information",
    response_class=JSONResponse,
    tags=["User"],
)
def list_user(request: Request, response: Response):
    """
    Return user information
    """
    result = ProcessHandler.get_users(**request.query_params)
    response.status_code = status.HTTP_200_OK
    return response_format(
        {
            "success": True,
            "message": "User information",
            "data": result
        }
    )


@router.post(
    "/user",
    description="Create a new user",
    response_class=JSONResponse,
    tags=["User"],
)
def create_user(model: User, response: Response):
    """
    Create a new user
    """
    model_dict = jsonable_encoder(model)
    result = ProcessHandler.create_user(model_dict)
    response.status_code = status.HTTP_201_CREATED
    return response_format(
        {
            "success": True,
            "message": "User created successfully",
            "data": result
        }
    )


@router.put(
    "/user/{uuid}",
    description="Update user, {uuid} of user",
    response_class=JSONResponse,
    tags=["User"],
)
def update_user(model: User, response: Response, uuid: UUID):
    """
    Update user
    """
    model_dict = jsonable_encoder(model)
    result = ProcessHandler.update_users(uuid, model_dict)
    response.status_code = status.HTTP_202_ACCEPTED
    return response_format(
        {
            "success": True,
            "message": "User updated successfully",
            "data": result
        }
    )


@router.delete(
    "/user/delete/{uuid}",
    description="Delete user, {uuid} of user",
    response_class=JSONResponse,
    tags=["User"],
)
def delete_user(response: Response, uuid: UUID):
    """
    Delete user
    """
    result = ProcessHandler.delete_users(uuid)
    response.status_code = status.HTTP_202_ACCEPTED
    return response_format(
        {
            "success": True,
            "message": "User deleted successfully",
            "data": result
        }
    )