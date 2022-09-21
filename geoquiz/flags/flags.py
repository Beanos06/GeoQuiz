from flask import Blueprint, render_template
import json
import random

flags_bp = Blueprint('flags_bp', __name__, template_folder='templates')

@flags_bp.route('/')
def flag_quiz():
    with open('static/data/countries/countries.json', 'r') as data:
        json_data = json.load(data)
        number_of_countries = len(json_data)

        random_country =  json_data[random.randint(0,number_of_countries)]
        country_name = random_country['name']['common']
        flag_url = random_country['flags']['png']

    return render_template('flags/quiz.html', country_name=country_name, flag_url=flag_url)