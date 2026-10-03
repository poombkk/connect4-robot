from board import *
from ai import *

def ask_column(board, player):
    while True:
        text = input("please input (0-6): ")
        if text.isdigit() == False:
            print("not a number please try input (0-6):") ; continue
        col = int(text)
        if col < 0 or col > 6:
            print("wrong number please try input (0-6): ") ; continue
        return col


brains = {RED: random_move, YELLOW: random_move}

def main():
    board = create_board()
    player = RED
    while True:
        print_board(board)
        #col = ask_column(board, player)
        col = brains[player](board, player)
        drop_piece(board, col, player)
        if winning_move(board, player):
            print_board(board) ; print("RED WIN!") ; break
        if is_board_full(board):
            print_board(board) ; print("TIE!") ; break
        if player == RED:
            player = YELLOW
        else:
            player = RED

if __name__ == "__main__":
    main()