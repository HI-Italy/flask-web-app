from datetime import datetime

from flask import Flask, render_template

from database import add_row, get_plot_schema, load_db, save_db

app = Flask(__name__)
db = load_db("crypto_data.csv")


@app.route("/")
def index():
    names = db.columns[1:]
    return render_template("index.html", names=names)


@app.route("/today")
def today():
    return f"{datetime.now()}"


@app.route("/crypto/<int:index>")
def crypto(index):
    name = db.columns[index + 1]
    price = db[name].iloc[-1]

    return render_template("crypto.html", name=name, price=price)


if __name__ == "__main__":
    app.run(debug=True)
