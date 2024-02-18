# Binance API
URL = 'https://api.binance.com/api/v3/ticker/price?symbols=["ETHUSDT","DOGEUSDT","BTCUSDT"]'

# Map Binance symbols to column names
COLUMN_MAP = {
    "BTCUSDT": "Bitcoin",
    "DOGEUSDT": "Dogecoin",
    "ETHUSDT": "Ethereum",
}
