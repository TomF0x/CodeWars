def rot13(message):
    mess = ""
    for letter in message:
        if letter != " ":
            if letter.isalpha():
                if ord("a") <= ord(letter.lower()) - 13:
                    mess += chr(ord(letter) - 13)
                else:
                    mess += chr(ord(letter) - 13 + 26)
            else:
                mess += letter
        else:
            mess += " "
    return mess


print(rot13("test"))
