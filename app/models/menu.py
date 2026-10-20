class Menu:
    def __init__(self, id, menu, ruta, orden, menu_padre_id, es_activo = None) -> None:
        self.id = id
        self.menu = menu
        self.ruta = ruta
        self.orden = orden
        self.menu_padre_id = menu_padre_id
        self.es_activo = es_activo

    def to_dict(self):
        return {
            'id': self.id,
            'menu': self.menu,
            'ruta': self.ruta,
            'orden': self.orden,
            'menu_padre_id': self.menu_padre_id,
            'es_activo': self.es_activo
        }