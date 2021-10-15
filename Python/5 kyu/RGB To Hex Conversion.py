# https://www.codewars.com/kata/513e08acc600c94f01000001

def rgb(r, g, b):
    #Failed
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
