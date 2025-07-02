from flask_sqlalchemy import SQLAlchemy
from app import db

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text_review = db.Column(db.Text, nullable=False)  # The main review text
    star_rating = db.Column(db.Integer, nullable=False)  # Star rating, e.g., 1-5

    # Foreign keys
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relationships (optional, for easier access)
    recipe = db.relationship('Recipe', backref='reviews')
    user = db.relationship('User', backref='reviews')

    # this method is used for debugging and logging
    def __repr__(self):
        return f"<Review(id={self.id}, star_rating={self.star_rating})>"
