from flask import Blueprint, jsonify, request
from app.services.review_service import ReviewService

review_bp = Blueprint('review_bp', __name__, url_prefix='/reviews')

@review_bp.route('/reviews', methods=['GET'])
def get_reviews():
    """Get all reviews."""
    reviews = ReviewService.get_all_reviews()
    return jsonify([review.to_dict() for review in reviews]), 200

@review_bp.route('/reviews/<int:review_id>', methods=['GET'])
def get_review(review_id):
    """Get a specific review by ID."""
    review = ReviewService.get_review_by_id(review_id)
    if review:
        return jsonify(review.to_dict()), 200
    else:
        return jsonify({"error": "Review not found"}), 404

@review_bp.route('/reviews', methods=['POST'])
def create_review():
    """Create a new review."""
    data = request.json
    if not data or 'main_review' not in data or 'star_rating' not in data:
        return jsonify({"error": "Invalid input"}), 400
    review = ReviewService.create_review(data['main_review'], data['star_rating'])
    return jsonify(review.to_dict()), 201

@review_bp.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    """Delete a review by ID."""
    success = ReviewService.delete_review(review_id)
    if success:
        return jsonify({"message": "Review deleted successfully"}), 200
    else:
        return jsonify({"error": "Review not found"}), 404

