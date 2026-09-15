ROWS = 6
COLS = 7
EMPTY = 0
RED = 1
YELLOW = 2
def create_board():
    board = [[0] * COLS for _ in range(ROWS)]
    return board


def print_board(board):
    for r in range(5,-1,-1) :
        line = str(r) + " "
        for c in range(7):
            cell = board[r][c]
            symbol = "." if cell == EMPTY else ("R" if cell == RED else "Y")
            line = line + symbol + " "
        print(line)

board = create_board()
print("  0 1 2 3 4 5 6")
print(print_board(board))