from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"status": "AI Trader Backend is running"})

@app.route("/analyze")
def analyze():

    # Exempeldata (vi förenklar så vi vet att det funkar)
    result = {
        "trend": "Bullish",
        "sentiment": "Positive",
        "summary": "Market momentum is strong.",
        "probability_up": "68%"
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run()