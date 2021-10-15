# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c

def max_sequence(arr):
    rep = sum(arr)
    for i in range(len(arr)):
        for y in range(i,len(arr)+1):
            if sum(arr[i:y])>=rep:
                rep = sum(arr[i:y])
    return rep if rep>0 else 0
