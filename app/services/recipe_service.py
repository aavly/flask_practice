from app.models.recipe import Recipe
from app import db

class RecipeService:
    @staticmethod
    def get_all_recipes():
        return Recipe.query.all()

    @staticmethod
    def get_recipe_by_id(recipe_id):
        return Recipe.query.get(recipe_id)

    @staticmethod
    def create_recipe(title, description, ingredients, user_id):
        recipe = Recipe(
            title=title,
            description=description,
            ingredients=ingredients,
            user_id=user_id
        )
        db.session.add(recipe)
        db.session.commit()
        return recipe

    @staticmethod
    def update_recipe(recipe_id, title=None, description=None, ingredients=None):
        recipe = Recipe.query.get(recipe_id)
        if not recipe:
            return None
        if title is not None:
            recipe.title = title
        if description is not None:
            recipe.description = description
        if ingredients is not None:
            recipe.ingredients = ingredients
        db.session.commit()
        return recipe

    @staticmethod
    def delete_recipe(recipe_id):
        recipe = Recipe.query.get(recipe_id)
        if not recipe:
            return False
        db.session.delete(recipe)
        db.session.commit()
        return True