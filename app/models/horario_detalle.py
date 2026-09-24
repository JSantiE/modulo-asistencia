from flask_login import UserMixin

class Horario_Detalle(UserMixin):
    
    def __init__(self, id, horario_id, dia, hora_trabajo_inicio, hora_trabajo_fin, hora_refrigerio_inicio, hora_refrigerio_fin, minutos_tolerancia_entrada, minutos_tolerancia_salida, minutos_tolerancia_refrigerio, es_nocturno, es_activo = None) -> None:
        self.id = id
        self.horario_id = horario_id
        self.dia = dia
        self.hora_trabajo_inicio = hora_trabajo_inicio
        self.hora_trabajo_fin = hora_trabajo_fin
        self.hora_refrigerio_inicio = hora_refrigerio_inicio
        self.hora_refrigerio_fin = hora_refrigerio_fin
        self.minutos_tolerancia_entrada = minutos_tolerancia_entrada
        self.minutos_tolerancia_salida = minutos_tolerancia_salida
        self.minutos_tolerancia_refrigerio = minutos_tolerancia_refrigerio
        self.es_nocturno = es_nocturno
        self.es_activo = es_activo

    def to_dict(self):
        return {
            'id': self.id,
            'horario_id': self.horario_id,
            'dia': self.dia,
            'hora_trabajo_inicio': self.hora_trabajo_inicio,
            'hora_trabajo_fin': self.hora_trabajo_fin,
            'hora_refrigerio_inicio': self.hora_refrigerio_inicio,
            'hora_refrigerio_fin': self.hora_refrigerio_fin,
            'minutos_tolerancia_entrada': self.minutos_tolerancia_entrada,
            'minutos_tolerancia_salida': self.minutos_tolerancia_salida,
            'minutos_tolerancia_refrigerio': self.minutos_tolerancia_refrigerio,
            'es_nocturno': self.es_nocturno,
            'es_activo': self.es_activo
        }