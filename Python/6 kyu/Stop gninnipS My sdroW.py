# https://www.codewars.com/kata/5264d2b162488dc400000001

def spin_words(sentence):
    return ' '.join([a if len(a)<5 else a[::-1] for a in sentence.split(' ')])
