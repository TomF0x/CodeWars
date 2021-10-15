# https://www.codewars.com/kata/56b8903933dbe5831e000c76

def spoonerize(words):
    return "{}{} {}{}".format(words.split(" ")[1][0],words.split(" ")[0][1:],words.split(" ")[0][0],words.split(" ")[1][1:])
