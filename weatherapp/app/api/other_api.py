import requests
from app.common.constants import GOOGLE_GEOCODE_API

class GeocodeClient(object):
    def __init__(self):
        self.cache = {}

    def get_administrative_area(self, lat, lng):
        url = GOOGLE_GEOCODE_API + "?latlng={},{}&sensor={}".format(lat, lng, False)
        if self.url_in_cache(url):
            print "from cache"
            return self.cache.get(url)
        response = requests.get(url)
        response_list = response.json()
        address_components = response_list["results"][0]["address_components"]
        for comp in address_components:
            if comp["types"][0] == "administrative_area_level_1":
                admin_short_name = comp["short_name"]
                self.cache[url] = admin_short_name
                return admin_short_name

    def url_in_cache(self, url):
        if self.cache.get(url) is None:
            return False
        return True
