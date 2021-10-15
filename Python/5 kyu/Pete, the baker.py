# https://www.codewars.com/kata/525c65e51bf619685c000059

def cakes(recipe, available):
    for a in recipe:
        if a not in [a for a in available]: return 0
    else: return min([available[a]//recipe[a] for a in recipe])
