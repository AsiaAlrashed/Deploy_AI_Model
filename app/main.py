from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from .get_traffic_volum import get_traffic_volum
from .startup.load_models import load_traffic_model

app = FastAPI(
    docs_url="/api/v2/docs",
    redoc_url="/api/v2/redoc",
    title="API Traffic volume",
    description="Traffic volume",
    version="2.0",
    openapi_url="/api/v2/openapi.json",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as needed
    allow_credentials=True,
    allow_methods=["*"],  # Use 'allow_methods' instead of 'allow_method'
    allow_headers=["*"],
)
"""
 We map the model to the application state which means 
 that any endpoint you can access and need a model 
 in memory for fast responses can do so.
"""

app.state.traffic_model = load_traffic_model()

app.include_router(get_traffic_volum.router)
