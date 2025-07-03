from flask import Blueprint, request, jsonify
from app.services.recipe_service import RecipeService

recipe_bp = Blueprint('recipe_bp', __name__, url_prefix='/recipes')

@recipe_bp.route('/', methods=['GET'])
def get_all_recipes():
    recipes = RecipeService.get_all_recipes()
    return jsonify([{
        'id': r.id,
        'title': r.title,
        'description': r.description,
        'ingredients': r.ingredients,
        'user_id': r.user_id
    } for r in recipes])

@recipe_bp.route('/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = RecipeService.get_recipe_by_id(recipe_id)
    if not recipe:
        return jsonify({'error': 'Recipe not found'}), 404
    return jsonify({
        'id': recipe.id,
        'title': recipe.title,
        'description': recipe.description,
        'ingredients': recipe.ingredients,
        'user_id': recipe.user_id
    })

@recipe_bp.route('/', methods=['POST'])
def create_recipe():
    data = request.get_json()
    recipe = RecipeService.create_recipe(
        title=data['title'],
        description=data.get('description'),
        ingredients=data['ingredients'],
        user_id=data['user_id']
    )
    return jsonify({
        'id': recipe.id,
        'title': recipe.title,
        'description': recipe.description,
        'ingredients': recipe.ingredients,
        'user_id': recipe.user_id
    }), 201

@recipe_bp.route('/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    data = request.get_json()
    recipe = RecipeService.update_recipe(
        recipe_id,
        title=data.get('title'),
        description=data.get('description'),
        ingredients=data.get('ingredients')
    )
    if not recipe:
        return jsonify({'error': 'Recipe not found'}), 404
    return jsonify({
        'id': recipe.id,
        'title': recipe.title,
        'description': recipe.description,
        'ingredients': recipe.ingredients,
        'user_id': recipe.user_id
    })

@recipe_bp.route('/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    success = RecipeService.delete_recipe(recipe_id)
    if not success:
        return jsonify({'error': 'Recipe not found'}), 404
    return