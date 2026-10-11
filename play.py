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
        if is_valid_move(board, col) == False:
            print("column is full please try others column (0-6): ") ; continue
        return col 

brains = {RED: ask_column, YELLOW: greedy_move}

def main():
    board = create_board()
    player = RED
    print_board(board)
    while True:
        #col = ask_column(board, player)
        col = brains[player](board, player)
        drop_piece(board, col, player)
        if player == 1:
            Winner = "RED"
        else:
            Winner = "YELLOW"
        if winning_move(board, player):
            print_board(board) ; print((Winner),"WIN!") ; break
        if is_board_full(board):
            print_board(board) ; print("TIE!") ; break
        print_board(board)
        print(Winner)
        print(score_position(board, player))        
        if player == RED:
            player = YELLOW
        else:
            player = RED        
 

if __name__ == "__main__":
    main()