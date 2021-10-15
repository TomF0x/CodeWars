# https://www.codewars.com/kata/5839edaa6754d6fec10000a2

def find_missing_letter(chars):
    chars = [ord(a) for a in chars]
    for i in range(1,len(chars)):
        if chars[i]-chars[i-1]==2:
            return chr(chars[i-1]+1)
