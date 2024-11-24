from flask import render_template, abort
from .queries import consulta_poblacion_promedio, consulta_paises_mas_50_millones

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/consulta1')
    def consulta_1():
        try:
            resultados = consulta_poblacion_promedio()
        except Exception as e:
            abort(500)  # Devuelve un error 500 en caso de fallo
        return render_template('consulta_1.html', resultados=resultados)

    @app.route('/consulta2')
    def consulta_2():
        try:
            resultados = consulta_paises_mas_50_millones()
        except Exception as e:
            abort(500)
        return render_template('consulta_2.html', resultados=resultados)

    @app.route('/consulta3/<codigo_pais>')
    def consulta_3(codigo_pais):
        try:
            resultados = consulta_idiomas_por_pais(codigo_pais)
        except Exception as e:
            abort(500)
        return render_template('consulta_3.html', resultados=resultados, codigo_pais=codigo_pais)
