from flask import Blueprint, jsonify, abort, make_response

class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "Hello Book", "A fantasy novel"),
    Book(2, "Horrors of Flask", "A horror novel."),
    Book(3, "Who dunder init?", "A suspense novel.")
]

books_bp = Blueprint("books", __name__, url_prefix="/books")

def validate_book(book_id):
    # handle invalid book_id, return 400
    try:
        book_id = int(book_id)
    except:
        abort(make_response({"message":f"Book {book_id} is invalid"}, 400))
    # search for book_id in data, return book 
    for book in books:
        if book.id == book_id:
            return book
    # return a 404 for non-existing book 

    abort(make_response({"message":f"Book {book_id} is not found"}, 404))

@books_bp.route("", methods = ["GET"])
def handle_books():
    books_response = []
    for book in books:
        books_response.append({
            "id" : book.id,
            "title" : book.title,
            "description" : book.description
        })
    return jsonify(books_response), 200

@books_bp.route("/<book_id>", methods=["GET"])
def handle_book(book_id):
    book = validate_book(book_id)

    return{
        "id": book.id,
        "title": book.title, 
        "description": book.description,
            }
    