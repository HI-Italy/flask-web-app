from datetime import datetime

import requests
from flask import Flask, abort, render_template, request

from constants import COLUMN_MAP, URL
from database import add_row, get_plot_schema, load_db, save_db

app = Flask(__name__)

# Load the dataframe
db = load_db("crypto_data.csv")

# Number of visits of the 'data' page
number_of_visits = 0


@app.route("/")
def index():
    """Main page.

    The main page displays links to all cryptos.
    """

    # To exclude datetime
    crypto_names = db.columns[1:]

    return render_template("index.html", names=crypto_names)


@app.route("/data")
def data():
    """Data page.

    The data page counts the number of visits.
    """

    # It must be global because it cannot be passed as argument.
    global number_of_visits
    number_of_visits += 1

    return render_template("data.html", number_of_visits=number_of_visits)


@app.route("/about_us")
def about_us():
    """About us page.

    Just a simple web page with some random text.
    """

    return render_template("about_us.html")


@app.route("/crypto/<int:index>", methods=["GET", "POST"])
def crypto(index):
    """Cryptocurrency pages.

    To distinguish between cryptos, we use the index
    variable:

    /crypto/0 -> Bitcoin
    /crypto/1 -> Dogecoin
    /crypto/2 -> Ethereum

    The POST method is used to update the price using
    the Binance API. The data we get has this format:
    [
      {
          "symbol":"BTCUSDT",
          "price":"16815.07000000"
      },
      {
          "symbol":"ETHUSDT",
          "price":"1250.00000000"
      },
      {
          "symbol":"DOGEUSDT",
          "price":"0.07365000"
      }
    ]

    Args:
        index (int): Index of the cryptocurrency.
    """

    # Index of the last cryptocurrency
    max_index = len(db.columns) - 2

    # These pages don't exist
    if index > max_index:
        abort(404)

    # Update all prices
    if request.method == "POST":

        # Get the JSON prices of all cryptos through the Binance API.
        results = requests.get(URL)
        results = results.json()

        # After this stage we get:
        # {"BTCUSDT": "1", "DOGEUSDT": "2", "ETHUSDT": "3"}
        unformatted_row = {
            result["symbol"]: result["price"] for result in results
        }

        # Now it will have the shape of a row:
        # {"Bitcoin": 1.0, "Dogecoin": 2.0, "Ethereum": 3.0}
        new_row = {
            COLUMN_MAP[symbol]: float(price)
            for symbol, price in unformatted_row.items()
        }

        # Add date and time to the new row
        new_row["Datetime"] = str(datetime.now())

        # Add the row and save the db as a csv file
        add_row(db, new_row)
        save_db(db, "crypto_data.csv")

    # Name of the crypto specified by the index
    name = db.columns[index + 1]

    # The returned price is 0 if the database is empty
    price = db[name].iloc[-1] if len(db) > 0 else 0.0

    # JSON schema of the plot
    plot_schema = get_plot_schema(db, name)

    return render_template(
        "crypto.html",
        name=name,
        value=price,
        plot_schema=plot_schema,
        index=index,
        max_index=max_index,
    )


# Execute the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
