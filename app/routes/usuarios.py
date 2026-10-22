from flask import Blueprint, make_response, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.security import generate_password_hash
from flask_login import login_required, current_user
from app.models.usuario import Usuario
from app.services.usuario_service import UsuarioService
from app.services.perfil_service import PerfilService
from app.services.menu_service import MenuService

usuarios = Blueprint('usuarios', __name__)

@usuarios.route('/usuarios')
@login_required
def list():
    perfil_id = 0 #current_user.perfil_id
    usuarios_list = UsuarioService.list_users(int(current_user.empresa_id), perfil_id)
    perfiles_list = PerfilService.list_perfiles(int(current_user.empresa_id))
    return render_template('seguridad/usuarios/list.html', usuarios=usuarios_list, perfiles=perfiles_list)

@usuarios.route('/usuarios/get_user', methods=['POST'])
def get_user():
    req = request.get_json()
    user = UsuarioService.get_user_by_id(int(req.get('id')))
    return make_response(jsonify({"user": user.to_dict()}), 200)

@usuarios.route('/usuarios/crear', methods=["GET", "POST"])
@login_required
def create():
    if request.method == 'GET':
        perfiles_list = PerfilService.list_perfiles(int(current_user.empresa_id))
        menu_list = MenuService.list_menu()
        return render_template("seguridad/usuarios/formulario.html", user=None, perfiles=perfiles_list, menus=menu_list)
    
    usuario_generado = generar_usuario(request.form.get('apellido_paterno'), request.form.get('apellido_materno'), request.form.get('nombres'))
    contrasena_generada = generate_password_hash(usuario_generado);
    user = Usuario(0, usuario_generado, contrasena_generada, request.form.get('nombres'), current_user.empresa_id, request.form.get('apellido_paterno'), request.form.get('apellido_materno'), request.form.get('perfil_id'), None)
    UsuarioService.create_user(user)
    
    return redirect(url_for('usuarios.list'))

@usuarios.route('/usuarios/editar/<int:id>', methods=["GET", "POST"])
@login_required
def edit(id):
    if request.method == 'POST':
        user = Usuario(int(id), None, None, request.form.get('nombres'), current_user.empresa_id, request.form.get('apellido_paterno'), request.form.get('apellido_materno'), request.form.get('perfil_id'), None)
        UsuarioService.update_user(user)    
        return redirect(url_for('usuarios.list'))
        
    user = UsuarioService.get_user_by_id(id)
    menus = MenuService.list_menu()
    perfiles_list = PerfilService.list_perfiles(int(current_user.empresa_id))
    
          
    return render_template("seguridad/usuarios/formulario.html", user=user.to_dict(), perfiles=perfiles_list, menus=menus)












@usuarios.route('/usuarios/datos', methods=['POST'])
@login_required
def datos():
    id = request.form.get('id')
    user = UsuarioService.get_user_by_id(int(id))
    perfiles_list = PerfilService.list_perfiles(int(current_user.empresa_id))
    menu_list = MenuService.list_menu()
    return render_template("seguridad/usuarios/formulario.html", user=user.to_dict(), perfiles=perfiles_list, menus=menu_list)

@usuarios.route('/usuarios/create', methods=['POST'])
def creates():
    req = request.get_json()
    usuario_generado = generar_usuario(req.get('apellido_paterno'), req.get('apellido_materno'), req.get('nombres'))
    contrasena_generada = generate_password_hash(usuario_generado);
    user = Usuario(0, usuario_generado, contrasena_generada, req.get('nombres'), current_user.empresa_id, req.get('apellido_paterno'), req.get('apellido_materno'), req.get('perfil_id'), None)
    create_user = UsuarioService.create_user(user)
    
    if create_user != None:
        return make_response(jsonify({"success": True}), 200)
    else:
        return make_response(jsonify({"success": False}), 400)

@usuarios.route('/usuarios/update', methods=['POST'])
def update():
    req = request.get_json()
    user = Usuario(int(req.get('id')), None, None, req.get('nombres'), current_user.empresa_id, req.get('apellido_paterno'), req.get('apellido_materno'), req.get('perfil_id'), None)
    update_user =  UsuarioService.update_user(user)
     
    if  update_user != None:
        return make_response(jsonify({"success": True}), 200)
    else:
        return make_response(jsonify({"success": False}), 400)

@usuarios.route('/usuarios/delete', methods=['POST'])
def delete():
    req = request.get_json()
    delete_user = UsuarioService.delete_user(int(req.get('id')), current_user.empresa_id)
    
    if delete_user != None:
        return make_response(jsonify({"success": True}), 200)
    else:
        return make_response(jsonify({"success": False}), 400)
    
def generar_usuario(apellido_P, apellido_M, nombres):
    primer_apellido = apellido_P[:2].lower()
    segundo_apellido = apellido_M[:2].lower()
    primer_nombre = nombres[:2].lower()
    return f"{primer_apellido}{segundo_apellido}{primer_nombre}"