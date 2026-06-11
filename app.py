# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

board = ["   " for _ in range(9)]
current_player = " X "


def print_board():
    row1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
    row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
    row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)


def player_move(icon):
    global current_player

    number = 1 if icon == " X " else 2

    print("It's your turn, Player {} ".format(number))
    choice = int(request.form["choice"].strip())

    if board[choice - 1] == "   ":
        board[choice - 1] = icon
    else:
        print()
        print("Number is taken")


def is_victory(icon):
    if (
        (board[0] == board[1] == board[2] == icon)
        or (board[3] == board[4] == board[5] == icon)
        or (board[6] == board[7] == board[8] == icon)
        or (board[0] == board[3] == board[6] == icon)
        or (board[1] == board[4] == board[7] == icon)
        or (board[2] == board[5] == board[8] == icon)
        or (board[0] == board[4] == board[8] == icon)
    ):
        return True
    else:
        return False


def is_draw():
    if "   " not in board:
        print("It's a draw")
        return True
    else:
        return False


@app.route("/")
def index():
    return render_template("index.html", board=board)


@app.route("/make_move", methods=["POST"])
def make_move():
    global current_player

    player_move(current_player)

    if is_victory(current_player):
        result = f"{current_player} wins!"
    elif is_draw():
        result = "It's a draw! Start a new game."
    else:
        current_player = " O " if current_player == " X " else " X "
        result = None

    return render_template("index.html", board=board, result=result)


@app.route("/restart_game", methods=["POST"]) 
def restart_game():
    global board, current_player
    board = ["   " for _ in range(9)]
    current_player = " X "
    return render_template("index.html", board=board, current_player=current_player)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
