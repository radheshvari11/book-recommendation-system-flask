from flask import Flask, render_template, request
from model import recommend
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("data/books.csv")

@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []

    if request.method == "POST":
        book = request.form["book"]
        recommendations = recommend(book)

    books = df["Book"].tolist()

    return render_template(
        "index.html",
        books=books,
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)
