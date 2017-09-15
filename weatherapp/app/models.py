# -*- coding: utf-8 -*-
from app.common.constants import CITIES_INFO

class Cities(object):
    def __init__(self):
        self.cities = CITIES_INFO

    def get_edmonton(self):
        return self.cities["Edmonton"]

    def get_city_info(self, city_name):
        return self.cities.get(city_name)

    def get_all_cities(self):
        return CITIES_INFO.keys()

class CurrentWeather(object):
    def __init__(self, cur_weather_info):
        self.cur_weather_info = cur_weather_info
        self.city_name = cur_weather_info["name"]
        self.city_country = cur_weather_info["sys"]["country"]
        self.weather = cur_weather_info["weather"][0]["main"]
        self.weather_description = cur_weather_info["weather"][0]["description"]
        self.current_temp = cur_weather_info["main"]["temp"]

    def build_current_weather_response(self):
        cur_weather_response = dict()
        cur_weather_response["Cloudiness(%)"] = self.cur_weather_info.get("clouds")["all"]
        lat = self.cur_weather_info["coord"]["lat"]
        lon = self.cur_weather_info["coord"]["lon"]
        cur_weather_response["Geo Coordinates [lat, long]"] = [lat, lon]
        cur_weather_response["Pressure (hpa)"] = self.cur_weather_info["main"]["pressure"]
        cur_weather_response["Humidity (%)"] = self.cur_weather_info["main"]["humidity"]
        cur_weather_response["Wind (m/s)"] = self.cur_weather_info["wind"]["speed"]
        return cur_weather_response
