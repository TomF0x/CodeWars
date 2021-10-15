# https://www.codewars.com/kata/5552101f47fc5178b1000050

def dig_pow(n, p,r=0):
    for a in str(n):
        r += int(a)**p
        p+=1
    return int(r/n) if (r/n)>=1 and (r/n)%1==0 else -1
