from ch_app.dll import albhed_cypher


#
# eng_phrase = input("type something: ")

def translate_eng(phrase):
    output = ""
    for letter in phrase:
        trans_letter = albhed_cypher.eng_alb.get(letter.upper())
        try:
            output = output + trans_letter
        except TypeError:
            output = output + letter
    return output

#
# def translate_to_ab(engPhrase):
#     translation = ""
#     for letter in engPhrase:
#         if letter in "Aa":
#             if letter.isupper():
#                 translation = translation + "Y"
#             else:
#                 translation = translation + "y"
#
#         elif letter in "Bb":
#             if letter.isupper():
#                 translation = translation + "P"
#             else:
#                 translation = translation + "p"
#
#         elif letter in "Cd":
#             if letter.isupper():
#                 translation = translation + "L"
#             else:
#                 translation = translation + "l"
#
#         elif letter in "Dd":
#             if letter.isupper():
#                 translation = translation + "T"
#             else:
#                 translation + translation + "t"
#
#         elif letter in "Ee":
#             if letter.isupper():
#                 translation = translation + "A"
#             else:
#                 translation = translation + "a"
#
#         elif letter in "Ff":
#             if letter.isupper():
#                 translation = translation + "V"
#             else:
#                 translation = translation + "v"
#
#         elif letter in "Gg":
#             if letter.isupper():
#                 translation = translation + "K"
#             else:
#                 translation = translation + "k"
#
#         elif letter in "Hh":
#             if letter.isupper():
#                 translation = translation + "R"
#             else:
#                 translation = translation + "r"
#
#         elif letter in "Ii":
#             if letter.isupper():
#                 translation = translation + "E"
#             else:
#                 translation = translation + "e"
#
#         elif letter in "Jj":
#             if letter.isupper():
#                 translation = translation + "Z"
#             else:
#                 translation = translation + "z"
#
#         elif letter in "Kk":
#             if letter.isupper():
#                 translation = translation + "G"
#             else:
#                 translation = translation + "g"
#
#         elif letter in "Ll":
#             if letter.isupper():
#                 translation = translation + "M"
#             else:
#                 translation = translation + "m"
#
#         elif letter in "Mm":
#             if letter.isupper():
#                 translation = translation + "S"
#             else:
#                 translation = translation + "s"
#
#         elif letter in "Nn":
#             if letter.isupper():
#                 translation = translation + "H"
#             else:
#                 translation = translation + "h"
#
#         elif letter in "Oo":
#             if letter.isupper():
#                 translation = translation + "U"
#             else:
#                 translation = translation + "u"
#
#         elif letter in "Pp":
#             if letter.isupper():
#                 translation = translation + "B"
#             else:
#                 translation = translation + "b"
#
#         elif letter in "Qq":
#             if letter.isupper():
#                 translation = translation + "X"
#             else:
#                 translation = translation + "x"
#
#         elif letter in "Rr":
#             if letter.isupper():
#                 translation = translation + "N"
#             else:
#                 translation = translation + "n"
#
#         elif letter in "Ss":
#             if letter.isupper():
#                 translation = translation + "C"
#             else:
#                 translation = translation + "c"
#
#         elif letter in "Tt":
#             if letter.isupper():
#                 translation = translation + "D"
#             else:
#                 translation = translation + "d"
#
#         elif letter in "Uu":
#             if letter.isupper():
#                 translation = translation + "I"
#             else:
#                 translation = translation + "i"
#
#         elif letter in "Vv":
#             if letter.isupper():
#                 translation = translation + "J"
#             else:
#                 translation = translation + "j"
#
#         elif letter in "Ww":
#             if letter.isupper():
#                 translation = translation + "F"
#             else:
#                 translation = translation + "f"
#
#         elif letter in "Xx":
#             if letter.isupper():
#                 translation = translation + "Q"
#             else:
#                 translation = translation + "q"
#
#         elif letter in "Yy":
#             if letter.isupper():
#                 translation = translation + "O"
#             else:
#                 translation = translation + "o"
#
#         elif letter in "Zz":
#             if letter.isupper():
#                 translation = translation + "W"
#             else:
#                 translation = translation + "w"
#
#         else:
#             translation = translation + letter
#
#     return "Al Bhed Translation: " + translation
#
#
# print(translate_to_ab(input("Enter an English word or phrase: ")))
