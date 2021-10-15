# https://www.codewars.com/kata/54da5a58ea159efa38000836

def find_it(seq):
    return [a for a in seq if seq.count(a)%2!=0][0]
