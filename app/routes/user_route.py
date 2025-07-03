from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

user_bp = Blueprint('user_bp', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
def get_all_users():
    users = UserService.get_all_users()
    return jsonify([{
        'id': u.id,
        'username': u.username,
        'email': u.email
    } for u in users])

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email
    })

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    user = UserService.create_user(
        username=data['username'],
        email=data['email'],
        password_hash=data['password_hash']
    )
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email
    }), 201

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = UserService.update_user(
        user_id,
        username=data.get('username'),
        email=data.get('email'),
        password_hash=data.get('password_hash')
    )
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email
    })

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    success = UserService.delete_user(user_id)
    if not success:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'message': 'User deleted'})