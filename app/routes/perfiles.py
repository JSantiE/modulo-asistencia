from flask import Blueprint, make_response, render_template, request, redirect, url_for, flash, jsonify
from flask_login import current_user, login_required
from app.models.perfil import Perfil
from app.services.perfil_service import PerfilService
from app.services.usuario_service import UsuarioService

perfiles = (Blueprint('perfiles', __name__))

@perfiles.route('/perfiles')
@login_required
def list():
    empresa_id = current_user.empresa_id
    perfiles_list = PerfilService.list_perfiles(empresa_id)
    return render_template('seguridad/perfiles/list.html', perfiles=perfiles_list)

@perfiles.route('/perfiles/get_perfil', methods=['POST'])
def get_perfil():
    req = request.get_json()
    perfil = PerfilService.get_perfil_by_id(int(req.get('perfil_id')))
    return make_response(jsonify({"perfil": perfil.to_dict()}), 200)

@perfiles.route('/perfiles/crear', methods=["GET", "POST"])
@login_required
def create():
    if request.method == 'GET':
        menu_list = UsuarioService.list_menu()
        return render_template("seguridad/perfiles/formulario.html", menus=menu_list)


@perfiles.route('/perfiles/datos', methods=["GET", "POST"])
@login_required
def datos():
    
    menu_list = UsuarioService.list_menu()
    
    if request.method == 'POST':
        print("POST")
        id = request.form.get('id')
        perfil = PerfilService.get_perfil_by_id(int(id))
        return render_template("seguridad/perfiles/formulario.html", perfil=perfil.to_dict(), menus=menu_list)
    else:
        print("GET")
        return render_template("seguridad/perfiles/formulario.html", perfil=None, menus=menu_list)



@perfiles.route('/perfiles/delete', methods=['POST'])
def delete():
    req = request.get_json()
    perfil = PerfilService.delete_perfil(int(req.get('id')), current_user.empresa_id)
    return render_template('seguridad/perfiles/list.html')