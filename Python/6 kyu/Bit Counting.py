# https://www.codewars.com/kata/526571aae218b8ee490006f4

def count_bits(n):
    return bin(n)[2:].count('1')
