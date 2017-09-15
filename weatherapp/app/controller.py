# -*- coding: utf-8 -*-
from app import geocode_client, owm_client


class InputHandler(object):

    def get_requested_city_state(self, city_name, city_info):
        # print city_name
        # print city_info
        if city_info is not None:
            print len(city_info)
            for city in city_info:
                admin_name = geocode_client.get_administrative_area(city["coord"]["lat"], city["coord"]["lon"])
                city["state"] = admin_name
        return city_info

    def get_city_cur_weather(self, city_id):
        print "city_ids: {}".format(city_id)
        current_weather = owm_client.get_current_weather(city_id)
        return current_weather

    def get_city_forecast(self, city_id):
        print "city_ids: {}".format(city_id)
        forecast = owm_client.get_forecast(city_id)
        return forecast
