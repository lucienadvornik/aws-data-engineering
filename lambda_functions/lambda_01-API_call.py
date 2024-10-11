#### LAMBDA for API call #### 

# import libraries
import json
import requests
import pandas as pd  # Import pandas for data manipulation
from datetime import datetime

# API URL and API key (example for OpenWeatherMap API)
API_URL = "https://api.openweathermap.org/data/3.0/onecall" 
API_KEY = "248891ebc2d89fefcb1a025e12e03b9f"  # Specific API key
CITY = "Prague"  # City where we take the weather from
# Latitude and Longitude for Prague
LATITUDE = 50.0755
LONGITUDE = 14.4378

# Download data from the API
def lambda_handler():
    # 1. Download data from the API
    # Construct the request URL with latitude, longitude, and API key
    response = requests.get(f"{API_URL}?lat={LATITUDE}&lon={LONGITUDE}&exclude=hourly,daily&appid={API_KEY}")
    
    # 2. If the request was successful, process the data
    if response.status_code == 200:  # Check if the response was successful
        weather_data = response.json()  # Convert response to JSON
        
        # 3. Extract useful information
        transformed_data = {
            "city": "Prague",  # City name
            "temperature": weather_data["current"]["temp"],  # Current temperature
            "weather": weather_data["current"]["weather"][0]["description"],  # Weather description
            "timestamp": datetime.now().isoformat()  # Get current timestamp
        }
        
        # 4. Create a DataFrame to store the data
        df = pd.DataFrame([transformed_data])  # Create a DataFrame
        
        # 5. Print DataFrame to see the data
        print(df)
        
    else:
        # If there was an error, print an error message with status code and response text
        print(f'Error fetching data from the API. Status code: {response.status_code}, Response: {response.text}')

# To run the function locally
if __name__ == "__main__":
    lambda_handler()  # Call the function to execute