# Web applications with Python and Flask

This repository contains the material for the seminar "Web applications with Python and Flask". The project can be downloaded by clicking the "code" button at the top-right corner of the page.

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

For these lectures, we will need to install the following libraries:
- Flask
- Pandas
- Requests
- Plotly

These dependencies can be installed in different ways.

## Manual installation

```bash
pip install flask
pip install pandas
pip install requests
pip install plotly
```

## Environment creation and installation through requirements.txt

The steps required to create and activate a virtual environment depend on the OS of the machine.

### Windows

To create a virtual environment named `.venv`, simply run:

```bat
python -m venv .venv
```

Once the environment is created, one can activate it by running

```bat
.venv\Script\activate.bat
```

### Linux (Debian)

venv may not be provided out of the box. To install venv run:

```bash
sudo apt install python3-venv
```

Then, create the virtual environment through:

```bash
python3 -m venv .venv
```

Finally, the environment can be activated by executing:

```bash
source .venv/Script/activate
```

### Dependency installation

Once the environment is created, all the dependencies can be installed by taking advantage of the `requirements.txt` file

```bash
pip install -r requirements.txt
```

## Conda environment

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

The app can be executed like any other python script:

```bash
python app.py
```

## Plotting

Plotly will allow us to make interactive plots of  the cryptocurrency prices.
To use Plotly inside templates, we must include the following two scripts into our web page:

```html
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3.min.js"></script>
```

## The Binance API

To get real-time cryptocurrency prices, we will use the
[Binance API](https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md).
Specifically, will make GET requests to the following endpoint:

[https://api.binance.com/api/v3/ticker/price?symbols=["ETHUSDT","DOGEUSDT","BTCUSDT"]](https://api.binance.com/api/v3/ticker/price?symbols=["ETHUSDT","DOGEUSDT","BTCUSDT"])


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

where `symbol` represents the cryptocurrency symbol and `price` is the price in USD(T). Notice that:
- Symbols do not correspond to the column labels of our dataframe
- Prices are provided as strings.
