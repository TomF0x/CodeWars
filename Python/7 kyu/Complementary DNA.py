# https://www.codewars.com/kata/554e4a2f232cdd87d9000038

def DNA_strand(dna):
    stri = ""
    for a in dna:
        if "A" in a:
            stri += "T"
        if "T" in a:
            stri += "A"
        if "G" in a:
            stri += "C"
        if "C" in a:
            stri += "G"
    return stri
