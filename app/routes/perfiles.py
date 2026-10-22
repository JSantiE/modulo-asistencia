from flask import Blueprint, make_response, render_template, request, redirect, url_for, flash, jsonify
from flask_login import current_user, login_required
from app.models.perfil import Perfil
from app.services.perfil_service import PerfilService
from app.services.menu_service import MenuService

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
        menu_list = MenuService.list_menu()
        return render_template("seguridad/perfiles/formulario.html", perfil=None, menus=menu_list)
    
    perfil = Perfil(0, request.form.get('perfil'), current_user.empresa_id)
    menus = [
        int(id_menu)
        for id_menu in request.form.getlist('menus')
    ]
    PerfilService.create_perfil(perfil, menus)
    
    return redirect(url_for('perfiles.list'))

@perfiles.route('/perfiles/editar/<int:id>', methods=["GET", "POST"])
@login_required
def edit(id):
    if request.method == 'POST':
        perfil = Perfil(id, request.form.get('perfil'), current_user.empresa_id)
        menu_seleccionados = [
            int(id_menu)
            for id_menu in request.form.getlist('menus')
        ]
        PerfilService.update_perfil(perfil, menu_seleccionados)    
        return redirect(url_for('perfiles.list'))
        
    perfil = PerfilService.get_perfil_by_id(id)
    menus = MenuService.list_menu()
    menus_perfil = PerfilService.list_menus_by_perfil(id, current_user.empresa_id)
          
    return render_template("seguridad/perfiles/formulario.html", perfil=perfil.to_dict(), menus=menus, menus_perfil=menus_perfil)

@perfiles.route('/perfiles/delete', methods=['POST'])
@login_required
def delete():
    req = request.get_json()
    PerfilService.delete_perfil(int(req.get('id')), current_user.empresa_id)
    return redirect(url_for('perfiles.list'))