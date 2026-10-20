from flask import json
from app.database.db import get_connection
from app.models.perfil import Perfil

class PerfilService():
    
    @classmethod
    def get_perfil_by_id(self, perfil_id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.callproc('sp_get_perfil_by_id', (perfil_id,))
                row = cursor.fetchone()
                
                if row != None:
                    return Perfil(row[0], row[1], row[2], row[3])
                else:
                    return None
        except Exception as ex:
            raise Exception(f"Error al obtener el perfil por ID: {ex}")
    
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
        
    @classmethod
    def create_perfil(self, perfil, menu):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.callproc('sp_create_perfil', 
                                (
                                    perfil.empresa_id,
                                    perfil.perfil,
                                    json.dumps(menu)
                                ))
                connection.commit()
        except Exception as ex:
            raise Exception(f"Error al crear el perfil: {ex}")
        
    @classmethod
    def update_perfil(self, perfil, menu):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.callproc('sp_update_perfil', 
                                (
                                    perfil.id,
                                    perfil.empresa_id,
                                    perfil.perfil,
                                    json.dumps(menu)
                                ))
                connection.commit()
        except Exception as ex:
            raise Exception(f"Error al actualizar el perfil: {ex}")
        
    @classmethod
    def delete_perfil(self, perfil_id, empresa_id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.callproc('sp_delete_perfil', (perfil_id, empresa_id))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            raise Exception(f"Error al eliminar el perfil: {ex}")
        
    @classmethod
    def list_menus_by_perfil(self, perfil_id, empresa_id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.callproc('sp_list_menus_by_perfil', (perfil_id, empresa_id))
                rows = cursor.fetchall()
                
                menus_seleccionados = [row[0] for row in rows]
                
                return menus_seleccionados
        except Exception as ex:
            raise Exception(f"Error al listar los menús por perfil: {ex}")