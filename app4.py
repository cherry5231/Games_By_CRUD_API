from flask import Flask, jsonify
import json
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
GAMES_FILE = BASE_DIR / "games.json"


@app.route("/")
def home():
    return "Game API is running!"


@app.route("/games", methods=["GET"])
def get_games():
    try:
        with open(GAMES_FILE, "r", encoding="utf-8") as file:
            games = json.load(file)
        return jsonify(games), 200
    except FileNotFoundError:
        return jsonify({"error": "games.json not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON file"}), 500


if __name__ == "__main__":
    app.run(debug=True)