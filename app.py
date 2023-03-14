from flask import Flask, render_template, request
from datetime import datetime
from database import load_db, save_db, get_plot_schema, add_row
import requests


db = load_db("crypto_data.csv")
app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    date = str(datetime.now())
    return render_template("data.html", date=date)

@app.route("/crypto/<int:index>", methods=["GET", "POST"])
def crypto(index):

    if request.method == "POST":
        pass

    name = db.columns[index + 1]
    price = db[name].iloc[-1]
    schema = get_plot_schema(db, name)

    return render_template(
        "crypto.html",
        name=name,
        price=price,
        schema=schema,
        index=index
    )




if __name__ == '__main__':
    app.run(debug=True)