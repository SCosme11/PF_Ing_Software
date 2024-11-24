from .models import db, City

def consulta_poblacion_promedio():
    # consulta #1: la poblacion promedio entre todas las ciudades en la db
    resultados = db.session.query(
        db.func.avg(City.population).label('poblacion_promedio')
    ).scalar()

    return {'poblacion_promedio': resultados}
