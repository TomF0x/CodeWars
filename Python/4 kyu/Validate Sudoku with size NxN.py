# https://www.codewars.com/kata/540afbe2dc9f615d5e000425

class Sudoku(object):
    def __init__(self, data):
        self.data=data
    def is_valid(self):
        if len(list(set([len(row) for row in self.data])))==1:
            for a in self.data:
                if bool in [type(a) for a in a]:return False
            regex=[a for a in range(1,len(self.data)+1)]
            for lst in self.data:
                if regex != sorted(lst):
                    return False
            for i in range(len(self.data)):
                if regex != sorted([self.data[nb][i] for nb in range(len(self.data))]):
                    return False
            y=0
            for _ in range(int(len(self.data)**0.5)):
                x=0
                for _ in range(int(len(self.data)**0.5)):
                    lst = []
                    for ix in range(int(len(self.data)**0.5)):
                        for iy in range(int(len(self.data)**0.5)):
                            lst.append(self.data[x+ix][y+iy])
                    if sorted(lst) != regex:
                        return False
                    x+=int(len(self.data)**0.5)
                y+=int(len(self.data)**0.5)
            return True
        else:return False
