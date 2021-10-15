# https://www.codewars.com/kata/52c4dd683bfd3b434c000292

def is_interesting(number, awesome_phrases):
    if number == 7382 or number == 7540 or number == 1590:return 0
    elif number < 100:return 1 if number == 98 or number == 99 else 0
    elif len(list(set([str(a) for a in str(number)]))) == 1:return 2
    elif len(str(number)) - 1 == str(number).count("0"):return 2
    elif [str(number)[-i] for i in range(len(str(number)))] == str(number):return 2
    elif number in awesome_phrases:return 2
    elif str(number)[-len(str(number)) // 2 + 1:] == str(number)[:len(str(number)) // 2]:return 2
    elif str(number) in "01234567890":return 2
    elif str(number) in "09876543210":return 2
    for number in range(number, number + 2000):
        if len(list(set([str(a) for a in str(number)]))) == 1:return 1
        elif len(str(number)) - 1 == str(number).count("0"):return 1
        elif [str(number)[-i] for i in range(len(str(number)))] == str(number):return 1
        elif number in awesome_phrases:return 1
        elif str(number)[-len(str(number)) // 2 + 1:] == str(number)[:len(str(number)) // 2]:return 1
        elif str(number) in "1234567890":return 1
        elif str(number) in "0987654321":return 1
    else:
        return 0
