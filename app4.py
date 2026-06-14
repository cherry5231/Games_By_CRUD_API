from flask import Flask
from pathlib import Path
import json

app = Flask(__name__)


@app.route("/")
def home():
    file_path = Path(__file__).resolve().parent / "games.json"

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    html = """
    <html>
    <head>
        <title>🎮 Games Dashboard</title>
        <style>
            body {
                font-family: Arial;
                background: #0f0f1a;
                color: white;
                margin: 0;
                padding: 20px;
            }

            h1 {
                text-align: center;
                color: #00ffcc;
            }

            .container {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 20px;
                padding: 20px;
            }

            .card {
                background: #1c1c2b;
                padding: 15px;
                border-radius: 12px;
                box-shadow: 0 0 10px rgba(0,255,204,0.2);
                transition: 0.3s;
            }

            .card:hover {
                transform: scale(1.03);
                box-shadow: 0 0 20px rgba(0,255,204,0.5);
            }

            .title {
                font-size: 18px;
                color: #00ffcc;
                margin-bottom: 10px;
            }

            .info {
                font-size: 14px;
                line-height: 1.5;
                color: #ddd;
            }
        </style>
    </head>
    <body>
        <h1>🎮 Games Dashboard</h1>
        <div class="container">
    """

    for game, info in data.items():
        html += f"""
        <div class="card">
            <div class="title">{game}</div>
            <div class="info">
                <b>Engine:</b> {info.get('Engine')}<br>
                <b>Year:</b> {info.get('Release_year')}<br>
                <b>Company:</b> {info.get('Company')}
                 <b>Major Source Code:</b> {info.get('Major Source Code')}
            </div>
        </div>
        """

    html += """
        </div>
    </body>
    </html>
    """


    return html
