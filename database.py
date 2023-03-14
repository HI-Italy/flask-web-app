import pandas as pd


def load_db(path):
    """"""
    db = pd.read_csv(path)
    return db


def save_db(db, path):
    db.to_csv(path, index=False)

def add_row(db, row):
    new_index = len(db)
    db.loc[new_index] = row

def get_plot_schema(db, crypto):
    schema = {
        "data" : [
        {
            "x": db["Datetime"].tolist(),
            "y": db[crypto].tolist(),
            "type": "scatter",
            "line": {
                "color": "#d92626",
                "width": 3
                                        }
        }
        ],
        "layout": {
            "width": 1000,
            "xaxis": {"title": "Datetime"},
            "yaxis": {"title": "Price (USD)"}
        }
    }

    return schema


if __name__ == '__main__':

    from datetime import datetime
    import plotly.io as pio

    db = load_db("crypto_data.csv")
    print(db.head())

    # test plots
    schema = get_plot_schema(db, "Bitcoin")
    pio.show(schema)

    new_row = {'Datetime': datetime.now(),
               'Bitcoin': 1.,
               'Dogecoin': 2.,
               'Ethereum': 3.}
    
    add_row(db, new_row)
    print(db.tail())

    save_db(db, "crypto_csv2.csv")
