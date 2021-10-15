# https://www.codewars.com/kata/54da539698b8a2ad76000228

def is_valid_walk(walk):
    return True if len(walk)==10 and 1*walk.count('n')-1*walk.count('s')==0 and 1*walk.count('e')-1*walk.count('w')==0 else False
