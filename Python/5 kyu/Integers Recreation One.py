# https://www.codewars.com/kata/55aa075506463dac6600010d

def divisors(n):
    divisors_list = []
    i=1
    while (i <= n**0.5):
        if (n%i==0):
            divisors_list.append(i)
            divisors_list.append(n//i)
        i=i+1
    return(divisors_list)


def list_squared(m, n):
    resp=[]
    for nb in range(m,n):
        squared = sum(list(set([a**2 for a in divisors(nb)])))
        if squared**0.5%1==0:
            resp.append([nb,squared])
    return resp
