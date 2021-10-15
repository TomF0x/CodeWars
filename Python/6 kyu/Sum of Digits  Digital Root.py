# https://www.codewars.com/kata/541c8630095125aba6000c00

def digital_root(n,b=0):
    while len(str(n))!=1:
        n=sum([int(a) for a in str(n)])
    return n
