from flask import Blueprint, redirect, url_for
from app.models.usuario import Usuario
from app.services.usuario_service import UsuarioService

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return redirect(url_for('auth.login'))