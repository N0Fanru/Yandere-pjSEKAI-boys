define wn_ru = False
define wn_tsu = False
define wn_nof = False
define wn = int(0)

define all_secret_name_rui = [rui_names, tsukasa_names, nofanru_name]

label what_name_rui:

    if persistent.name in rui_names:
        if not wn_ru:
            $ wn += 1
        $ wn_ru = True
    elif persistent.name in tsukasa_names:
        if not wn_tsu:
            $ wn += 1
        $ wn_tsu = True
    elif persistent.name in nofanru_name:
        if not wn_nof:
            $ wn += 1
        $ wn_nof = True

    return

label secret_name_rui:

    call what_name_rui from _call_what_name_rui

    $ s4_add('1')

    "[persistent.name]?... Вы серьёзно?"

    "Нет, так дело не пойдёт, давай по новой."

    show screen inputstart

    extend ""

    $ persistent.name = persistent.name.title() 

    call what_name_rui from _call_what_name_rui_1

    if persistent.name in rui_names:

        "Вы настолько гениальны, что хотите назвать себя именем вашего виртуального яндере партнёра?..."

        "Как вы себе это представляете?.. {w=1}Это бы сломало мой мозг, при том факте, что лишь набор цифорок в коде."

    elif persistent.name in tsukasa_names:

        "Цукаса? Очень умно..."

        "Спешу вас огорчить, но в этой игре РуиКасы не канон."

    elif persistent.name in nofanru_name:

        "Ты же не Нофанру, так?.."

        "Тогда зачем ты ставишь её имя..."

    else:

        return

    "Как удалиться из этой игры..."

    show screen inputstart

    extend ""

    $ persistent.name = persistent.name.title() 

    call what_name_rui from _call_what_name_rui_2

    if wn_nof and wn_ru and wn_tsu:

        jump .win

    if contains_element(all_secret_name_rui, persistent.name):

        "Ладно, в третий раз можно догадаться, что вы не просто так вводите такие ники..."

    else:

        return

    "Что вы хотите взамен? Ачивку? Секретную концовку? Пойти нахуй?"

    "Хорошо, давай так: я делаю вид, что вы случайно три раза подрят ввели странный ник, а вы сейчас вводите нормальный, хорошо?"

    show screen inputstart

    extend ""

    $ persistent.name = persistent.name.title() 

    call what_name_rui from _call_what_name_rui_3

    if wn_nof and wn_ru and wn_tsu:

        jump .win

    if contains_element(all_secret_name_rui, persistent.name):

        "..."

        "Я разочарован в вас..."

    else:

        return

    "Итак, хорошо, вы получите свою секретную концвоку, но при одном условии..."

    "Вы должны угадать все три имени, на которые срабатывает эту часть скрипта. Окей?"

    if wn == 1:

        "Вы нашли всего одно такое имя. Что ж.. удачи с остальными двумя."

    elif wn == 2:

        "Вы уже нашли два таких имени, осталось всего одно... Что же это?"

    $ n = 0

    $ oldd = wn

    $ nt = 0

    $ sp = []

    while n == 0:

        show screen inputstart

        extend ""

        $ persistent.name = persistent.name.title() 

        call what_name_rui from _call_what_name_rui_4

        if wn_nof and wn_ru and wn_tsu:

            $ n = 1

            jump .win

        elif contains_element(all_secret_name_rui, persistent.name):

            if oldd == wn:

                if nt == 5:

                    "Ладно. С меня достаточно. В пятый раз это уже не так интересно."

                    "Мне нужно выполнять свою роль рассказчика, а не страдать этой фигнёй сейчас..."

                    "Я сам выдам вам имя и на этом мы разойдёмся."

                    $ persistent.name = "Спасибо, Олег"

                    $ get_ach('oleg')

                    $ n = 1

                    return

                else:

                    "Вы ведь уже вводили это имя... Вы надеетесь, что оно дважды засчитается или что?"

                    $ nt += 1    

            else:

                "Ага, отлично! Вы нашли ещё одно имя. Давайте, осталось ещё одно.."

        else:

            if nt == 5:

                "Ладно. С меня достаточно. В пятый раз это уже не так интересно."

                "Мне нужно выполнять свою роль рассказчика, а не страдать этой фигнёй сейчас..."

                "Я сам выдам вам имя и на этом мы разойдёмся."

                $ persistent.name = "Спасибо, Олег"

                $ get_ach('oleg')

                $ n = 1

                return

            elif persistent.name in sp:

                "Вы ведь уже вводили это имя... Вы надеетесь, что во второй раз оно станет верным?"

            else:

                "Нет, вы не угадали! Попробуйте ещё разок, ехехехех."

                $ x = persistent.name

                $ sp.insert(0, x)

                $ nt += 1

    label .win:

        "Ха-ха! Вы угадали все три имени! {p=1}И зачем я потратил на это столько времени..."

        "В любом случае, держите вашу секрутную концовку и не подавитесь!"

        'Назову её "Спасибо, что доводите рассказчика!"'

        $ n = 9

        window hide

        call ends_secret("name") from _call_ends_secret

        pause 5.0

    return


label startRui:

    stop music fadeout 0.5

    scene bg room
    with Fade(0.5, 1.0, 0.5)

    if persistent.name == "":

        show screen inputstart

        pause 0.1

        pause 0.2

    pause 0.1

    window show

    label .name:

        $ n = 0

        $ persistent.name = persistent.name.title() 

        if contains_element(all_secret_name_rui, persistent.name):

            call secret_name_rui from _call_secret_name_rui

        if n == 9:

            return

        if persistent.name == "" or persistent.name == "Т/И" or persistent.name == "Y/N":

            if _preferences.language == None:

                $ persistent.name = "т/и"
                $ pn_tp = "т/и"

            else:

                $ persistent.name = "y/n"
                $ pn_tp = "y/n"

        elif len(persistent.name) < 2:

            "Введенно слишком короткое имя! Должно быть минимум две буквы!"

            show screen inputstart

            pause 0.1

            pause 0.2

            jump .name


        elif persistent.name == "Спасибо, Олег":

            $ persistent.name = "Спасибо, Олег"
            if _preferences.language == None:
                $ pn_tp = "Олегом"
            else:
                $ pn_tp = "Oleg"

        elif persistent.name in kaito_names:

            show bg roomglitch

            $ persistent.showkaito_rui = False

            voice k_sad_um
            ks2 "{glitch=10}{sc}{=norm_style}ТЫ ЗНАЕШЬ?{/sc}{/glitch}{w=0.1}{nw}"

            show bg room

            call kaito_list_lable("name") from _call_kaito_list_lable

            $ persistent.name = "Йяисн"
            $ pn_tp = "Я �и�у"

        elif persistent.name == "Йяисн" or persistent.name == "Jzhsn":

            if _preferences.language == None:
                $ persistent.name = "Йяисн"
                $ pn_tp = "Я �и�у"
            else:
                $ persistent.name = "Jzhsn"
                $ pn_tp = "Jzhsn"

        else:

            if _preferences.language == None or skl_tl == True:
                call skl(persistent.name) from _call_skl
                $ pn_tp = name_tp
            else:
                $ pn_tp = persistent.name

        if persistent.name in waifu_names:
            $ get_ach('flower')

    $ player_name = persistent.name
    $ PN = player_name.upper()
    $ timerm = False

    $ persistent.petlya -= 1

    play music ruistart fadein 2.0 volume 0.5

    play sound knock3

    "Какой-то долбаёб стучится к вам в 6 утра."
    extend "\nДолжно быть это ваш парень Руи..."

    # $ persistent.showkaito_rui = False

    play sound knock2
    queue sound knock2
    queue sound knock2

    "Чё за хуйня.."

    "Наверное вам стоит переодеться и открыть ему дверь."

    menu:

        "Жёстко игнорить":
            jump ignor

        "Раздеться до трусов":
            jump trusiki

        "Остаться в пижаме":
            jump pizhama

        "Переодеться":

            jump pereodetsa

    return


# гг переезжает к Руи
label go_rui_home:

    stop music fadeout 1.5

    scene black with Dissolve(.3)

    pause 0.5

    "Удивительно..."

    "После переезда к Руи, он начал вести себя слишком... нормально?.."

    "Да, именно нормально!"

    "Поздравляю, вы пришли с ним к здоровым отношениям~"

    window hide

    pause 5.0

    call ends_rui("home") from _call_ends_rui_22

    pause 5.0

    return

    return