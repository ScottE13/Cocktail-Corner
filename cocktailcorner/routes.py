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


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        # Check to see if the username exists
        existing_user = User.query.filter(User.username ==
                                          request.form.get(
                                              "username").lower()).all()

        if existing_user:
            request.form.get("username")
            if check_password_hash(
                    existing_user[0].password, request.form.get("password")):
                session["current_user"] = request.form.get("username").lower()
                return redirect(url_for("account", username=session["current_user"]))

            else:
                # Password Incorrect
                flash('Invalid Username or Password.')
                return redirect(url_for("log_in"))
        else:
            # Username Incorrect
            flash('Invalid Username or Password.')
            return redirect(url_for("log_in"))

    return render_template("log_in.html")

@app.route("/account/<username>", methods=["GET", "POST"])
def account(username):
    if "current_user" in session:
        return render_template("account.html", username=session["current_user"])

    return redirect(url_for("log_in"))

@app.route("/log_out")
def logout():
    # Remove user from the session
    session.pop("current_user")
    session.pop('_flashes', None)
    flash("You have successfully logged out!")
    return redirect(url_for("log_in"))

@app.route("/manage_categories")
def manage_categories():
    # Only allow site owner to access this page
    if "current_user" in session and session["current_user"] == "_owner":
        categories = list(Category.query.order_by(Category.category_name).all())
        return render_template("manage_categories.html", categories=categories)
    else:
        return redirect(url_for("log_in"))

@app.route("/add_category", methods=["GET", "POST"])
def add_category():

    if "current_user" in session and session["current_user"] == "_owner" and request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        flash("Category added successfully.")
        return redirect(url_for("manage_categories"))
    else:
        return redirect(url_for("log_in"))