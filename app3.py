
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

GAMES_FILE = "games.json"


def load_games():
    if not os.path.exists(GAMES_FILE):
        return []

    with open(GAMES_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_games(games):
    with open(GAMES_FILE, "w", encoding="utf-8") as file:
        json.dump(games, file, indent=4)


# Load games when the app starts
games = load_games()


@app.route("/games", methods=["GET"])
def get_games():
    return jsonify(games), 200


@app.route("/games/<int:game_id>", methods=["GET"])
def get_game(game_id):
    game = next((g for g in games if g.get("id") == game_id), None)

    if not game:
        return jsonify({"error": "Game not found"}), 404

    return jsonify(game), 200


@app.route("/games", methods=["POST"])
def add_game():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    games.append(data)
    save_games(games)

    return jsonify({
        "message": "Game added successfully",
        "game": data
    }), 201


@app.route("/games/<int:game_id>", methods=["PUT"])
def update_game(game_id):
    game_index = next(
        (i for i, g in enumerate(games) if g.get("id") == game_id),
        None
    )

    if game_index is None:
        return jsonify({"error": "Game not found"}), 404

    data = request.get_json()

    games[game_index] = data
    save_games(games)

    return jsonify({
        "message": "Game updated successfully"
    }), 200


@app.route("/games/<int:game_id>", methods=["DELETE"])
def delete_game(game_id):
    game_index = next(
        (i for i, g in enumerate(games) if g.get("id") == game_id),
        None
    )

    if game_index is None:
        return jsonify({"error": "Game not found"}), 404

    deleted_game = games.pop(game_index)
    save_games(games)

    return jsonify({
        "message": "Game deleted successfully",
        "deleted_game": deleted_game
    }), 200


if __name__ == "__main__":
    app.run(debug=True)

