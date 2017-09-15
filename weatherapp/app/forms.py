# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired


class CityInputForm(FlaskForm):
    city = StringField('City', validators=[DataRequired('Please fill out the missing field')])

class SelectCityForm(FlaskForm):
    city_list = SelectField("DuplicateCity")
