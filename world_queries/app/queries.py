from app.models import db, City, Country, CountryLanguage

# Consulta 1: Obtener la población promedio de todas las ciudades
def consulta_poblacion_promedio():
    resultado = db.session.query(db.func.avg(City.Population)).scalar()
    return {"poblacion_promedio": resultado}

# Consulta 2: Listar los países con más de 50 millones de habitantes
def consulta_paises_mas_50_millones():
    resultados = (
        db.session.query(Country.Name, Country.Population)
        .filter(Country.Population > 50000000)
        .order_by(Country.Population.desc())
        .all()
    )
    return [{"nombre": r.Name, "poblacion": r.Population} for r in resultados]

# Consulta 3: Idiomas oficiales y porcentaje por país
def consulta_idiomas_por_pais(codigo_pais):
    resultados = (
        db.session.query(CountryLanguage.Language, CountryLanguage.Percentage)
        .filter(CountryLanguage.CountryCode == codigo_pais, CountryLanguage.IsOfficial == 'T')
        .all()
    )
    return [{"idioma": r.Language, "porcentaje": r.Percentage} for r in resultados]
