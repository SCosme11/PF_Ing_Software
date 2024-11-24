from . import db
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DECIMAL, SmallInteger
from sqlalchemy.orm import declarative_base, relationship
class Country(db.Model):
    __tablename__ = 'country'

    # Columnas de la tabla country
    Code = Column(String(3), primary_key=True)  # Llave primaria
    Name = Column(String(52), nullable=False, default='')  # Nombre del país
    Continent = Column(
        Enum('Asia', 'Europe', 'North America', 'Africa', 'Oceania', 'Antarctica', 'South America'),
        nullable=False,
        default='Asia'
    )  # Continente
    Region = Column(String(26), nullable=False, default='')  # Región
    SurfaceArea = Column(DECIMAL(10, 2), nullable=False, default=0.00)  # Área superficial
    IndepYear = Column(SmallInteger, nullable=True)  # Año de independencia
    Population = Column(Integer, nullable=False, default=0)  # Población
    LifeExpectancy = Column(DECIMAL(3, 1), nullable=True)  # Expectativa de vida
    GNP = Column(DECIMAL(10, 2), nullable=True)  # Producto nacional bruto
    GNPOld = Column(DECIMAL(10, 2), nullable=True)  # Producto nacional bruto anterior
    LocalName = Column(String(45), nullable=False, default='')  # Nombre local
    GovernmentForm = Column(String(45), nullable=False, default='')  # Forma de gobierno
    HeadOfState = Column(String(60), nullable=True)  # Jefe de estado
    Capital = Column(Integer, nullable=True)  # ID de la capital
    Code2 = Column(String(2), nullable=False, default='')  # Código alternativo

    # Relación con CountryLanguage
    languages = relationship('CountryLanguage', back_populates='country')

class City(db.Model):
    __tablename__ = 'city'  # Nombre de la tabla

    # Definición de columnas
    ID = Column(Integer, primary_key=True, autoincrement=True)  # Llave primaria, autoincremental
    Name = Column(String(35), nullable=False, default='')  # Nombre de la ciudad
    CountryCode = Column(String(3), ForeignKey('country.Code'), nullable=False, default='')  # Clave foránea
    District = Column(String(20), nullable=False, default='')  # Distrito
    Population = Column(Integer, nullable=False, default=0)  # Población

    # Relación con la tabla `country`
    country = relationship('Country', back_populates='cities')

class CountryLanguage(db.Model):
    __tablename__ = 'countrylanguage'

    # Columnas de la tabla countrylanguage
    CountryCode = Column(String(3), ForeignKey('country.Code'), primary_key=True)  # Llave foránea
    Language = Column(String(30), primary_key=True)  # Nombre del idioma
    IsOfficial = Column(Enum('T', 'F'), nullable=False, default='F')  # Si es oficial
    Percentage = Column(DECIMAL(4, 1), nullable=False, default=0.0)  # Porcentaje de hablantes

    # Relación con Country
    country = relationship('Country', back_populates='languages')



