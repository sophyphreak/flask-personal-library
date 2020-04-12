from db import db


class BookModel(db.Model):
    __tablename__ = "book"
    _id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    comments = db.relationship("CommentModel")

    def __init__(self, title):
        self.title = title

    def json(self):
        return {
            "_id": self._id,
            "title": self.title,
            "comments": [comment.comment_text for comment in self.comments],
            "commentcount": len(self.comments),
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(_id=_id).first()

    @classmethod
    def get_all_books(cls):
        return cls.query.all()

    @classmethod
    def delete_all_books(cls):
        number_deleted = cls.query.delete()
        db.session.commit()
        return number_deleted

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
