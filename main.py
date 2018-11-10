from tkinter import *
from helper import *
turns = 0

window = Tk()

window.title('Tic-Tac-Toe')
board = [[None, None, None], [None, None, None], [None, None, None]]

def make_a_play(r, c):
    global turns
    player = 'X' if turns%2==0 else 'O'
    # print(board[r][c]['text'], player)

    if board[r][c]['text'] == "":
        board[r][c]['text'] = player
        turns += 1
        info_string.set("")
        player_string.set(str("Player " + str(1 if turns%2==0 else 2) + "'s Turn"))
        if check_for_winner(board, player, r, c):
            # print("\n**** PLAYER",str('2' if turns%2==0 else '1'), " WINS ****\n")
            player_string.set(str("MATCH ENDED"))
            info_string.set(str("**** PLAYER " + str('2' if turns%2==0 else '1') + " WINS****"))
            disable_board()
            return

    else:
        info_string.set("Invalid play. Try again")
        # print("Invalid play. Try again\n")

    if turns == 9:
        # print("TIE")
        player_string.set(str("MATCH ENDED"))
        info_string.set(str("**** DRAW ****"))
        disable_board()


def make_board():
    for i in range(3):
        for j in range(3):
            board[i][j] = Button(window, text="", height=10, width=20, command = lambda _i=i, _j=j: make_a_play(_i, _j))
            board[i][j].config(state = "normal")
            board[i][j].grid(row=i+2,column=j)


def disable_board():
    for i in range(3):
        for j in range(3):
            board[i][j].config(state = "disabled")


def reset():
    global turns
    make_board()
    turns = 0
    player_string.set(str("Player 1's Turn"))
    info_string.set("")
    return


player_string = StringVar()
player_string.set(str("Player 1's Turn"))
player_label = Label(window,textvariable=player_string, relief="flat", width=60, height=2)
player_label.grid(row=0, columnspan=3)

info_string = StringVar()
info_string.set("")
info_label = Label(window,textvariable=info_string, relief="flat", width=60, height=2)
info_label.grid(row=1, columnspan=3)

make_board()

reset_button = Button(window, text="RESET BOARD", height=3, width=15, command = reset)
reset_button.grid(row=5, columnspan=3)

window.mainloop()


