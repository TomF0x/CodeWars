# https://www.codewars.com/kata/585d7d5adb20cf33cb000235

def find_uniq(arr):
    for a in arr:
        if arr.count(a) == 1:
            return a
        else:
            b = list(set(arr))
            b.remove(a)
            return b[0]
