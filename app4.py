from flask import Flask
from pathlib import Path
import json

app = Flask(__name__)

@app.route("/")
def home():
    file_path = Path(__file__).resolve().parent / "games.json"

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return f"""
    <html>
    <head>
        <title>Games API</title>
    </head>
    <body>
        <h2>Games Data</h2>
        <pre>{json.dumps(data, indent=4, ensure_ascii=False)}</pre>
    </body>
    </html>
    """
