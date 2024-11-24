from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    # Registra las rutas
    with app.app_context():
        from .views import register_routes
        register_routes(app)  # Pasamos la instancia de `app` a `views`

    return app
