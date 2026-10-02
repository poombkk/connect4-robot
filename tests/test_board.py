from board import * #test

def test_drop_stacks_from_bottom():
    b = create_board()
    drop_piece(b, 3, RED)
    drop_piece(b, 3, YELLOW)
    assert b[0][3] == RED 
    assert b[1][3] == YELLOW

def test_full_column_is_invalid():
    b = create_board()
    for r in range(6):
        drop_piece(b, 0, RED)
    assert is_valid_move(b, 0) == False

def test_horizontal_win():
    b = create_board()
    for i in range(4):
        drop_piece(b, i, RED)
    assert winning_move(b, RED) == True
    assert winning_move(b, YELLOW) == False

def test_vertical_win():
    c = 0
    b = create_board()
    for i in range(7):
        for a in range(c):
            drop_piece(b, i, YELLOW)
        for r in range(4):
            drop_piece(b, i, RED)
        assert winning_move(b, RED) == True
        assert winning_move(b, YELLOW) == False

def test_vertical_win():
    b = create_board()
    for i in range(7):
        for r in range(4):
            drop_piece(b, i, RED)
        assert winning_move(b, RED) == True
        assert winning_move(b, YELLOW) == False

def test_diag_up_win():
    b = create_board()
    for i in range(1, 4, 1):
        for r in range(0, i, 1):
            drop_piece(b, i, YELLOW)
        drop_piece(b, i, RED)
    drop_piece(b, 0, RED)   
    assert winning_move(b, RED) == True
    assert winning_move(b, YELLOW) == False

def test_diag_down_win():
    b = create_board()
    for i in range(0, 3, 1):
        for r in range(3, i, -1):
            drop_piece(b, i, YELLOW)
        drop_piece(b, i, RED)
    drop_piece(b, 3, RED)
    print_board(b)
    assert winning_move(b, RED) == True
    assert winning_move(b, YELLOW) == False

def test_empty_board_no_winner():
    b = create_board()
    assert winning_move(b, RED) == False
    assert winning_move(b, YELLOW) == False
    