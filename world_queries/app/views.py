from flask import render_template
from app import db
from app.models import Country, City, CountryLanguage
from app.queries import get_complex_query_1, get_complex_query_2

@app.route('/')
def index():
    return render_template('index.html')
