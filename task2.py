def alphanumeric (a_string):
    alphanum = ""
    for character in a_string:
        if character.isalnum():
            alphanum += character
    return alphanum

print(alphanumeric ('Ziha&$%$^$#&qqq879678q'))

