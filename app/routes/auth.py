from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user, logout_user, login_required
from app.models.usuario import Usuario
from app.services.usuario_service import UsuarioService
from app import login_manager

auth = Blueprint("auth", __name__)

@login_manager.user_loader
def load_user(user_id):
    return UsuarioService.get_user_by_id(user_id)

@auth.route("/login", methods=["GET", "POST"])
def login():
    
    if request.method == "POST":
        user = Usuario(0, request.form["username"], request.form["password"])
        logged_usuer = UsuarioService.login(user)
        
        if logged_usuer != None:
            if logged_usuer.password:
                login_user(logged_usuer)
                return redirect(url_for("auth.home"))
            else:
                flash("Contraseña incorrecta", "danger")
                return render_template("login.html")        
        else:
            flash("Usuario no encontrado", "danger")
            return render_template("login.html")    
        
    else:
        return render_template("login.html")

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route("/home")    
@login_required
def home():
    return render_template("index.html")

def status_401(error):
    return redirect(url_for("auth.login"))

def status_404(error):
    return "<h1>Page Not Found</h1>", 404