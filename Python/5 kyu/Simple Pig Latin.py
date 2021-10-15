# https://www.codewars.com/kata/520b9d2ad5c005041100000f

def pig_it(text):
    return " ".join([a[1:]+a[0]+'ay' if a!='!' and a!='?' else a for a in text.split(" ")])
