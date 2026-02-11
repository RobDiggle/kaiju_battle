# kaiju_battle
Flask-based Pokemon clone battle game using Japanese Kaiju characters featuring turn-based combat, session-managed state, and dynamic battle logs.

Kaiju Battle

A Flask-based turn-based battle game inspired by classic Pokémon mechanics, built using Japanese Kaiju characters. The game features server-side combat logic, session-managed state, and dynamic battle logs.

Features

Select two Kaiju characters

Turn-based attack and defend system

Session-managed game state

Dynamic battle log updates

Reset functionality

Static asset integration (images + audio)

Tech Stack

Python

Flask

Jinja2

HTML / CSS

Session-based state management

How It Works

Character selections are stored in Flask session

init_game_state() initializes health and attack values

Each POST request executes exactly one turn

Game state is rebuilt from session data per request

State is persisted after each move

Battle log dynamically updates until win condition is met

Project Structure
kaiju_battle/
│
├── battle_engine.py      # Game logic
├── kaiju_routes.py       # Flask routes
├── templates/            # HTML templates
├── static/
│   ├── img/              # Kaiju images
│   └── music/            # Background music
└── README.md

Run Locally
pip install -r requirements.txt
flask run


Then visit:

http://127.0.0.1:5000

Future Improvements

Add persistent database (replace session storage)

Add multiplayer support

Deploy to Render / Railway / Fly.io

Add automated tests

Add REST API endpoints
