# For debugging
from datetime import datetime

import pandas as pd
import plotly.io as pio


def load_db(path):
    """Load the database.

    The 'database' is actually a dataframe read from
    the csv file. It is made of 4 columns:

    - Datetime: Date and time.
    - Bitcoin: Bitcoin price in USDT.
    - Dogecoin: Dogecoin price in USDT.
    - Ethereum: Ethereum price in USDT.

    Args:
        path (str): Path to the csv file.

    Returns:
        db (DataFrame): Our database.
    """

    db = pd.read_csv(path)

    return db


def save_db(db, path):
    """Save the database as a csv file.

    Args:
        db (DataFrame): Database.
        path (str): Path to the csv file.
    """

    db.to_csv(path, index=False)


def add_row(db, row):
    """Add a new row to the database.

    It is required whenever the user updates the
    prices.

    Args:
        db (DataFrame): Database.
        row (dict): New row.
    """

    new_index = len(db)
    db.loc[new_index] = row


def get_plot_schema(db, crypto):
    """Get the Plotly JSON schema.

    Cryptocurrency price graphs are plotted in the
    browser. The JSON schema is used to pass the
    plot information to javascript.

    Args:
        db (DataFrame): Database.
        crypto (str): Cryptocurrency name.

    Returns:
        schema (dict): JSON schema of the plot.
    """

    schema = {
        "data": [
            {
                "x": db["Datetime"].tolist(),
                "y": db[crypto].tolist(),
                "type": "scatter",
                "line": {"color": "#d92626", "width": 3},
            }
        ],
        "layout": {
            "width": 1000,
            "xaxis": {"title": "Datetime"},
            "yaxis": {"title": "Price (USD)"},
        },
    }

    return schema


if __name__ == "__main__":

    # Load and print the DB
    db = load_db("crypto_data.csv")
    print(db.to_string())

    # Plot Bitcoin prices
    schema = get_plot_schema(db, "Bitcoin")
    pio.show(schema)

    # New row
    current_dt = str(datetime.now())
    new_row = {
        "Datetime": current_dt,
        "Bitcoin": 1.0,
        "Dogecoin": 2.0,
        "Ethereum": 3.0,
    }

    # Add the row and save the DB with a different name
    add_row(db, new_row)
    save_db(db, "crypto2.csv")
