from . import db

class Country(db.Model):
    __tablename__ = 'country'
    code = db.Column(db.String(3), primary_key=True)
    name = db.Column(db.String(52), nullable=False)
    continent = db.Column(db.String(50), nullable=False)
    population = db.Column(db.Integer, nullable=False)

class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(35), nullable=False)
    countrycode = db.Column(db.String(3), db.ForeignKey('country.code'))
    population = db.Column(db.Integer, nullable=False)

class CountryLanguage(db.Model):
    __tablename__ = 'countrylanguage'
    countrycode = db.Column(db.String(3), db.ForeignKey('country.code'), primary_key=True)
    language = db.Column(db.String(30), primary_key=True)
    isofficial = db.Column(db.Boolean, nullable=False)
    percentage = db.Column(db.Float, nullable=False)

