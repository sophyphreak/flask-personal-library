from flask_restful import Resource, reqparse

from models.book import BookModel
from models.comment import CommentModel


class Book(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("comment_text", type=str, location="form")

    def get(self, book_id):
        return BookModel.find_by_id(book_id).json()

    def post(self, book_id):
        comment_text = Book.parser.parse_args()["comment_text"]
        new_comment = CommentModel(comment_text=comment_text, book_id=book_id)
        new_comment.save_to_db()
        return BookModel.find_by_id(book_id).json()

    def delete(self, book_id):
        book = BookModel.find_by_id(book_id)
        number_of_comments_deleted =  CommentModel.delete_all_from_book(book_id)
        book.delete_from_db()
        return {
            "message": f"1 book ands {number_of_comments_deleted} comments deleted successfully."
        }


class BookList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("title", type=str, location="form")

    def get(self):
        book_list = BookModel.get_all_books()
        return [book.json() for book in book_list]

    def post(self):
        title = BookList.parser.parse_args()["title"]
        new_book = BookModel(title=title)
        new_book.save_to_db()
        return new_book.json()

    def delete(self):
        number_of_books_deleted = BookModel.delete_all_books()
        number_of_comments_deleted = CommentModel.delete_all_comments()
        return {
            "message": f"{number_of_books_deleted} books and {number_of_comments_deleted} comments successfully deleted"
        }
