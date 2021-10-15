# https://www.codewars.com/kata/54e6533c92449cc251001667

def unique_in_order(iterable):
    listemp=['']
    for a in range(len(iterable)):
        if iterable[a-1]==iterable[a] and listemp[-1]!=iterable[a]:
            listemp.append(iterable[a-1])
        elif iterable[a-1]!=iterable[a]:
            listemp.append(iterable[a])
    return listemp[1:]
