# https://www.codewars.com/kata/517abf86da9663f1d2000003

def to_camel_case(text):
    if text=='':return text
    for a in range(len(text)-text.count('-')-text.count('_')):
        if text[a] in ['_','-']:
            text=text[:a]+text[a+1].upper()+text[a+2:]
    return text
