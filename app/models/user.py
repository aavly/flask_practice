from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    # Relationships
    recipes = db.relationship('Recipe', back_populates='user', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'recipes': [
                {
                    'id': recipe.id,
                    'title': recipe.title,
                    'description': recipe.description,
                    'ingredients': recipe.ingredients
                }
                for recipe in self.recipes
            ]
        }

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"