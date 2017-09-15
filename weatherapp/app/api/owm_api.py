# -*- coding: utf-8 -*-
import requests
import datetime
from app.common.constants import CURRENT_WEATHER_BASE_URL, API_KEY, TEN_MINTUE_MILLI, FORECAST_BASE_URL, THREE_HR_MILLI

class OwmApiClient(object):
    def __init__(self):
        self.daily_weather_cache = {}
        self.cur_weather_cache = {}
        self.epoch = datetime.datetime.utcfromtimestamp(0)

    def unix_time_milliseconds(self, dt):
        return (dt - self.epoch).total_seconds() * 1000.0

    def get_current_weather(self, city_id):
        url = CURRENT_WEATHER_BASE_URL + "?id={}&appid={}".format(city_id, API_KEY)
        current_unix_ts = self.unix_time_milliseconds(datetime.datetime.utcnow())
        if self.url_in_cur_weather_cache(url):
            print "current - from cache"
            current_weather_info = self.cur_weather_cache.get(url)
            last_update_unix_ts = current_weather_info[1] # in milliseconds
            if not self.can_update_cur_weather_cache(current_unix_ts, last_update_unix_ts):
                print "current - not updating cache"
                return self.cur_weather_cache.get(url)[0]
        print "current - updating cache"
        response = requests.get(url)
        current_weather_info = response.json()
        self.cur_weather_cache[url] = (current_weather_info, current_unix_ts)
        return current_weather_info

    def get_forecast(self, city_id):
        url = FORECAST_BASE_URL + "?id={}&appid={}".format(city_id, API_KEY)
        current_unix_ts = self.unix_time_milliseconds(datetime.datetime.utcnow())
        if self.url_in_daily_cache(url):
            print "forecast - from cache"
            forecast_results = self.daily_weather_cache.get(url)
            last_update_unix_ts = forecast_results[1]  # in milliseconds
            if not self.can_update_cur_weather_cache(current_unix_ts, last_update_unix_ts):
                print "forecast - not updating cache"
                return self.daily_weather_cache.get(url)[0]
        print "forecast - updating cache"
        response = requests.get(url)
        forecast_results = response.json()
        self.daily_weather_cache[url] = (forecast_results, current_unix_ts)
        return forecast_results

    def url_in_cur_weather_cache(self, url):
        if self.cur_weather_cache.get(url) is None:
            return False
        return True

    def url_in_daily_cache(self, url):
        if self.daily_weather_cache.get(url) is None:
            return False
        return True

    def can_update_cur_weather_cache(self, cur_ts, last_update_ts):
        difference = cur_ts - last_update_ts
        if difference > TEN_MINTUE_MILLI:
            print difference
            return True
        return False

    def can_update_daily_cache(self, cur_ts, last_update_ts):
        difference = cur_ts - last_update_ts
        if difference > THREE_HR_MILLI:
            print difference
            return True
        return False
