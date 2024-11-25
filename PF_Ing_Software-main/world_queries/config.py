import os #para acceder a las variables de entorno

#clase de config para Flask
class Config:
    #Obtener la URI de la base de datos desde una variable de entorno
    #Si no se encuentra se usa el valor por defecto
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+pymysql://root:Scos1109@localhost/world')
    #desactivar el seguimiento de cambios de la db
    SQLALCHEMY_TRACK_NOTIFICATIONS = False
