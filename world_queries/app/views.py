from flask import render_template, abort
from .queries import consulta_poblacion_promedio, consulta_ciudades_por_pais, consulta_lenguajes_por_pais, consulta_idiomas_por_pais, consulta_paises_mas_50_millones, consulta_todos_los_paises

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/consulta1')
    def consulta_1():
        resultados = consulta_poblacion_promedio()
        return render_template('consulta_1.html', resultados=resultados)

    @app.route('/consulta2')
    def consulta_2():
        resultados = consulta_ciudades_por_pais()
        return render_template('consulta_2.html', resultados=resultados)

    @app.route('/consulta3')
    def consulta_3():
        resultados = consulta_lenguajes_por_pais()
        return render_template('consulta_3.html', resultados=resultados)

    @app.route('/consulta4')
    def consulta_4():
        try:
            resultados = consulta_paises_mas_50_millones()
        except Exception as e:
            abort(500)
        return render_template('consulta_4.html', resultados=resultados)

    @app.route('/todos_los_paises')
    def todos_los_paises():
        # Obtener todos los países de la base de datos
        resultados = consulta_todos_los_paises()
        return render_template('TodosPaises.html', resultados=resultados)

    @app.route('/consulta5/<codigo_pais>')
    def consulta_5(codigo_pais):
        try:
            resultados = consulta_idiomas_por_pais(codigo_pais)
        except Exception as e:
            abort(500)
        return render_template('consulta_5.html', resultados=resultados, codigo_pais=codigo_pais)

