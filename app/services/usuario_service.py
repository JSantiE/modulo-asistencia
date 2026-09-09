from app.database.db import get_connection
from app.models.usuario import Usuario

class UsuarioService():
    
    @classmethod
    def login(self, user):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                query = "SELECT id, usuario, contrasena_hash, nombres FROM usuario WHERE usuario = '{}'".format(user.usuario)
                cursor.execute(query)
                row = cursor.fetchone()
                
                if row != None:
                    user = Usuario(row[0], row[1], Usuario.check_password(row[2], user.contrasena_hash), row[3], None, None, None, None, None)
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
                query = "SELECT id, usuario, nombres, empresa_id, perfil_id FROM usuario WHERE id = '{}'".format(user_id)
                cursor.execute(query)
                row = cursor.fetchone()
                
                if row != None:
                    return Usuario(row[0], row[1], None, row[2], row[3], None, None, row[4], None)
                else:
                    return None
        except Exception as ex:
            raise Exception(f"Error al obtener el usuario por ID: {ex}")
        
    @classmethod
    def list_users(self, empresa_id, perfil_id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.callproc('sp_list_usuario', (empresa_id, perfil_id))
                rows = cursor.fetchall()
                
                return rows
        except Exception as ex:
            raise Exception(f"Error al listar los usuarios: {ex}")
        
    @classmethod
    def create_user(self, user):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.callproc('sp_create_usuario', 
                                (
                                    user.empresa_id, 
                                    user.apellido_paterno,
                                    user.apellido_materno,
                                    user.nombres,
                                    user.contrasena_hash,
                                    user.perfil_id))
                connection.commit()
                return cursor.lastrowid
        except Exception as ex:
            raise Exception(f"Error al crear el usuario: {ex}")
        
    @classmethod
    def update_user(self, user):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.callproc('sp_update_usuario', 
                                (
                                    user.id,
                                    user.empresa_id, 
                                    user.apellido_paterno,
                                    user.apellido_materno,
                                    user.nombres,
                                    user.contrasena_hash,
                                    user.perfil_id))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            raise Exception(f"Error al actualizar el usuario: {ex}")
    