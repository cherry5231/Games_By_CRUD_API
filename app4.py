from flask import Flask
from pathlib import Path
import json

app = Flask(__name__)


@app.route("/")
def home():
    file_path = Path(__file__).resolve().parent / "games.json"

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    html = "<h1>🎮 Games Database</h1>"

    for game_name, info in data.items():
        html += f"""
        <div style="
            border:1px solid #ccc;
            padding:10px;
            margin:10px;
            border-radius:10px;
        ">
            <h2>{game_name}</h2>
            <p><b>Engine:</b> {info.get('Engine')}</p>
            <p><b>Release Year:</b> {info.get('Release_year')}</p>
            <p><b>Company:</b> {info.get('Company')}</p>
             <p><b>MajorSourceCode:</b> {info.get('Major Source Code')}</p>
        </div>
        """

    return html
