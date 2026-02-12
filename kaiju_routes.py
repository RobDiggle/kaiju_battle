from flask import Flask, render_template, request, session, redirect, url_for
# Importing what we need from the battle engine to get the game started.
from battle_engine import (
    Kaiju,
    kaiju_list,
    init_game_state,
    rebuild_kaiju,
    run_turn,
    persist_state,
)

# First line creates the Flask app, second line enables secure sessions.
# Since our game relies on Flask sessions, this is required.
app = Flask(__name__)
app.secret_key = "dev"

# ============================================================================
# 1. THE GAME ROUTE IS CALLED - Inside the route init_game_state(session) is called.
#=============================================================================
@app.route("/battle_game", methods=["GET", "POST"])
def battle_game():
# START GAME (POST from homepage form)
    if request.method == "POST" and "player_name" in request.form and "enemy_name" in request.form:
        session.clear()
        session["player_name"] = request.form.get("player_name") 
        session["enemy_name"] = request.form.get("enemy_name") 
        init_game_state(session)
        session.modified = True
        return redirect(url_for("battle_game"))

# If game not started yet, go back to home
    if "player_name" not in session or "enemy_name" not in session:
        return redirect(url_for("home_page"))

# Ensures the game is initialized
    init_game_state(session)

# BATTLE ACTIONS (POST from battle_game.html)
    if request.method == "POST":
        move = request.form.get("move")

# Reset button on the bottom of the page that returns the players to the homepage and wipes the log clean for a new game.
        if move == "reset_game":
            session.clear()
            session.modified = True
            return redirect(url_for("home_page"))

        player, enemy = rebuild_kaiju(session)

        output = run_turn(player, enemy, move)
        session["log"].extend(output)

        persist_state(session, player, enemy)
        session.modified = True
        return redirect(url_for("battle_game"))

    return render_template(
        "battle_game.html",
        __MARKER__="BATTLE_GAME_TEMPLATE",
        player=session["player_name"],
        enemy=session["enemy_name"],
        player_health=session["player_health"],
        enemy_health=session["enemy_health"],
        log=session["log"],
    )



# App route for the homepage.

@app.route("/home", methods=["GET", "POST"])
def home_page():
        return render_template(
        "kaiju_battle.html",
        Kaiju=Kaiju,
        kaiju_list=kaiju_list
    )

# App route dynamically constructed for the information pages.

@app.route("/kaiju_info_pages/<kaiju_name>", methods=["GET", "POST"])
def kaiju_info_pages(kaiju_name):
    return render_template(f"{kaiju_name}_info.html")

@app.route("/about_game", methods=["GET", "POST"])
def about_game_page():
        return render_template(
        "about_game.html",
        Kaiju=Kaiju,
        kaiju_list=kaiju_list
    )


