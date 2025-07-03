from app.models.user import User
from app import db

class UserService:
    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def create_user(username, email, password_hash):
        user = User(
            username=username,
            email=email,
            password_hash=password_hash
        )
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def update_user(user_id, username=None, email=None, password_hash=None):
        user = User.query.get(user_id)
        if not user:
            return None
        if username is not None:
            user.username = username
        if email is not None:
            user.email = email
        if password_hash is not None:
            user.password_hash = password_hash
        db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return False
        db.session.delete(user)
        db.session.commit()