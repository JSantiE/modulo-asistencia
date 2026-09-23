from flask import Blueprint, make_response, render_template, request, redirect, url_for, flash, jsonify
from flask_login import current_user, login_required
from app.models.perfil import Perfil
from app.services.perfil_service import PerfilService

perfiles = (Blueprint('perfiles', __name__))

@perfiles.route('/perfiles')
@login_required
def list():
    try:
        empresa_id = current_user.empresa_id
        perfiles_list = PerfilService.list_perfiles(empresa_id)
        
        return render_template('perfiles.html', perfiles=perfiles_list)
    except Exception as ex:
        return render_template('perfiles.html', perfiles=[])
    
@perfiles.route('/perfiles/get_perfil', methods=['POST'])
def get_perfil():
    req = request.get_json()
    perfil = PerfilService.get_perfil_by_id(int(req.get('perfil_id')))
    return make_response(jsonify({"perfil": perfil.to_dict()}), 200)

@perfiles.route('/perfiles/delete', methods=['POST'])
def delete():
    req = request.get_json()
    perfil = PerfilService.delete_perfil(int(req.get('id')), current_user.empresa_id)
    return render_template('perfiles.html')