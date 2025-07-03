from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    migrate = Migrate(app, db)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models so Alembic can detect them
    from app.models import recipe, review, user  

    # Register blueprints
    from app.routes.main_routes import main_bp
    app.register_blueprint(main_bp)
    from app.routes.recipe_route import recipe_bp
    app.register_blueprint(recipe_bp)  
    from app.routes.review_route import review_bp
    app.register_blueprint(review_bp)  
    from app.routes.user_route import user_bp
    app.register_blueprint(user_bp)

    
    return app