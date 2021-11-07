from flask import Flask, render_template, redirect, session, request
from flask_app import app
from flask_app.models.dojo import Dojos

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data = {
        "name":request.form["name"],
        "location":request.form["location"],
        "language":request.form["language"],
        "comment":request.form["comment"]
    }
    
    new_id = Dojos.save(data)

    if Dojos.validate_ninja(request.form):
        return redirect(f"/results/{new_id}")
    else:
        return redirect("/")


@app.route("/results/<int:id>")
def results(id):
    data = {
        "id":id
    }
    dojos = Dojos.show_ninja(data)
    return render_template("results.html", dojos=dojos)

@app.route("/Go_back", methods=["POST"])
def goback():
    session.clear()
    return redirect("/")
