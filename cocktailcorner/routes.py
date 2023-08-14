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

        current_user = User(
            username=request.form.get("username").lower(),
            password=generate_password_hash(request.form.get("password"))
        )

        db.session.add(current_user)
        db.session.commit()

        # Add user to the session
        session["current_user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("register", username=session["current_user"]))
    return render_template("register.html")
