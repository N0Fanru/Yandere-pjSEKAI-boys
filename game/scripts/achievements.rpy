# ачивки четырёх типов:
# 1. обычные
# 2. прогрессируешие (нужно выполнить несколько действий)
# 3. скрытые 
# 4. скрытые прогрессируешие

# [тип отношения(common, rui), тип(целое число), название(строка), описание(строка), получуена или нет(логическая), прогресс(целое число, только прогрессирующий, сколько выполнино), возможный прогресс(сколько можно выполнить всего)]
# ['rui', 1, 'Ачивка1', 'Не сдохнуть с Руи', False] или ['common' 2, 'Ачивка2', 'Сдохнуть три раза', False, 0, 3]

define len_kaito_secret = len(kaito_list_full)
define len_rui = 22
define len_secret_ends = 4

define len_ends = len_rui + len_secret_ends

# common 'Истинный фанат', 'Откройте все концовки и все ачивки в игре...' #1
default persistent.main_ach = False

define ach_ru = [
['common', 2, 'Фанат', 'Откройте все концовки в игре', False, 0, len_ends], #2
['common', 2, 'Сыщик', 'Откройте все секретные концовки', False, 0, len_secret_ends], #3
['common', 2, 'Четвёртая стена это who?', 'Заставьте рассказчика сломать четвёртую стену всеми возможными способами', False, 0, 7], #4
['common', 1, 'Я знаю вкус автора!', 'Введите имя любимого женского вокалоида автора новеллы', False], #5
['common', 3, 'Девушка с подвохом', 'Получите имя "Спасибо, Олег"', False], #6
['common', 3, 'Цветок?', 'Услышьте голос VFlower в заставке', False], #7
['common', 4, 'Prope sum', 'Volo te attendere ad me', False, 0, len_kaito_secret], #8
['rui', 2, 'Руи симп', 'Откройте все концовки с яндере Руи', False, 0, len_rui], #9
['rui', 1, 'Довели...', 'Получите отказ от Руи...', False], #10
['rui', 1, 'Напряжённое молчание...', 'Вам тревожно видеть это многоточие...', False], #11
['rui', 1, 'Поддержка', 'Максимально защищайте Руи в диалоге с Цукасой и после этого', False], #12
['rui', 2, 'Решала!', 'Победите в двух спорах с Руи на время', False, 0, 2], #14
['rui', 2, 'Вы точно человек?', 'Угадайте числа в генераторе рандомных чисел с первой попытки на всех сложностях', False, 0, 3], #15
['rui', 2, 'Бедный Цукаса...', 'Позвольте Руи дважды избить Цукасу', False, 0, 2], #16
['rui', 2, 'Руи делает меня хорни!', 'Просмотрите все возможные вариации постельных сцен', False, 0, 21], #17
['rui', 2, 'Руи, за что?', 'Заставьте Руи причинить вам вред всеми возможными способами...', False, 0, 46], #18
['rui', 2, 'Адвокат', 'Победите в суде двумя способами', False, 0, 2], #19
['rui', 2, 'Играть так играть!', 'Опробуйте все варианты в "Правда или действие"', False, 0, 5], #20
['rui', 2, 'Неудачный романтик', 'Провалите попытки уломать Цукасу на секс всеми возможными способами', False, 0, 3], #21
['rui', 2, 'Идеальный лжец', 'Заставьте Руи поверить в вашу ложь везде, где это возможно', False, 0, 7], #22
['rui', 3, 'Сопротивление невозможно', 'У вас есть выбор только "Смириться"...', False], #23
['rui', 3, 'По краю лезвия ходишь', 'Разозлите Руи, но извинитесь', False], #13
['rui', 4, 'Где мои деньги???', 'Попросите Руи здонатить вам в секае пять раз... Вы ведь понимаете, что это не сработает?', False, 0, 5], #24
['rui', 4, 'Один исход...', 'Получите концовку "Идеальный мир" всеми способами', False, 0, 3], #25
['rui', 4, 'Юморист', 'Ваш юмор ужасен...', False, 0, 3] #26
]

define ach_code_def = [
'fan', #2
'secret_ends', #3
'4s', #4
'flower', #5
'oleg', #6
'voca', #7
'kaito_secret', #8
'rui_fan', #9
'rui_say_no', #10
'...', #11
'za_rui', #12
'reshala', #14
'mega_rangen', #15
'tsu_pain', #16
'horny_rui', #17
'rui_why', #18
'advokat', #19
'play_as', #20
'tsu_no', #21
'lie', #22
'smir', #23
'dog_wow', #13
'sekai', #24
'pr_world_all', #25
'haha' #26
]

default persistent.ach = ach_ru
default persistent.ach_code = ach_code_def

default persistent.done_ach = []

# default persistent.ach = []

default persistent.common_ach_pct = 0.0
default persistent.rui_ach_pct = 0.0
default persistent.all_ach_pct = 0.0

init python:

    # persistent.ach = ach_ru
    # persistent.ach_code = ach_code_def

    # if persistent.ach = []:
    #     if _preferences.language == None:
    #         persistent.ach = ach_ru
    #     else:
    #         persistent.ach = ach_tl

    persistent.ach_100 = 0
    persistent.ach_rui_100 = 0
    persistent.ach_com_100 = 0
    for i in persistent.ach:
        if len(i) == 5:
            persistent.ach_100 += 1
            if i[0] == 'common':
                persistent.ach_com_100 += 1
            elif i[0] == 'rui':
                persistent.ach_rui_100 += 1
        else:
            n = i[6]
            persistent.ach_100 += n
            if i[0] == 'common':
                persistent.ach_com_100 += n
            elif i[0] == 'rui':
                persistent.ach_rui_100 += n


    def ach_pct():
        numcom = 0
        numrui = 0
        numall = 0
        for i in persistent.ach:
            if i[1] == 1 or i[1] == 3:
                if i[4] == True:
                    numall += 1
                    if i[0] == 'common':
                        numcom += 1
                    elif i[0] == 'rui':
                        numrui += 1
            else:
                n = i[5]
                numall += n
                if i[0] == 'common':
                    numcom += n 
                elif i[0] == 'rui':
                    numrui += n 
        persistent.common_ach_pct = round(((numcom*100) / persistent.ach_com_100), 2)
        persistent.rui_ach_pct = round(((numrui*100) / persistent.ach_rui_100), 2)
        persistent.all_ach_pct = round(((numall*100) / persistent.ach_100), 2)


    def game_end():
        if persistent.all_ach_pct == 100 and not persistent.main_ach:
            persistent.main_ach = True
            renpy.show_screen('get_all_ach_show')


    def get_ach(ach, tm=0.1):
        if ach not in persistent.done_ach:
            n_list = persistent.ach_code
            i = n_list.index(ach)
            n_list.pop(i)
            n_list.insert(0, ach)
            ach_full = persistent.ach[i]
            n_list = persistent.ach
            n_list.pop(i)
            n_list.insert(0, ach_full)
            persistent.ach = n_list
            if persistent.ach[0][1] == 1 or persistent.ach[0][1] == 3:
                persistent.crystal += 50
                if persistent.ach[0][1] == 3:
                    persistent.crystal += 50
                renpy.show_screen('get_ach_show', tm)
                persistent.ach[0][4] = True
                n_list = persistent.done_ach
                n_list.insert(0, ach)
                persistent.done_ach = n_list
            else:
                persistent.ach[0][5] += 1
                persistent.crystal += 10
                if persistent.ach[0][1] == 4:
                    persistent.crystal += 10
                if persistent.ach[0][5] == persistent.ach[0][6]:
                    persistent.crystal += 50
                    if persistent.ach[0][1] == 4:
                        persistent.crystal += 25
                    renpy.show_screen('get_ach_show', tm)
                    persistent.ach[0][4] = True
                    n_list = persistent.done_ach
                    n_list.insert(0, ach)
                    persistent.done_ach = n_list
            ach_pct()






define spacegetach = 40 if renpy.variant("small") else 30

screen get_ach_show(tm):
    zorder 100
    $ ach_name = persistent.ach[0][2]
    frame at ach_appear(tm):
        yalign 0.04
        xalign 0.04
        style_prefix "end_noti"
        hbox:
            add "ach_noti" yalign 0.6 zoom endnotizoom
            null width spacegetach
            vbox:
                text _("{size=-5}{font=gt}Достижение разблокировано!{/font}{/size}")
                text _("[ach_name]")
                timer 0.01 action Play("ui", "audio/ui_sfx/ach.flac")
    timer 3.25 action Hide('get_ach_show')

screen get_all_ach_show():
    zorder 100
    frame at ach_appear(0.1):
        yalign 0.2
        xalign 0.04
        style_prefix "end_noti"
        hbox:
            add "ach_noti" yalign 0.6 zoom endnotizoom
            null width spacegetach
            vbox:
                text _("{size=-5}{font=gt}Поздравляю!{/font}{/size}")
                text _("Игра полностью пройдена!")
                timer 0.01 action Play("ui", "audio/ui_sfx/all_ach.flac")
    timer 3.25 action Hide('get_all_ach_show')

transform ach_appear(tm):
    on show:
        xalign -1.0 alpha 1.0
        pause tm
        easein .25 xalign 0.04
    on hide:
        linear .3 alpha 0.0




style framedoneslot_frame:
    background Frame("slot_done")

style framedoneslot_text:
    color "#00000099"


default persistent.what_ach_show = 'common'

screen achievements():

    modal True
    tag menu
    use menus(_("Достижения"), frmside = True)

    vbox:
        style_prefix "stylebtside"
        xalign 0.0
        yalign 0.5
        xsize frmsidesize
        spacing 40

        button:
            xfill True
            ysize btsidesize
            vbox:
                xalign 0.5
                yalign 0.5
                text _("{=endtextsz}Общие") 
            activate_sound "audio/ui_sfx/touch.flac"
            action SetField(persistent, 'what_ach_show', 'common')

        button:
            xfill True
            ysize btsidesize
            vbox:
                xalign 0.5
                yalign 0.5
                spacing -10
                if renpy.variant("small"):
                    text _("Яндере") size 35
                    text _("Руи") size 35 xalign 0.5
                else:
                    text _("Яндере")
                    text _("Руи") xalign 0.5
            activate_sound "audio/ui_sfx/touch.flac"
            action SetField(persistent, 'what_ach_show', 'rui')

    frame at showendsmenu(0.25):
        style_prefix "styleframemenu"
        padding (frpadx, frpady)
        yalign yposset
        ysize setysize 
        xsize 1500

        vbox:
            ypos -30
            if persistent.what_ach_show == 'common':
                text _("{image=icontext1} {=settitle}Общие ачивки  |  [persistent.common_ach_pct]%")
            if persistent.what_ach_show == 'rui':
                text _("{image=icontext1} {=settitle}Яндере Руи  |  [persistent.rui_ach_pct]%")
            null width 20
            frame:
                xfill True
                ysize 5
                style_prefix "textline"


        hbox:
            xfill True
            ysize endssize
            yalign 0.6
            viewport id "ach":
                xfill True
                xpos -20
                draggable True
                mousewheel True
                arrowkeys True
                
                vbox:
                    xfill True
                    spacing 10

                    if persistent.what_ach_show == 'common':
                        frame:
                            if persistent.main_ach == True:
                                style_prefix "framedoneslot"
                            else:
                                style_prefix "frameendslot"
                            xfill True
                            ysize 150
                            hbox:
                                yalign 0.2
                                null width 20
                                vbox:
                                    spacing 8
                                    text _("Истинный фанат!") size 30
                                    text _("Откройте все ачивки в игре") size 25
                                    null height 1
                                    hbox:
                                        bar:
                                            xsize 1100
                                            ysize 30
                                            value persistent.all_ach_pct
                                            range 100
                                            if persistent.main_ach == True:
                                                left_bar Frame ("bar_done_left", 10,10)
                                                right_bar Frame ("bar_done_right", 10,10)
                                            else:
                                                left_bar Frame ("gui/bar/left_long.png", 10,10)
                                                right_bar Frame ("gui/bar/right_long.png", 10,10)
                                        null width 10
                                        text "[persistent.all_ach_pct]%" size 25 ypos -3


                    $ n = len(persistent.ach)

                    for j in range(0, n):

                        if persistent.what_ach_show == persistent.ach[j][0]:

                            frame:
                                if persistent.ach[j][4] == True:
                                    style_prefix "framedoneslot"
                                else:
                                    style_prefix "frameendslot"
                                xfill True
                                ysize 150

                                $ name_ach = persistent.ach[j][2]
                                if persistent.ach[j][4] == False and (persistent.ach[j][1] == 3 or persistent.ach[j][1] == 4):
                                    $ text_ach = _('(Условия выполнения скрыты)')
                                else:
                                    $ text_ach = persistent.ach[j][3]
                                if persistent.ach[j][1] == 2 or persistent.ach[j][1] == 4:
                                    $ bar_value = persistent.ach[j][5]
                                    $ bar_range = persistent.ach[j][6]
                                else:
                                    if persistent.ach[j][4] == True:
                                        $ bar_value = 1
                                    else:
                                        $ bar_value = 0
                                    $ bar_range = 1

                                hbox:
                                    yalign 0.2
                                    null width 20
                                    vbox:
                                        spacing 8
                                        text "[name_ach]" size 30
                                        text "[text_ach]" size 25
                                        null height 1
                                        hbox:
                                            bar:
                                                xsize 1100
                                                ysize 30
                                                value bar_value
                                                range bar_range
                                                if persistent.ach[j][4] == True:
                                                    left_bar Frame ("bar_done_left", 10,10)
                                                    right_bar Frame ("bar_done_right", 10,10)
                                                else:
                                                    left_bar Frame ("gui/bar/left_long.png", 10,10)
                                                    right_bar Frame ("gui/bar/right_long.png", 10,10)
                                            null width 10
                                            text "[bar_value]/[bar_range]" size 25 ypos -3

            null width 5

            vbar value YScrollValue("ach")


image bar_done_left:
    "gui/bar/left_long.png"
    alpha 0.8

image bar_done_right:
    "gui/bar/right_long.png"
    alpha 0.8