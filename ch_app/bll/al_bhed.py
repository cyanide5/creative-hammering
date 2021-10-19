from ch_app.dll import albhed_cypher


def translate_eng(phrase):
    output = ""
    for letter in phrase:
        trans_letter = albhed_cypher.eng_alb.get(letter.upper())
        try:
            output = output + trans_letter
        except TypeError:
            output = output + letter
    return output
