# https://www.codewars.com/kata/5526fc09a1bbd946250002dc

def find_outlier(integers):
    lst=[a%2==0 for a in integers]
    if lst.count(False)>lst.count(True):
        for i in range(len(integers)):
            if integers[i]%2==0:
                return integers[i]
    if lst.count(False)<lst.count(True):
        for i in range(len(integers)):
            if integers[i]%2==1:
                return integers[i]
