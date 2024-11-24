from .models import db, City

def consulta_poblacion_promedio():
    # Consulta de ejemplo: Población promedio por ciudad
    resultados = db.session.query(
        db.func.avg(City.population).label('poblacion_promedio')
    ).scalar()

    return {'poblacion_promedio': resultados}
