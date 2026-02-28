from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"status": "AI Trader Backend is running"})

@app.route("/analyze")
def analyze():
    return jsonify({
        "trend": "Bullish",
        "sentiment": "Positive",
        "summary": "Market momentum is strong.",
        "probability_up": "68%"
    })