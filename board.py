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

def winning_move(board, player):
# ---- แนวนอน
    for r in range(ROWS):
        for c in range(COLS - 2): 
            if(
                 board[r][c] == player and board[r][c+1] == player
                and board[r][c+2] == player and board[r][c+3] == player
            ):
                return True
# ---- แนวตั้ง
    for r in range(ROWS - 3):
        for c in range(COLS):
            if(
                 board[r][c] == player and board[r+1][c] == player 
                and board[r+2][c] == player and board[r+3][c] == player
            ):
                return True
# ---- ทแยงขึ้น
    for r in range(ROWS - 3):
        for c in range(COLS):
            if(
                 board[r][c] == player and board[r+1][c+1] == player 
                and board[r+2][c+2] == player and board[r+3][c+3] == player
            ):
                return True
# ---- ทแยงลง
    for r in range(ROWS -1, 2, -1):
        for c in range(COLS):
            if(
                 board[r][c] == player and board[r-1][c+1] == player 
                and board[r-2][c+2] == player and board[r-3][c+3] == player
            ):
                return True
    return False

board = create_board()
drop_piece(board, 3, YELLOW)
drop_piece(board, 2, RED)
drop_piece(board, 2, YELLOW)
drop_piece(board, 1, RED)
drop_piece(board, 1, RED)
drop_piece(board, 1, YELLOW)
drop_piece(board, 0, RED)
drop_piece(board, 0, RED)
drop_piece(board, 0, RED)
drop_piece(board, 0, YELLOW)
print_board(board)
print(winning_move(board, YELLOW))
