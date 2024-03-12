from datetime import datetime

from flask import Flask, redirect, render_template, url_for

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
