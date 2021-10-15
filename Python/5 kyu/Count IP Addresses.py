# https://www.codewars.com/kata/526989a41034285187000de4

def ips_between(start, end):
    print(start,end)
    return int(end.split(".")[-1])-int(start.split(".")[-1])+(int(end.split(".")[-2])-int(start.split(".")[-2]))*256+(int(end.split(".")[-3])-int(start.split(".")[-3]))*65536+(int(end.split(".")[-4])-int(start.split(".")[-4]))*16777216
