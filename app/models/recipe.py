from flask_sqlalchemy import SQLAlchemy
from app import db


class Recipe(db.Model):
    """ Recipe Class"""
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    ingredients = db.Column(db.Text, nullable=False)
    
    # Foreign key to User
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relationship to User (owner)
    user = db.relationship('User', back_populates='recipes')

    # this method is used for debugging and logging
    def __repr__(self):
        return f"<Recipe(id={self.id}, title='{self.title}')>"