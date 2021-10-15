# https://www.codewars.com/kata/52597aa56021e91c93000cb0

def move_zeros(array):
    return [a for a in array if a!=0]+[0]*array.count(0)
