from flask import Flask, render_template, Blueprint, redirect, request
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

books_blueprint = Blueprint("books", __name__)


# INDEX
# GET '/books'
@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books=books)




# NEW
# GET '/books/new'
@books_blueprint.route("/books/new", methods = ["GET"])
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors=authors)

# CREATE
# POST '/books'
@books_blueprint.route("/books", methods=["POST"])
def create_book():
    #Grab the form data for description, user_id, duration and completed
    title = request.form['title']
    genre = request.form['genre']
    publisher = request.form['publisher']
    author_id = request.form['author_id']
    #select the user using the repository 
    author = author_repository.select(author_id)
    #create a new task object
    book = Book(title, genre, publisher, author)
    #save that task object back to the database
    book_repository.save(book)

    return redirect('/books')

# SHOW
# GET '/books/<id>'
@books_blueprint.route('/books/<id>')
def show_book(id):
    book = book_repository.select(id)
    return render_template("books/show.html", book=book)

# EDIT
# GET '/books/<id>/edit'


# UPDATE
# PUT '/books/<id>'



# DELETE
# DELETE '/books/<id>'

@books_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')

