from flask import flash, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from cocktailcorner import app, db
from cocktailcorner.models import User, Category, Cocktail


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check to see if the username already exists
        existing_user = User.query.filter(User.username ==
                                          request.form.get(
                                            "username").lower()).all()

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # Check that the passwords match
        password_one = request.form.get("password")
        password_two = request.form.get("password2")

        if password_one != password_two:
            flash("Passwords must match")
            return redirect(url_for("register"))

        current_user = User(
            username=request.form.get("username").lower(),
            password=generate_password_hash(request.form.get("password"))
        )

        db.session.add(current_user)
        db.session.commit()

        # Add user to the session
        session["current_user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("account", username=session["current_user"]))
    return render_template("register.html")


@app.route("/log_in")
def log_in():
    return render_template("log_in.html")

@app.route("/account/<username>", methods=["GET", "POST"])
def account(username):
    if "current_user" in session:
        return render_template("account.html", username=session["current_user"])

    return redirect(url_for("login"))