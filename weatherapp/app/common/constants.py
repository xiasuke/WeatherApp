import os
from common import CommonHelper

JSON_FILE = os.path.abspath(os.path.dirname(__file__)) + "/../static/city.list.json"
CITIES_INFO = CommonHelper.load_city_list_json(JSON_FILE)

# OWM API related URL
ROOT_OMW_URL = "http://api.openweathermap.org/data/2.5"
CURRENT_WEATHER_BASE_URL = ROOT_OMW_URL + "/weather"
FORECAST_BASE_URL = ROOT_OMW_URL + "/forecast"
APPID = "appid="
TEN_MINTUE_MILLI = 600000
THREE_HR_MILLI =1.08e+7


# Other API
GOOGLE_GEOCODE_API = "http://maps.googleapis.com/maps/api/geocode/json"

API_KEY = os.environ['OWM_API_KEY']
print API_KEY
# REMOVE LATER http://api.openweathermap.org/data/2.5/weather?q=london&appid=e66de67701cd41fc966f816cddbcdabf
# api.openweathermap.org/data/2.5/weather?id=2172797