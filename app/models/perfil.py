from flask_login import UserMixin

class Perfil(UserMixin):
    def __init__(self, id, perfil, empresa_id = None, es_activo = None) -> None:
        self.id = id
        self.perfil = perfil
        self.empresa_id = empresa_id
        self.es_activo = es_activo
        
    def to_dict(self):
        return {
            'id': self.id,
            'perfil': self.perfil,
            'empresa_id': self.empresa_id,
            'es_activo': self.es_activo
        }