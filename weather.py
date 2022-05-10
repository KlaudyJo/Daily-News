import requests

endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "API_KEY"
weather_params  = {
    "lat": 50.08804,
    "lon": 14.42076,
    'unit': 'metric',
    'lang': 'cz',
    "appid": api_key,
}
class Weather_api:
    def get_weather(self):
        response = requests.get(endpoint, params=weather_params)
        weather_slice = response.json()["daily"][0]
        daily_temp = float(weather_slice['temp']['day']) - 273.15
        weather = weather_slice['weather'][0]['main']
        weather_desc =  weather_slice['weather'][0]['description']
        
        return round(float(daily_temp),1), weather, weather_desc
