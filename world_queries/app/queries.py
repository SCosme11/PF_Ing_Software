from .models import db, City

def consulta_poblacion_promedio():
    # consulta #1: la poblacion promedio por cada ciudad en la db
    resultados = db.session.query(
        db.func.avg(City.population).label('poblacion_promedio')
    ).scalar()

    return {'poblacion_promedio': resultados}
