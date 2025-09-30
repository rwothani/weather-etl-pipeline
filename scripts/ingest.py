import requests
import pandas as pd
import os

# API configuration
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": 40.71,  # New York City
    "longitude": -74.01,
    "start_date": "2023-01-01",
    "end_date": "2023-01-07",  # Shortened for testing
    "hourly": "temperature_2m,precipitation",
    "temperature_unit": "celsius",
    "precipitation_unit": "mm"
}

# Fetch data
try:
    response = requests.get(url, params=params, proxies={"http": None, "https": None})
    response.raise_for_status()
    data = response.json()
except requests.RequestException as e:
    print(f"API request failed: {e}")
    exit(1)

# Process and save to CSV
if "hourly" in data and data["hourly"]["time"]:
    df = pd.DataFrame({
        "time": data["hourly"]["time"],
        "temperature_2m": data["hourly"]["temperature_2m"],
        "precipitation": data["hourly"]["precipitation"]
    })
    # Use /app/data in Docker, project root data/ otherwise
    output_dir = "/app/data" if os.path.exists("/app") else os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "openmeteo_data.csv")
    df.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")
else:
    print("No data returned from API")