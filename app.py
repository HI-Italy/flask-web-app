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
        URL = 'https://api.binance.com/api/v3/ticker/price?symbols=%5B%22ETHUSDT%22,%22DOGEUSDT%22,%22BTCUSDT%22%5D'
        response = requests.get(URL)
        results = response.json()

        new_row = {result["symbol"]: result["price"]
                   for result in results}
        
        symbol_dict = {
            "BTCUSDT": "Bitcoin",
            "DOGEUSDT": "Dogecoin",
            "ETHUSDT": "Ethereum"
        }
        
        new_row = {symbol_dict[symbol]: float(price)
                   for symbol, price in new_row.items()}
        
        new_row["Datetime"] = str(datetime.now())

        add_row(db, new_row)
        save_db(db, "crypto_data.csv")
    


        print(new_row)




    name = db.columns[index + 1]
    price = db[name].iloc[-1] if len(db) > 0 else 0
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