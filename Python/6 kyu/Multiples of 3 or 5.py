# https://www.codewars.com/kata/514b92a657cdc65150000006

def solution(number):
    return sum([a for a in range(number) if a%5==0 or a%3==0])
