from app.models.review import Review, db

class ReviewService:
    @staticmethod
    def create_review(text_review, star_rating):
        review = Review(text_review=text_review, star_rating=star_rating)
        db.session.add(review)
        db.session.commit()
        return review

    @staticmethod
    def get_review_by_id(review_id):
        return Review.query.get(review_id)

    @staticmethod
    def get_all_reviews():
        return Review.query.all()

    @staticmethod
    def update_review(review_id, text_review=None, star_rating=None):
        review = Review.query.get(review_id)
        if not review:
            return None
        if text_review is not None:
            review.text_review = text_review
        if star_rating is not None:
            review.star_rating = star_rating
        db.session.commit()
        return review

    @staticmethod
    def delete_review(review_id):
        review = Review.query.get(review_id)
        if not review:
            return False
        db.session.delete(review)
        db.session.commit()
        return True