# https://www.codewars.com/kata/523a86aa4230ebb5420001e1

def anagrams(word, words,alp = 'abcdefghijklmnoqprstuvwxyz'):
    return [a for a in words if [word.count(t) for t in alp]==[a.count(t) for t in alp]]
