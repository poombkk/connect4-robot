import random
import copy

from board import *

def valid_columns(board):
    c = []
    for r in range(COLS):
        if is_valid_move(board, r):
            c.append(r)
    return c

def random_move(board, player): 
    return random.choice(valid_columns(board))



def score_window(window, player):
    mine = 0
    theirs = 0
    empty = 0
    if player == RED:
        opp = YELLOW
    else:
        opp = RED
    for r in range(len(window)):
        if window[r] == player:
            mine += 1
        if window[r] == opp:
            theirs += 1    
        if window[r] == EMPTY:
            empty += 1
    if mine == 4:
        return 1000
    if mine == 3 and empty == 1:
        return 50
    if mine == 2 and empty == 2:
        return 25
    if theirs == 3 and empty == 1:
        return -50 # ลบ!
    
    return 0

def score_position(board, player):
    if player == RED:
        opp = YELLOW
    else:
        opp = RED
    score = 0
    for r in range(ROWS):
        if board[r][3] == player:
            score += 2
    for r in range(ROWS):
        for c in range(COLS):
            for d in range(4):
                window = [[],[],[],[]]
                for w in range(4):
                    # up
                    if d == 0 and r <= 2:
                        if board[r + w][c] == opp:
                            window = []
                            break
                        window.append(board[r + w][c])

                    # upright
                    if d == 1 and r <= 2 and c <= 3:
                        if r > 0 and board[r + w - 1][c + w] == EMPTY:
                            window = []
                            break
                        if board[r + w][c + w] == opp:
                            window = []
                            break
                        window.append(board[r + w][c + w])
                    # right
                    if d == 2 and c <= 3:
                        if r > 0 and board[r - 1][c + w] == EMPTY:
                            window = []
                            break
                        if board[r][c + w] == opp:
                            window = []
                            break
                        window.append(board[r][c + w])
                    # downright
                    if d == 3 and c <= 3 and r >= 3:
                        if board[r - w - 1][c + w] == EMPTY:
                            window = []
                            break
                        if board[r - w][c + w] == opp:
                            window = []
                            break
                        window.append(board[r - w][c + w])

                score += score_window(window ,player)
    return score

def greedy_move(board, player):
    best_col = None
    best_score = 0
    score = 0
    for col in valid_columns(board):
        tempb = copy.deepcopy(board)
        drop_piece(tempb, col, player)
        score = score_position(tempb, player)
        # print(col)
        # print_board(tempb)
        # print(score)
        if best_score < score:
            best_score = score
            best_col = col
    return best_col
        