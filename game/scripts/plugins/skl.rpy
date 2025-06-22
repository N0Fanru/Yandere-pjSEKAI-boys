define rus_text = 'йцукенгшщзхъфывапролджэячсмитьбю'

label skl(name0):

    if _preferences.language == None:

        $ last_n0 = name0[-1]

        if last_n0 == "а" or last_n0 == "ы" or last_n0 == "э":
            $ tp = "ой"
        elif last_n0 == "я" or last_n0 == "ю":
            $ tp = "ей"
        elif last_n0 == "о":
            $ tp = "ом"
        elif last_n0 == "е" or last_n0 == "й":
            $ tp = "ем"
        elif last_n0 == "ь":
            $ tp = "ью"
        elif last_n0 == "и" or last_n0 == "у":
            $ tp = last_n0
        elif last_n0 in rus_text:
            $ tp = last_n0 + "ом"
        else: 
            $ tp = last_n0

        $ name_tp = name0[:-1] + tp
        # творительный падеж, Instrumental case, used in the context of "relationship with" "came with"
        # The final value must be written to the variable 'name_tp'

    # elif skl_tl:

        # this

    return