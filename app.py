from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/analyze")
def analyze():

    btc = requests.get("https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT").json()

    price = float(btc["lastPrice"])
    open_price = float(btc["openPrice"])

    trend = "Bullish" if price > open_price else "Bearish"
    signal = "BUY" if trend == "Bullish" else "SELL"

    return jsonify({
        "asset": "BTCUSDT",
        "price": round(price,2),
        "trend": trend,
        "signal": signal
    })

if __name__ == "__main__":
    app.run()