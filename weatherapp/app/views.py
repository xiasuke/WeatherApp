# -*- coding: utf-8 -*-
import json
from flask import render_template, url_for, redirect, flash, request
from app import app
from .forms import CityInputForm, SelectCityForm
from .models import Cities, CurrentWeather
from controller import InputHandler

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CityInputForm()

    if form.validate_on_submit():
        city_name = form.city.data
        return redirect(url_for('find_city', city_name=city_name))
    return render_template("home.html",
                           title='Home',
                           searchform=form,
                           entries=Cities().get_all_cities())


@app.route('/find_city/<city_name>', methods=['GET', 'POST'])
def find_city(city_name):
    search_form = CityInputForm()
    duplicate_city_form = SelectCityForm()

    if duplicate_city_form.is_submitted() and not search_form.validate_on_submit():
        print "go here"
        value = duplicate_city_form.city_list.data
        if value == "None":
            return render_template("home.html",
                                   title="Invalid Entry",
                                   searchform=search_form,
                                   entries=Cities().get_all_cities())
        value = json.loads(duplicate_city_form.city_list.data)
        print "value_id: {}, {}".format(value, type(value))
        return redirect(url_for('current_weather', city_id=value.get("id")))
    # print city_name
    if search_form.validate_on_submit():
        new_city_name = search_form.city.data
        return redirect(url_for('find_city', city_name=new_city_name))
    city_info = Cities().get_city_info(city_name)

    new_city_info = InputHandler().get_requested_city_state(city_name, city_info)

    if new_city_info is not None and len(new_city_info) != 1:
        duplicate_city_form.city_list.choices = [(json.dumps(city), ", ".join((city_name, city.get("state"), city.get("country")))) for city in new_city_info]
        return render_template("home.html",
                               title=city_name,
                               searchform=search_form,
                               cityinfo=duplicate_city_form,
                               numcityinfo=len(new_city_info),
                               entries=Cities().get_all_cities())
    elif new_city_info is not None and len(new_city_info) == 1:
        print new_city_info[0].get("id")
        return redirect(url_for('current_weather', city_id=new_city_info[0].get("id")))

    flash("%s is not a city" % (city_name))
    return redirect(url_for("index"))


@app.route('/current_weather/<city_id>', methods=['GET', 'POST'])
def current_weather(city_id):
    cur_weather_result = InputHandler().get_city_cur_weather(city_id)
    cur_response_builder = CurrentWeather(cur_weather_result)
    cur_response = cur_response_builder.build_current_weather_response()

    forecast_result = InputHandler().get_city_forecast(city_id)

    return render_template("current_weather.html",
                           title=cur_response_builder.city_name + ", " + cur_response_builder.city_country,
                           weatherdescrip=cur_response_builder.weather_description,
                           temp=cur_response_builder.current_temp,
                           curweather = cur_response,
                           forecast_info=forecast_result["list"])


@app.route('/daily_forecast/<city_id>', methods=['GET', 'POST'])
def daily_forecast(city_id):
    forecast_result = InputHandler().get_city_forecast(city_id)
    return
