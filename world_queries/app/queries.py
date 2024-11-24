from .models import db, City, Country, CountryLanguage
from sqlalchemy import func, desc

def consulta_poblacion_promedio():
    # consulta #1: la poblacion promedio entre todas las ciudades en la db
    resultados = db.session.query(func.avg(City.Population).label("PoblacionPromedio"))

    return resultados[0][0] #ya que está devolviendo una tupla y sólo queremos el primer elemento

def consulta_ciudades_por_pais():
    # Consulta 2: el número de ciudades que hay por país.
    resultados = (
    db.session.query(
        Country.Name.label("Pais"),  # Nombre del país
        func.count(City.ID).label("NumeroDeCiudades")  # Conteo de ciudades
    )
    .outerjoin(City, Country.Code == City.CountryCode)  # LEFT JOIN entre Country y City
    .group_by(Country.Code, Country.Name)  # Agrupar por código y nombre del país
    .order_by(func.count(City.ID).desc())  # Ordenar por número de ciudades, descendente
)
    return resultados.all()  # Devolver los resultados como una lista

def consulta_lenguajes_por_pais():
    #Consulta 3: el número de lenguajes que se hablan por país sin importar si son oficiales o no
    resultados = (
    db.session.query(
        Country.Name.label("Pais"),  # Nombre del país
        func.count(CountryLanguage.Language).label("NumLenguajes")  # Conteo de lenguajes
    )
    .join(CountryLanguage, Country.Code == CountryLanguage.CountryCode)  # Join entre Country y CountryLanguage
    .group_by(Country.Code, Country.Name)  # Agrupar por país
    .order_by(desc("NumLenguajes"))  # Ordenar por número de lenguajes en orden descendente
)
    return resultados.all()

def consulta_paises_mas_50_millones():
    resultados = (
        db.session.query(Country.Name, Country.Population)
        .filter(Country.Population > 50000000)
        .order_by(Country.Population.desc())
        .all()
    )
    return [{"nombre": r.Name, "poblacion": r.Population} for r in resultados]

# Consulta 5: Idiomas oficiales y porcentaje por país
def consulta_idiomas_por_pais(codigo_pais):
    resultados = (
        db.session.query(CountryLanguage.Language, CountryLanguage.Percentage)
        .filter(CountryLanguage.CountryCode == codigo_pais, CountryLanguage.IsOfficial == 'T')
        .all()
    )
    return [{"idioma": r.Language, "porcentaje": r.Percentage} for r in resultados]

def consulta_todos_los_paises():
    resultados = db.session.query(Country.Name, Country.Code).all()  # Obtener el nombre y código del país
    return resultados
