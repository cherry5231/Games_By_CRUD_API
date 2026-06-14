# Games_By_CRUD_API


A simple RESTful API built with Flask for managing a collection of games. The application stores data in a JSON file and supports basic CRUD (Create, Read, Update, Delete) operations.
## requirements
* Python
* Flask
* JSON
## Features

* Get all games
* Get a game by ID
* Add a new game
* Update an existing game
* Delete a game
* JSON file-based storage

## Technologies Used

* Python 3
* Flask
* JSON


## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/flask-games-api.git
cd flask-games-api
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python app.py
```

The server will start at:

```text
http://127.0.0.1:5000
```

## API Endpoints

### Get All Games

```http
GET /games
```

### Get Game By ID

```http
GET /games/<id>
```

Example:

```http
GET /games/1
```

### Add a New Game

```http
POST /games
```

Request Body:

```json
{
    "id": 3,
    "name": "FIFA 24",
    "genre": "Sports"
}
```

### Update a Game

```http
PUT /games/<id>
```

Request Body:

```json
{
    "id": 3,
    "name": "EA FC 24",
    "genre": "Sports"
}
```

### Delete a Game

```http
DELETE /games/<id>
```

## Example Response

```json
{
    "message": "Game added successfully",
    "game": {
        "id": 3,
        "name": "FIFA 24",
        "genre": "Sports"
    }
}
```

## Future Improvements

* Input validation
* Error handling enhancements
* Database integration (SQLite/MySQL/PostgreSQL)
* Pagination and filtering
* Unit testing

## Author
https://github.com/cherry5231
Created as a simple Flask CRUD API project for learning REST API development.
