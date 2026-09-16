ROWS = 6
COLS = 7
EMPTY = 0
RED = 1
YELLOW = 2
def create_board():
    board = [[0] * COLS for _ in range(ROWS)]
    return board


def print_board(board):
    print("  0 1 2 3 4 5 6")
    for r in range(5,-1,-1) :
        line = str(r) + " "
        for c in range(7):
            cell = board[r][c]
            symbol = "." if cell == EMPTY else ("R" if cell == RED else "Y")
            line = line + symbol + " "
        print(line)
    
def is_valid_move(board, col):
    return board[ ROWS - 1 ][col] == EMPTY

def get_next_open_row(board, col):
    for r in range(ROWS):
        if board[r][col] == EMPTY:
            return r
    return None

def drop_piece(board, col, player):
    if not is_valid_move(board, col):
        return -1

    r = get_next_open_row(board, col)
    board[r][col] = player
    return r 

board = create_board()
drop_piece(board, 0, YELLOW)
print(print_board(board))