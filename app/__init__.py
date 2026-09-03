from flask import Flask
from config import Config
from flask_login import LoginManager

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    
    login_manager.init_app(app)
    
    #Cargar configuración
    app.config.from_object(Config)
    
    #Registrar rutas
    from app.routes.main import main
    
    app.register_blueprint(main)
    
    
    return app