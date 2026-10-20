from flask import json
from app.database.db import get_connection
from app.models.menu import Menu

class MenuService():
    @classmethod
    def list_menu(self):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.callproc('sp_list_menu')
                rows = cursor.fetchall()
                
                return rows
        except Exception as ex:
            raise Exception(f"Error al listar los menús: {ex}")