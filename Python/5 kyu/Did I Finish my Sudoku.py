# https://www.codewars.com/kata/53db96041f1a7d32dc0004d2

def done_or_not(board): #board[i][j]
    regex=[1,2,3,4,5,6,7,8,9]
    for lst in board:
        if regex != sorted(lst):
            return 'Try again!'
    for i in range(9):
        if regex != sorted([board[nb][i] for nb in range(9)]):
            return 'Try again!'
    y=0
    for _ in range(3):
        x=0
        for _ in range(3):
            lst = []
            for ix in range(3):
                for iy in range(3):
                    lst.append(board[x+ix][y+iy])
            if sorted(lst) != regex:return 'Try again!'
            x+=3
        y+=3
    return "Finished!"
