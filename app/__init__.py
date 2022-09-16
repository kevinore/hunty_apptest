import mongoengine as mongo
from fastapi import FastAPI
from config import settings
from fastapi.middleware.cors import CORSMiddleware
from app.api.urls import routers


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
