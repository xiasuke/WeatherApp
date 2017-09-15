# -*- coding: utf-8 -*-
import json

class CommonHelper(object):

    @staticmethod
    def load_city_list_json(json_file):
        print "loading cities"
        cities = dict()
        with open(json_file) as data_file:
            city_list = json.load(data_file)

            for city_info in city_list:
                city_name = city_info.get("name")
                del city_info["name"]
                if cities.get(city_name) is None:
                    cities[city_name] = [city_info]
                else:
                    cities[city_name].append(city_info)
        return cities
