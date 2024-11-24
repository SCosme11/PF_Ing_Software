from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

#Instancia de SQLAlchemy
db = SQLAlchemy()

def create_app():
    #Crear la aplicación Flask
    app = Flask(__name__)

    #Carga la configuración desde config.py
    app.config.from_object(Config)

    #Inicializa la db
    db.init_app(app)

    with app.app_context():
        from . import views, models  # Importar rutas y modelos
        db.create_all()  # Crear tablas si no existen

    return app
