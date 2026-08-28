from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def index():
    data = {
        "title": "Index",
        "message": "Modulo Asistencia - Prueba estructuración",
    }
    
    return render_template("index.html", data=data)