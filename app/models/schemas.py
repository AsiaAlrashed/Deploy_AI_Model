from pydantic import BaseModel


class TrafficReuest(BaseModel):
    rain: float
    snoe: float
    temp: float
    cloud: int
    hour: int
    day: int
    month: int


class TrafficResponse(BaseModel):
    traffic_volume: float


"""The Metro Interstate Traffic Volume dataset, hosted by the UCI Machine Learning Repository, 
provides information about hourly traffic volume on the Interstate 94 highway (I-94) westbound in Minneapolis,
Minnesota. This dataset was collected with the intention to understand factors affecting traffic volume, 
especially weather-related conditions. 
Here’s a breakdown of its key components: 
Dataset Overview: Data Points: The dataset includes nearly 48,000 records.
Features: There are 9 features plus a target variable.
Features in the Dataset: Holiday: Indicates if the day was a holiday.
Temperature (temp): Temperature in Kelvin.
Rain (rain_1h): Amount of rain in the previous hour (mm).
Snow (snow_1h): Amount of snow in the previous hour (mm).
Clouds (clouds_all): Percentage of cloud cover.
Weather Main (weather_main): General weather condition (e.g., clear, rain, snow).
Weather Description (weather_description): Detailed weather description (e.g., light rain, heavy snow).
Date and Time (date_time): Timestamp of the traffic volume record."""
