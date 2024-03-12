from datetime import datetime
import pandas as pd 
import plotly.io as pio

def load_db(path):
    data = pd.read_csv(path)
    return data

def add_row(db, row):
    new_index = len(db)
    db.loc[new_index] = row

def save_db(db, path):
    db.to_csv(path, index=False)

def get_plot_schema(db, crypto):

    schema = {
        'data': [
            {
                "x" : db['Datetime'].tolist(),
                "y" : db[crypto].tolist(),
                "type" : "scatter",
                "line" : {"color": "#d92626", "width": 3}
            }
        ],
        "layout" : {
            "width" : 1000,
            "xaxis" : {"title" : "Datetime"},
            "yaxis" : {"title" : "Price (USD)"}
        }
    }

    return schema

if __name__ == '__main__':
    db = load_db('crypto_data.csv')
    print(db)

    schema = get_plot_schema(db, "Bitcoin")
    pio.show(schema)

    new_row = [datetime.now(), 1, 3, 5]

    add_row(db, new_row)
    print(db)

    save_db(db, 'crypto_data2.csv')
