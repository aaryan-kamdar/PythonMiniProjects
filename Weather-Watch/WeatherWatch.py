from requests import get
from requests.exceptions import RequestException
import pandas as pd

API_KEY = ""
BASE_URL = "https://api.openweathermap.org/"


def get_links(BASE_URL, city, country):
    JOIN_URL = f"data/2.5/weather?q={city},{country}&appid={API_KEY}"
    return BASE_URL + JOIN_URL


def get_different_conditions(BASE_URL, city, country, Unit):
    # 1. Network errors (no internet, timeout, DNS failure)
    try:
        response = get(get_links(BASE_URL, city, country), timeout=10)
    except RequestException as e:
        print(f"Network error while fetching '{city}': {e}")
        return None

    # 2. Bad status codes  give a specific message, not just "Error"
    if response.status_code == 404:
        print(f"City not found: '{city}, {country}' — check the spelling.")
        return None
    elif response.status_code == 401:
        print("Invalid API key.")
        return None
    elif response.status_code != 200:
        print(f"API error for '{city}': status code {response.status_code}")
        return None

    # 3. Unexpected/malformed JSON structure
    try:
        data = response.json()
        temp = data["main"]["temp"]
        if Unit.lower() == "celsius":
            temp = round(temp - 273.15, 1)
        pressure = data["main"]["pressure"]
        feels_like = data["main"]["feels_like"]
        city_name = data["name"]
        wind_speed = data["wind"]["speed"]
    except (KeyError, ValueError) as e:
        print(f"Unexpected API response for '{city}': missing {e}")
        return None

    return city_name, temp, pressure, feels_like, wind_speed


def current_conditions(BASE_URL, city, country, Unit):
    result = get_different_conditions(BASE_URL, city, country, Unit)
    if result is None:          
        return
    city_name, temp, pressure, feels_like, wind_speed = result
    print(f"City Name: {city_name}")
    print(f"Temperature: {temp}")
    print(f"Wind Speed: {wind_speed}")
    print(f"Pressure: {pressure}")
    print(f"Feels_like: {feels_like}")


def compare_cities(BASE_URL, city_1, country_1, city_2, country_2, Unit):
    result1 = get_different_conditions(BASE_URL, city_1, country_1, Unit)
    result2 = get_different_conditions(BASE_URL, city_2, country_2, Unit)

    if result1 is None or result2 is None:
        print("Comparison aborted — could not fetch data for one or both cities.")
        return

    city_name1, temp1, pressure1, feels_like1, wind_speed1 = result1
    city_name2, temp2, pressure2, feels_like2, wind_speed2 = result2

    data = pd.DataFrame({
        "City": [city_name1, city_name2],
        "Temperature": [temp1, temp2],
        "Pressure": [pressure1, pressure2],
        "Feels Like": [feels_like1, feels_like2],
        "Wind speed": [wind_speed1, wind_speed2],
    })
    print(data)


compare_cities(BASE_URL, "LEH", "INDIA", "BLACKSBURG", "USA", "celsius")