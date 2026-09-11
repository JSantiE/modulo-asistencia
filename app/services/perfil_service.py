from app.database.db import get_connection

class PerfilService():
    @classmethod
    def list_perfiles(self, empresa_id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.callproc('sp_list_perfil', (empresa_id,))
                rows = cursor.fetchall()
                
                return rows
        except Exception as ex:
            raise Exception(f"Error al listar los perfiles: {ex}")