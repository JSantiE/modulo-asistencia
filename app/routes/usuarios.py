from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.usuario import Usuario
from app.services.usuario_service import UsuarioService

usuarios = Blueprint('usuarios', __name__)

@usuarios.route('/usuario')
def usuario():
    try:
        empresa_id = 1 #request.args.get('empresa_id')
        perfil_id = 1 #request.args.get('perfil_id')
        usuarios_list = UsuarioService.list_users(empresa_id, perfil_id)
        return render_template('usuarios.html', usuarios=usuarios_list)
    except Exception as ex:
        flash(f"Error al listar los usuarios: {ex}", "danger")
        return render_template('usuarios.html', usuarios=[])