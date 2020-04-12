from db import db


class CommentModel(db.Model):
    __tablename__ = "comment"
    _id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.String(80))
    book_id = db.Column(db.Integer, db.ForeignKey("book._id"))

    def __init__(self, comment_text, book_id):
        self.comment_text = comment_text
        self.book_id = book_id

    def json(self):
        return {
            "_id": self._id,
            "comment_text": self.comment_text,
            "book_id": self.book_id,
        }

    @classmethod
    def find_by_book_id(cls, book_id):
        return cls.query.filter_by(book_id=book_id).all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(_id=_id).first()

    def delete_all_from_Book(cls, book_id):
        number_deleted = cls.query.filter_by(book_id=book_id).delete()
        db.session.commit()
        return number_deleted

    @classmethod
    def delete_all_comments(cls):
        number_deleted = cls.query.delete()
        db.session.commit()
        return number_deleted

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
