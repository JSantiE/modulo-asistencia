from werkzeug.security import check_password_hash
from flask_login import UserMixin

class Usuario(UserMixin):
    
    def __init__(self, id, usuario, contrasena_hash, nombres, empresa_id = None, apellido_paterno = None, apellido_materno = None, perfil_id = None, es_activo = None) -> None:
        self.id = id
        self.empresa_id = empresa_id
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.nombres = nombres
        self.usuario = usuario
        self.contrasena_hash = contrasena_hash
        self.perfil_id = perfil_id
        self.es_activo = es_activo

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'empresa_id': self.empresa_id,
            'apellido_paterno': self.apellido_paterno,
            'apellido_materno': self.apellido_materno,
            'nombres': self.nombres,
            'contrasena_hash': self.contrasena_hash,
            'perfil_id': self.perfil_id
        }