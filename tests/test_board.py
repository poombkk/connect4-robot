from board import * #test

def test_drop_stacks_from_bottom(): # ตัวอย่างเต็ม 1 ข้อ
    b = create_board()
    drop_piece(b, 3, RED)
    drop_piece(b, 3, YELLOW)
    assert b[0][3] == RED # assert = "ยืนยันว่าจริง" ถ้าไม่จริง test แดง
    assert b[1][3] == YELLOW

#print(test_drop_stacks_from_bottom())