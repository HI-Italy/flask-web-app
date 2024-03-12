from datetime import datetime

import requests
from flask import Flask, redirect, render_template, url_for

from constants import COLUMN_MAP, URL
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


@app.route("/update/<int:index>")
def update(index):

    response = requests.get(URL)
    response_json = response.json()

    # 1
    row = {res["symbol"]: res["price"] for res in response_json}
    print(row)

    # 2-3
    row = {COLUMN_MAP[symbol]: float(price) for symbol, price in row.items()}
    print(row)

    # 4
    row["Datetime"] = str(datetime.now())
    print(row)

    add_row(db, row)
    save_db(db, "crypto_data.csv")

    return redirect(url_for("crypto", index=index))


@app.route("/crypto/<int:index>")
def crypto(index):
    name = db.columns[index + 1]
    price = db[name].iloc[-1]
    schema = get_plot_schema(db, name)

    return render_template(
        "crypto.html", name=name, price=price, schema=schema, index=index
    )


if __name__ == "__main__":
    app.run(debug=True)
