from flask import Flask
from flask_restful import Api
from flask_talisman import Talisman
from flask_cors import CORS
from db import db
import os

from resources.book import Book, BookList

app = Flask(__name__)
Talisman(app)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "sqlite:///personal-library"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(BookList, "/api/books/")
api.add_resource(Book, "/api/books/<book_id>")

if __name__ == "__main__":
    app.run(debug=True)
