from flask import Blueprint, flash, redirect, render_template, request, url_for
from app.repositories.crud import *
bp = Blueprint("main",__name__)

@bp.route("/")
def index():
    return render_template("home.html")

@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        dato1 = request.form.get("dato1")
        crea(dato1)
        return redirect(url_for('main.index'))
    return render_template("create.html")

@bp.route("/read")
def read():
    dati = ottieni_dati()
    return render_template("read.html", dati=dati)

@bp.route("/delete", methods=("GET", "POST"))
def delete():
    dati = ottieni_dati()

    if request.method == "POST":
        dato1 = request.form.get("id")
        cancella(dato1)
        return redirect(url_for('main.index'))
    
    return render_template("delete.html", dati=dati)

@bp.route("/update/<int:id>", methods=("GET", "POST"))
def update(id):
    db = get_db()
    query = "SELECT * FROM tabella WHERE id = ?"
    dato_vecchio = db.execute(query, (id,)).fetchone()
    print(dato_vecchio)

    if request.method == "POST":
        nuovo_valore = request.form.get("dato1")
        if nuovo_valore:
            aggiorna(id, nuovo_valore)
        return redirect(url_for("main.index"))
    
    return render_template("update.html", dato_vecchio=dato_vecchio)