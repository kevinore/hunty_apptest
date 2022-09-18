import mongoengine as mongo
from config import settings
from fastapi import FastAPI
from app.api.urls import routers
from starlette.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.openapi.utils import get_openapi
from app.core.responses import response_format
from app.core.exceptions import ExceptionService
from app.core.exceptions import ExceptionService
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException


app = FastAPI(
    title="App",
    description="Hunty test app",
    version=settings.API_VERSION,
    docs_url='/api/v1/docs'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers)

mongo.connect(host=settings.MONGO_URI)


@app.exception_handler(ExceptionService)
async def exception_service_handler(request, exc):
    data = {
        "success": False,
        "message": str(exc.args[1]),
        "data": exc.args[2]
    }

    return JSONResponse(
        status_code=exc.args[3],
        content=jsonable_encoder(
            response_format(data)
        ),
    )


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Hunty 💜",
        version="1.0",
        description="Api documentation",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.exception_handler(Exception)
async def exception_handler(request, exc):
    data = {
        "success": False,
        "message": str(exc.__class__) + " - " + str(exc.args[0]),
        "data": exc.errors if hasattr(exc, "errors") else {}
    }

    return JSONResponse(
        status_code=500,
        content=jsonable_encoder(
            response_format(data)
        ),
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    data = {
        "codPrestates": exc.status_code,
        "observations": str(exc.detail)
    }

    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(
            response_format(data)
        ),
    )

