from flask import Flask
from .api.other_api import GeocodeClient
from .api.owm_api import OwmApiClient

app = Flask(__name__)
app.config.from_object('config')

geocode_client = GeocodeClient()
owm_client = OwmApiClient()

from app import views, models
