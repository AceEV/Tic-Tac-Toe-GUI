def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], "\t", end='')
        print()

def check_for_winner(_board, player, i, j):
    global board
    board = _board
    if check_row(player, i) or check_column(player, j) or check_diagonal(player):
        return True
        
    return False


def check_row(player, i):
    for j in range(3):
        if board[i][j]['text'] != player:
            return False
    return True


def check_column(player, j):
    for i in range(3):
        if board[i][j]['text'] != player:
            return False
    return True


def check_diagonal(player):
    j=0
    for i in range(3):
        if board[i][j]['text'] == player:
            j += 1
        else:
            break
        if j == 3:
            return True

    j=2
    for i in range(3):
        if board[i][j]['text'] == player:
            j -= 1
        else:
            break
        if j == -1:
            return True

    return False
    