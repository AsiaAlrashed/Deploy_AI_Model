from fastapi import APIRouter, Request
from ..models.schemas import TrafficReuest, TrafficResponse

import pandas as pd

router = APIRouter(
    prefix="/traffic",
)

"""Create api router so we can build or 
connect this endpoint to our application"""


@router.post("/volume")
async def get_traffic_predicition(
    request: Request,
    traffic_reuest: TrafficReuest,
):
    """Asynchronous function to get traffic prediction"""
    traffic_model = request.app.state.traffic_model

    feature = {
        "rain_1h": [traffic_reuest.rain],
        "snow_1h": [traffic_reuest.snoe],
        "temp": [traffic_reuest.temp],
        "clouds_all": [traffic_reuest.cloud],
        "hour": [traffic_reuest.hour],
        "day": [traffic_reuest.day],
        "month": [traffic_reuest.month],
    }

    transformed_feature = pd.DataFrame.from_dict(feature)

    traffic_volume = traffic_model.predict(transformed_feature)

    return TrafficResponse(traffic_volume=traffic_volume)
