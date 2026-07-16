# Weather Watch

A Python application that fetches real-time weather data using the OpenWeatherMap API. The program supports viewing current weather conditions for a city and comparing weather metrics between two different locations.

## Features

* Real-time weather data retrieval
* Compare weather conditions between two cities
* Temperature conversion to Celsius
* Wind speed, pressure, and "feels like" temperature
* Robust error handling
* Tabular comparison using Pandas

## Technologies Used

* Python 3
* Requests
* Pandas
* OpenWeatherMap API

## How to Run

### Install Dependencies

```bash
pip install requests pandas
```



Create an environment variable:

```bash
export OPENWEATHER_API_KEY="your_api_key"
```

Windows:

```powershell
set OPENWEATHER_API_KEY=your_api_key
```

### Run the Application

```bash
python WeatherWatch.py
```

## Example Output

```text
City Name: Leh
Temperature: 15.3
Wind Speed: 3.2
Pressure: 1013
Feels Like: 14.8
```

### City Comparison

| City       | Temperature | Pressure | Feels Like | Wind Speed |
| ---------- | ----------: | -------: | ---------: | ---------: |
| Leh        |        15.3 |     1013 |       14.8 |        3.2 |
| Blacksburg |        23.7 |     1009 |       22.5 |        2.4 |

## Project Structure

```text
Weather-Watch/
├── WeatherWatch.py
├── .env
└── README.md
```

