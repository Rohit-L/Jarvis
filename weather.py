import forecastio
import datetime

class Weather:

    def __init__(self):
        self.api_key = "cc5f21ee8de685035e024ffbc0c233d8"
        self.lat = 37.871593
        self.lon = -122.272747

    def get_current_forcast(self):
        forecast = forecastio.load_forecast(self.api_key, self.lat, self.lon)
        summary = forecast.currently().summary
        temperature = round(forecast.currently().temperature, 0)
        weather = "It is " + summary + " and " + str(temperature) + " degrees"
        return weather

    def get_tomorrow_forcast(self):
        time = datetime.datetime.now() + datetime.timedelta(days=1)
        forecast = forecastio.load_forecast(self.api_key, self.lat, self.lon, time=time)
        summary = forecast.currently().summary
        temperature = round(forecast.currently().temperature, 0)
        weather = "It is " + summary + " and " + str(temperature) + " degrees tomorrow."
        if "Rain" in summary:
            weather += " You should bring an umbrella and a jacket."
            return weather
        if temperature < 50:
            weather += " It might be a good idea to take a jacket."
            return weather
        if temperature > 75:
            weather += " Dress lightly."
            return weather
        return weather
