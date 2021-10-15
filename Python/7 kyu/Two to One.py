# https://www.codewars.com/kata/5656b6906de340bd1b0000ac

def longest(a1, a2):
    return "".join(chr(b) for b in list(set(sorted([ord(a) for a in a1+a2]))))
