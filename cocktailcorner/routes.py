from flask import render_template
from cocktailcorner import app, db
from cocktailcorner.models import User, Category, Cocktail


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")