# https://www.codewars.com/kata/57b06f90e298a7b53d000a86

def queue_time(customers, n):
    list=[0 for a in range(n)]
    while len(customers)!=0:
        list[list.index(min(list))]+=customers.pop(0)
    return max(list)
