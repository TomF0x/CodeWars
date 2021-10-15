# https://www.codewars.com/kata/52fba66badcd10859f00097e

def disemvowel(string):
    return str("".join([a for a in string if a.lower() not in ['a','e','i','o','u']]))
