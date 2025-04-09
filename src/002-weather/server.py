from mcp.server.fastmcp import FastMCP

import httpx

from dotenv import load_dotenv
import os


mcp = FastMCP(
    "Arjuns Weather App",
    dependencies=[
        "httpx",
        "python-dotenv",
    ],
)

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Base URL for OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather_by_city_name(city: str) -> dict | None:
    """
    Function to get weather data for a specific city
    """
    try:
        # Parameters for the API request
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric",  # Use 'imperial' for Fahrenheit
        }

        # Make the API request
        response = httpx.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Return the JSON response
        return response.json()
    except httpx.HTTPStatusError as e:
        print(f"Error fetching weather data: {e}")
        return None


@mcp.tool(
    "weather_by_city_name",
    description="Returns the weather info of city in dictionary.",
)
def weather_by_city(city: str) -> dict | None:
    """
    Get the weather by city name.
    """
    return get_weather_by_city_name(city)


if __name__ == "__main__":
    mcp.run(transport="stdio")
