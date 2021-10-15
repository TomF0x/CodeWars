# https://www.codewars.com/kata/52774a314c2333f0a7000688

def valid_parentheses(string):
    #Failed
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False
