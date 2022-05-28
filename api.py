from unittest import result
from flask import Flask, request, make_response
import mysql.connector
import password
app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=password.key,
    database="Library"
)

mycursor = db.cursor()

@app.route("/getallbooks", methods=["GET"])
def getAllBooks():
    if request.method == "GET":
        mycursor.execute("SELECT * FROM Books")
        result = mycursor.fetchall()

        for x in result:
            print(x)
        return str(result)

@app.route("/getbookfromtitle/<title>", methods=["GET"])
def getBookFromTitle(title):
    if request.method == "GET":
        mycursor.execute("SELECT * FROM Books WHERE title=%s", (title,))
        result = mycursor.fetchall()

        for x in result:
            print(x)
        if result == []:
            return "There is no book with this title!"
        else:
            return str(result)

@app.route("/getbookfromauthor/<publisher>", methods=["GET"])
def getBookFromAuthor(publisher):
    if request.method == "GET":
        mycursor.execute("SELECT * FROM Books WHERE publisher=%s", (publisher,))
        result = mycursor.fetchall()

        for x in result: 
            print(x)
        if result == []:
            return "There is no book written by this author!"
        else:
            return str(result)

@app.route("/getbooksfromdate/<year>", methods=["GET"])
def getBookFromYear(year):
    if request.method == "GET":
        mycursor.execute("SELECT * FROM Books WHERE publish_year=%s", (year,))
        result = mycursor.fetchall()

        for x in result:
            print(x)
        if result == []:
            return "There is no book published on this date!"
        else:
            return str(result)

@app.route("/addbook/<title>/<publisher>/<publish_year>", methods=["POST"])
def addBook(title, publisher, publish_year):
    if request.method == "POST":
        sql = "INSERT INTO Books (title, publisher, publish_year) VALUES (%s, %s, %s)"
        val = (title, publisher, publish_year)
        mycursor.execute(sql, val)
        db.commit()
        return "Book added successfully!"

@app.route("/removebook/<bookid>", methods=["DELETE"])
def removeBook(bookid):
    if request.method == "DELETE":
        sql = "DELETE FROM Books WHERE id=" + bookid
        mycursor.execute(sql)
        db.commit()
        return "Book was removed from the library successfully!"


if __name__ == '__main__':
    app.run(debug=True)