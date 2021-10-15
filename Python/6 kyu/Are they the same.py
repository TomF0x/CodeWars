# https://www.codewars.com/kata/550498447451fbbd7600041c

def comp(array1, array2):
    if array1==[] and array2!=[] or array1!=[] and array2==[]:return False
    for a in array1:
        if a*a in array2:
            array2.pop(array2.index(a*a))
        else:return False
    return True
