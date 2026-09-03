from app.database.db import get_connection
from app.models.usuario import Usuario

class UsuarioService():
    
    @classmethod
    def login(self, user):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                query = "SELECT id, usuario, contrasena_hash, nombres FROM usuario WHERE usuario = '{}'".format(user.username)
                cursor.execute(query)
                row = cursor.fetchone()
                
                if row != None:
                    user = Usuario(row[0], row[1], Usuario.check_password(row[2], user.password), row[3])
                    return user
                else:
                    return None
        except Exception as ex:
            raise Exception(f"Error al autenticar el usuario: {ex}")

    @classmethod
    def get_user_by_id(self, user_id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                query = "SELECT id, usuario, nombres FROM usuario WHERE id = '{}'".format(user_id)
                cursor.execute(query)
                row = cursor.fetchone()
                
                if row != None:
                    return Usuario(row[0], row[1], None, row[2])
                else:
                    return None
        except Exception as ex:
            raise Exception(f"Error al obtener el usuario por ID: {ex}")
