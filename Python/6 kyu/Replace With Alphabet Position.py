# https://www.codewars.com/kata/546f922b54af40e1e90001da

def alphabet_position(text):
    return " ".join([str(ord(a.upper())-64) for a in str(text) if ord(a.upper())-64>0])
