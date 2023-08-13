from cocktailcorner import db


class User(db.Model):
    # User Schema
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)
    users = db.relationship("Cocktail", backref="user",
                            cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.username


class Category(db.Model):
    # Category Schema
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.string(25), unique=True, nullable=False)
    cocktails = db.relationship("Cocktail", backref="category",
                                cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.category_name


class Cocktail(db.Model):
    # Cocktail Schema
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    category = db.Column(db.Integer, db.ForeignKey(
        "category.id", ondelete="CASCADE"), nullable=False)
    cocktail_name = db.Column(db.string(50), unique=True, nullable=False)
    ingredients = db.Column(db.string, nullable=False)
    method = db.Column(db.string)
    picture = db.Column(db.string)

    def __repr__(self):
        return self.cocktail_name
