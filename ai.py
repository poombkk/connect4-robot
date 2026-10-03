import random

from board import *

def valid_columns(board):
    c = []
    for r in range(COLS):
        if is_valid_move(board, r):
            c.append(r)
    return c

def random_move(board, player): 
    return random.choice(valid_columns(board))
