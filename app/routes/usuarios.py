from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.usuario import Usuario
from app.services.usuario_service import UsuarioService

usuarios = Blueprint('usuarios', __name__)

@usuarios.route('/usuarios')
@login_required
def list():
    try:
        empresa_id = current_user.empresa_id
        perfil_id = current_user.perfil_id
        usuarios_list = UsuarioService.list_users(empresa_id, perfil_id)
        
        return render_template('usuarios.html', usuarios=usuarios_list)
    except Exception as ex:
        return render_template('usuarios.html', usuarios=[])
    
def create():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            UsuarioService.create_user(data)
            return redirect(url_for('usuarios.list'))
        except Exception as ex:
            return render_template('usuario_form.html', data=data)
    return render_template('usuario_form.html', data={})