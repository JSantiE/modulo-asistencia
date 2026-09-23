from flask import Flask
from config import Config
from flask_login import LoginManager

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    
    #Cargar configuración
    app.config.from_object(Config)
    
    login_manager.init_app(app)
    
    #Registrar rutas
    from app.routes.auth import auth, status_401, status_404
    from app.routes.main import main
    from app.routes.usuarios import usuarios
    from app.routes.perfiles import perfiles
        
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(usuarios)
    app.register_blueprint(perfiles)
    
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    
    @app.context_processor
    def inject_menu():
        from app.services.usuario_service import UsuarioService
        menus = UsuarioService.list_menu()
        return {"menus": menus}
    
    return app