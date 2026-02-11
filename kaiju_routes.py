from flask import Flask, render_template, request, session, redirect, url_for
from battle_engine import (
    init_game_state,
    rebuild_kaiju,
    run_turn,
    persist_state,
    Kaiju,
    kaiju_list
)

app = Flask(__name__)
app.secret_key = "dev"

@app.route("/battle_game", methods=["GET", "POST"])
def battle_game():
    # START GAME (POST from homepage form)
    if request.method == "POST" and (("player" in request.form and "enemy" in request.form) or ("player_name" in request.form and "enemy_name" in request.form)):
        session.clear()
        session["player_name"] = request.form.get("player_name") or request.form["player"]
        session["enemy_name"] = request.form.get("enemy_name") or request.form["enemy"]
        init_game_state(session)
        session.modified = True
        return redirect(url_for("battle_game"))

    # If game not started yet, go back to home
    if "player_name" not in session or "enemy_name" not in session:
        return redirect(url_for("home_page"))

    # Ensure initialized
    init_game_state(session)

    # BATTLE ACTIONS (POST from battle_game.html)
    if request.method == "POST":
        move = request.form.get("move")

        if move == "reset_game":
            session.clear()
            session.modified = True
            return redirect(url_for("home_page"))

        player, enemy = rebuild_kaiju(session)
        turn = session["turn"]

        output = run_turn(player, enemy, move, turn)
        session["log"].extend(output)

        session["turn"] = "enemy" if turn == "player" else "player"
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
        turn=session["turn"],
    )



# App routes for the rest of the pages.

@app.route("/home", methods=["GET", "POST"])
def home_page():
        return render_template(
        "kaiju_battle.html",
        Kaiju=Kaiju,
        kaiju_list=kaiju_list
    )


@app.route("/kaiju_info_pages/<kaiju_name>", methods=["GET", "POST"])
def kaiju_info_pages(kaiju_name):
    return render_template(f"{kaiju_name}_info.html")

if __name__ == "__main__":
     app.run(debug=True)