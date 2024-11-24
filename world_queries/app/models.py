from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Column, String, Numeric, ForeignKey, CheckConstraint, DECIMAL, SmallInteger, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class City(db.Model):
    __tablename__='city'

    #Columnas de la tabla
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(35), nullable=False, default='')
    CountryCode = Column(String(3), ForeignKey('country.Code'), nullable=False, default='')
    Population = Column(Integer, nullable=False, default=0)

    #relación con Country
    country = relationship('Country', back_populates='cities')

class Country(db.Model):
    __tablename__='country'

    #Columnas de la tabla
    Code = Column(String(3), primary_key=True, default='')
    Name = Column(String(52), nullable=False, default='')
    Continent = Column(Enum('Asia', 'Europe', 'North America', 'Africa', 'Oceania', 'Antarctica', 'South America'),
                       nullable=False, default='Asia')
    Region = Column(String(26), nullable=False, default='')
    SurfaceArea = Column(DECIMAL(10,2), nullable=False, default=0.00)
    IndepYear = Column(SmallInteger, nullable=True)
    Population = Column(Integer, nullable=False, default=0)
    LifeExpectancy = Column(DECIMAL(3,1), nullable=True)
    GNP = Column(DECIMAL(10,2), nullable=True)
    GNPOld = Column(DECIMAL(10,2), nullable=True)
    LocalName = Column(String(45), nullable=False, default='')
    GovernmentForm = Column(String(45), nullable=False, default='')
    HeadOfState = Column(String(60), nullable=True)
    Capital = Column(Integer, nullable=True)
    Code2 = Column(String(2), nullable=False, default='')

    #relación con city
    cities = relationship('City', back_populates='country')
    #relación con countrylanguage
    languages = relationship('CountryLanguage', back_populates='country')

class CountryLanguage(db.Model):
    __tablename__ = 'countrylanguage'

    # Columnas de la tabla
    CountryCode = Column(String(3), ForeignKey('country.Code'), primary_key=True)
    Language = Column(String(30), primary_key=True)  
    IsOfficial = Column(Enum('T', 'F'), nullable=False, default='F')
    Percentage = Column(DECIMAL(4, 1), nullable=False, default=0.0)

    # Relación con Country
    country = relationship('Country', back_populates='languages')
