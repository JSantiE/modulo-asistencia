from flask_login import UserMixin

class Horario(UserMixin):
    
    def __init__(self, id, horario, descripcion, empresa_id = None, es_activo = None) -> None:
        self.id = id
        self.empresa_id = empresa_id
        self.horario = horario
        self.descripcion = descripcion
        self.es_activo = es_activo

    def to_dict(self):
        return {
            'id': self.id,
            'empresa_id': self.empresa_id,
            'horario': self.horario,
            'descripcion': self.descripcion,
            'es_activo': self.es_activo
        }