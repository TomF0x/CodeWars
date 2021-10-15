# https://www.codewars.com/kata/529bf0e9bdf7657179000008

def valid_solution(board):
    regex=[1,2,3,4,5,6,7,8,9]
    for lst in board:
        if regex != sorted(lst):return False
    for i in range(9):
        if regex != sorted([board[nb][i] for nb in range(9)]):return False
    for y in range(0,9,3):
        for x in range(0,9,3):
            lst = []
            for ix in range(3):
                for iy in range(3):
                    lst.append(board[x+ix][y+iy])
            if sorted(lst) != regex:return False
    return True
