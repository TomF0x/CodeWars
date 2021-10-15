# https://www.codewars.com/kata/545cedaa9943f7fe7b000048

import string

def is_pangram(s):
    s="".join([a for a in s.lower()if ord(a)>64])
    return all([str in string.ascii_lowercase for str in s]) and len([str in string.ascii_lowercase for str in s])>=26
