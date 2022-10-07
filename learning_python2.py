'''Creating a translator function
This program is cool'''



def translator (phrase):
    translation = ""
    for character in phrase:
        if character.lower() in "a":
            translation = translation + "9"
        elif character.lower() in "e":
            translation = translation + "3"
        elif character.lower() in "i":
            translation = translation + "1"
        elif character.lower() in "o":
            translation = translation + "@"
        elif character.lower() in "u":
            translation = translation + "v"
        else:
            translation = translation + character

    return translation

print(translator(input("Type in a word or sentence: ")))
