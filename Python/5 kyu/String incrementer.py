# https://www.codewars.com/kata/54a91a4883a7de5d7800009c

def increment_string(strng):
    index=-1
    if strng == "": return "1"
    if strng[-1] not in ["1","2","3","4","5","6","7","8","9","0"]: return strng+"1"
    for i in range(1,len(strng)+1):
        if strng[-i] in ["1","2","3","4","5","6","7","8","9","0"]:index=i
        else:return strng[:-index]+str(int(strng[-index:])+1).zfill(index)
    return strng[:-index]+str(int(strng[-index:])+1).zfill(index)
