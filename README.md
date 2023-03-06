# Web applications with Python and Flask

This repository contains the material for the "Web applications with Python and Flask" seminar.
You can download the project by clicking the "code" button at the top-right corner of the page.

## Repository structure

```
python_web_app
│   README.md
│   crypto_data.csv 
│   environment.yml
│   requirements.txt
│   .gitignore (ignore this file)
│   
└───static
│      uniupo_logo.svg
│      favicon-32x32.png
│      style.css
│   
└───templates
       .gitkeep (ignore this file)
```

## Required libraries

For these lectures, we will need the following libraries:
- flask
- pandas
- requests
- plotly

These dependencies can be installed in different ways.

### Manual installation

```bash
pip install flask
pip install pandas
pip install requests
pip install plotly
```

### Installation via requirements.txt

```bash
pip install -r requirements.txt
```

### Conda environment

You can create a conda environment named `web_app_env` that contains all these libraries
through the `environment.yml` file located in the root folder. To do this, simply run:

```bash
conda env create -f environment.yml
```

The environment can then be activated by running the following command:

```bash
conda activate web_app_env
```

## App execution

To execute the app, simply run:

```bash
python app.py
```

## Plotting

We will use Plotly to make interactive plots of cryptocurrency prices.
For this reason, we must include the following two scripts into our web page:

```html
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3.min.js"></script>
```

## The Binance API

To get real-time cryptocurrency prices, we will use the
[Binance API](https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md)
We will make GET requests to:

```
https://api.binance.com/api/v3/ticker/price?symbols=["ETHUSDT","DOGEUSDT","BTCUSDT"]
```

The data we receive is a JSON having the following shape:

```js
[
    {
        "symbol":"BTCUSDT",
        "price":"29316.60000000"
    },
    {
        "symbol":"ETHUSDT",
        "price":"1969.81000000"
    },
    {
        "symbol":"DOGEUSDT",
        "price":"0.08400000"
    }
]
```

where `symbol` corresponds to the cryptocurrency and `price` is the price in USD(T). Notice that:
- Symbols do not correspond to the column labels of our dataframe
- Prices are provided as strings.
