# https://www.codewars.com/kata/5270d0d18625160ada0000e4

def score(dice,score=0):
    for a in list(set(dice)):
        if a!=1 and a!=5:
            score+=a*100*(dice.count(a)//3)
        elif a==1:
            score+=1000*(dice.count(a)//3)
            score+=100*(dice.count(a)%3)
        else:
            score+=500*(dice.count(a)//3)
            score+=50*(dice.count(a)%3)
    return score
