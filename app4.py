from flask import Flask, jsonify
from pathlib import Path
import json

app = Flask(__name__)

@app.route("/")
def home():
    file_path = Path(__file__).resolve().parent / "games.json"

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return jsonify(data)
