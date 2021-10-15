# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

def persistence(n,nb=0):
    if len(str(n))==1: return 0
    while len(str(eval('*'.join([a for a in str(n)]))))!=1:
        n=eval('*'.join([a for a in str(n)]))
        nb+=1
    return nb+1
