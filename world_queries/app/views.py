from flask import render_template
from app import db
from app.models import Country, City, CountryLanguage
from app.queries import get_complex_query_1, get_complex_query_2
from .queries import consulta_poblacion_promedio

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consulta1')
def consulta_1():
    resultados = consulta_poblacion_promedio()
    return render_template('consulta_1.html', resultados=resultados)
