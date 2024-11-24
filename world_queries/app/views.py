from flask import render_template
from .queries import consulta_poblacion_promedio

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/consulta1')
    def consulta_1():
        resultados = consulta_poblacion_promedio()
        return render_template('consulta_1.html', resultados=resultados)
