from flask import Blueprint, make_response, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from app.models.usuario import Usuario
from app.services.usuario_service import UsuarioService
from app.services.perfil_service import PerfilService

usuarios = Blueprint('usuarios', __name__)

@usuarios.route('/usuarios')
@login_required
def list():
    try:
        empresa_id = current_user.empresa_id
        perfil_id = 0 #current_user.perfil_id
        usuarios_list = UsuarioService.list_users(empresa_id, perfil_id)
        perfiles_list = PerfilService.list_perfiles(empresa_id)
        
        return render_template('usuarios.html', usuarios=usuarios_list, perfiles=perfiles_list)
    except Exception as ex:
        return render_template('usuarios.html', usuarios=[], perfiles=[])

def create():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            UsuarioService.create_user(data)
            return redirect(url_for('usuarios.list'))
        except Exception as ex:
            return render_template('usuario_form.html', data=data)
    return render_template('usuario_form.html', data={})

@usuarios.route('/usuarios/get_user', methods=['POST'])
def get_user():
    req = request.get_json()
    user = UsuarioService.get_user_by_id(int(req.get('id')))
    return make_response(jsonify({"user": user.to_dict()}), 200)

@usuarios.route('/usuarios/delete', methods=['POST'])
def delete():
    req = request.get_json()
    user = UsuarioService.delete_user(int(req.get('id')), current_user.empresa_id)
    return render_template('usuarios.html')