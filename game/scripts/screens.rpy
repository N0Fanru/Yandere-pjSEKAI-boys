################################################################################
## Инициализация
################################################################################

init offset = -1


################################################################################
## Стили
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    unscrollable "hide"
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize 50
    base_bar Frame("gui/slider/horizontal_bar.png", gui.slider_borders, tile=gui.slider_tile)
    left_bar Frame("gui/slider/horizontal_bar_full.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Внутриигровые экраны
################################################################################

screen r_studio():

    button:
        xsize 300 ysize 300
        xalign 0.35 yalign 0.5
        action Jump('rui_studio.kaito_tell')

    button:
        xsize 250 ysize 250
        xalign 0.52 yalign 0.45
        if not tasks['studio'][0] and can_card:
            action Jump('rui_studio.shema')

screen r_room():

    button:
        xsize 330 ysize 250
        xalign 0.25 yalign 0.95
        if not tasks['room'][0] and talk_kaito:
            action Jump('rui_room.book')

    button:
        xsize 200 ysize 350
        xalign 0.85 yalign 0.57
        if not tasks['room'][1] and talk_kaito:
            action Jump('rui_room.vaza')

    button:
        xsize 220 ysize 320
        xalign 0.18 yalign 0.6
        if not tasks['room'][2] and talk_kaito:
            action Jump('rui_room.lampa')

screen r_bedroom():

    button:
        xsize 700 ysize 900
        xalign 0.45 yalign 0.2
        if not tasks['bedroom'][0] and talk_kaito:
            action Jump('rui_bedroom.sh')

screen r_kitchen():

    button:
        xsize 350 ysize 250
        xalign 0.25 yalign 0.55
        if not tasks['kitchen'][0] and talk_kaito:
            action Jump('rui_kitchen.food')

    button:
        xsize 350 ysize 250
        xalign 0.7 yalign 0.1
        if not tasks['kitchen'][1] and talk_kaito:
            action Jump('rui_kitchen.wt')

    button:
        xsize 350 ysize 250
        xalign 1.0 yalign 0.05
        if not tasks['kitchen'][2] and talk_kaito:
            action Jump('rui_kitchen.kn')

screen r_toilet():

    button:
        xsize 250 ysize 300
        xalign 0.55 yalign 0.65
        if not tasks['toilet'][0] and talk_kaito:
            action Jump('rui_toilet.pl')

    button:
        xsize 150 ysize 150
        xalign 0.38 yalign 0.08
        if not tasks['toilet'][1] and talk_kaito:
            action Jump('rui_toilet.ml')
        

image btn_card:
    "card"
    btn

image hover_card:
    "card"
    bt_hover

screen card_button():

    imagebutton:
        anchor (0.5, 0.5) xpos 130 ypos 240
        idle "btn_card"
        hover "hover_card"
        activate_sound "audio/ui_sfx/close.flac"
        if can_card:
            action Show('rui_home_scheme', transition=Dissolve(.3))

screen rui_home_scheme():
    zorder 81
    modal True

    $ coord = {'studio': [0.733, 0.93],
    'room': [0.63, 0.4],
    'bedroom': [0.5, 0.4],
    'toilet': [0.25, 0.38],
    'kitchen': [0.25, 0.5]}

    add "rui home"
    add "pr1" xalign coord[locate][0] yalign coord[locate][1]

    button:
        xsize 450 ysize 300 xalign 0.78 yalign 0.95
        #add Solid("#000000")
        if locate != 'studio':
            action [SetVariable("rui_time", rui_time-(abs(locates.index(locate)-locates.index('studio')))*2), Jump('rui_studio')]

    button:
        xsize 450 ysize 520 xalign 0.78 yalign 0.4
        #add Solid("#00fa25")
        if locate != 'room':
            action [SetVariable("rui_time", rui_time-(abs(locates.index(locate)-locates.index('room')))*2), Jump('rui_room')]

    button:
        xsize 450 ysize 520 xalign 0.47 yalign 0.69
        #add Solid("#ab00fa")
        if locate != 'bedroom':
            action [SetVariable("rui_time", rui_time-(abs(locates.index(locate)-locates.index('bedroom')))*2), Jump('rui_bedroom')]

    button:
        xsize 230 ysize 320 xalign 0.2 yalign 0.2
        #add Solid("#004bfa")
        if locate != 'toilet':
            action [SetVariable("rui_time", rui_time-(abs(locates.index(locate)-locates.index('toilet')))*2), Jump('rui_toilet')]

    button:
        xsize 350 ysize 450 xalign 0.22 yalign 0.75
        #add Solid("#fa7000")
        if locate != 'kitchen':
            action [SetVariable("rui_time", rui_time-(abs(locates.index(locate)-locates.index('kitchen')))*2), Jump('rui_kitchen')]

    imagebutton:
        anchor (0.5, 0.5) xpos posreturn+50 ypos 88
        idle "btn_return"
        hover "hover_return"
        keysym ('K_ESCAPE')
        activate_sound "audio/ui_sfx/close.flac"
        action Hide("rui_home_scheme", transition=Dissolve(.3))


screen rui_moning:
    default show = [True, True, True]

    for i in range(2, 5):

        if show[i-2]:

            $ im = "m" + str(i)
            imagebutton idle im focus_mask im action [SetDict(show, i-2, False), Jump('good_moning.'+im)]

    $ v  = "vaf2" if vafli else "vaf1"
    imagebutton idle v focus_mask v action Jump('good_moning.vaf')


transform rui_timer:
    xalign 0.14 yalign 0.115 alpha 0.0
    linear 0.2 alpha 1.0

style phone_text is text:
    font "good timing.ttf"

screen rui_timer():
    style_prefix "phone"

    if len(str(rui_time%60)) == 2:
        $ t = str(rui_time//60) + ":" + str(rui_time%60)
    else:
        $ t = str(rui_time//60) + ":0" + str(rui_time%60)

    text t size 50 at rui_timer

    timer 5.0 repeat True action If(rui_time>0, SetVariable("rui_time", rui_time-1), Jump("rui_return")) # 5.0





screen phone():
    style_prefix "phone"

    $ year, month, day, hour, minute, second, dow, doy, dst = time.localtime()
    if len(str(minute)) == 1:
        $ minute = '0'+str(minute)
    if len(str(day)) == 1:
        $ day = '0'+str(day)
    if len(str(month)) == 1:
        $ month = '0'+str(month)

    add 'phone' xalign 0.5 zoom 0.5 yalign -0.3

    text "{size=150}00:[minute]{/size}" xalign 0.5 yalign 0.4
    text "{size=50}[day].[month].[year]{/size}" xalign 0.5 yalign 0.55

    add 'framemenus' zoom 0.68 xalign 0.5 yalign 0.83 alpha 0.5

    text "{color=#000}{size=40}World hasn't even started{/size}{/color}" xalign 0.5 yalign 0.7
    hbox:
        xalign 0.5 yalign 0.8 spacing 150
        text "{color=#000}{size=65}<{/size}{/color}"
        button:
            yalign 0.5
            text "{color=#000}{size=75}▸{/size}{/color}" style "skip_triangle"
            if can_sekai:
                action [Show("enter_sekai"), Play("audio", ["audio/ui_sfx/sekai_enter.flac", "<silence .5>", "audio/ui_sfx/sekai_enter.flac"])]
        text "{color=#000}{size=65}>{/size}{/color}"

image ender_sekai:
    Solid("#fff")
    alpha 0.0
    easein_back 0.2 alpha 0.7
    easein_back 0.1 alpha 0.0
    pause 0.2
    easein_back 0.2 alpha 0.3
    linear 0.5 alpha 0.0

screen enter_sekai():
    modal True

    add "ender_sekai"

    timer 1.0 action Jump("wond_sekai")

screen loading():
    add "loading" xalign 0.95 yalign 0.98


style styleframe_text is text:
    color "#000"

style styleframe_text is text:
    variant "small"
    color "#000"
    size 40

style start_text is text:
    font "good timing.ttf"

# экраны перед началом игры

# screen hedkonon():
#     style_prefix "start"

#     vbox:
#         xalign 0.5
#         yalign 0.5
#         spacing 10
#         text _("{b}{size=+15}{color=#980002}Внимание! Треш-новелла!{/color}{/size}{/b}") xalign 0.5
#         null height 50
#         text _("{i}Проходите игру на свой страх и риск!{/i}") xalign 0.5
#         text _("Игра содержит множество абсоурдных, аморальных и триггерных тем.")
#         null height 50
#         text _("Действия в игре происходят в АУ и никак не связаны каноном!") xalign 0.5
#         text _("В пределах этой новеллы {b}все{/b} персонажи достигли {b}18 лет{/b}!") xalign 0.5
#         null height 50
#         text _("Новелла сделана в несерьёзной форме, ради рофла и опыта.") xalign 0.5
#         text _("{u}Не воспринимайте всё всерьёз!{/u}") xalign 0.5
#         null height 50
#         text _("Эта бета-версия игры! Все ошибки сообщать NoFanru.") xalign 0.5
#         text "{a=https://tapy.me/nofanru}https://tapy.me/nofanru{/a}" xalign 0.5

        
screen waring():
    style_prefix "start"
    
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        text _("{b}{size=+15}{color=#980002}Внимание! Треш-новелла!{/color}{/size}{/b}") xalign 0.5
        null height 50
        text _("{i}Проходите на свой страх и риск!{/i}") xalign 0.5
        text _("Игра содержит множество абсоурдных, аморальных и триггерных тем,") xalign 0.5
        text _("которые могут быть крайне неприятны некоторым лицам.") xalign 0.5
        null height 50
        text _("Действия в игре происходят в АУ и никак не связаны каноном!") xalign 0.5
        text _("В пределах этой новеллы {b}все{/b} персонажи достигли {b}18 лет{/b}!") xalign 0.5
        null height 50
        text _("Новелла сделана в несерьёзной форме, ради шутки и опыта.") xalign 0.5
        text _("{i}Не воспринимайте всё всерьёз!{/i}") xalign 0.5
        null height 50
        text _("Игра сделана N0Fanru.") xalign 0.5
        text "{a=https://t.me/nofanru}https://t.me/nofanru{/a}" xalign 0.5


screen sponsors():
    style_prefix "start"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 10
        text _("{size=+15}{color=#ffd700}Спасибо спонсорам с Boosty!{/color}{/size}") xalign 0.5
        text "{size=-5}{a=https://boosty.to/nofanru}https://boosty.to/nofanru{/a}{/size}" xalign 0.5
        null height 50
        text "- Ари" xalign 0.5
        text "- Angrrry Panda" xalign 0.5
        null height 20
        text _("{size=-15}И другие{/size}") xalign 0.5


screen permission():
    modal True
    frame at showframe(0.1):
        xalign 0.5
        yalign 0.5
        padding (frpadx, frpady)

        vbox:
            style_prefix "styleframe"
            text _("При отсутствии доступа к файлам приложение") xalign 0.5
            text _("может работать некоректно!") xalign 0.5
            null height nullsp
            text _("Перезапустите игру или выдайте") xalign 0.5
            text _("разрешение через настройки приложения.") xalign 0.5
            null height nullbt
            hbox:
                ysize framey
                xalign 0.5
                imagebutton:
                    ycenter ycen
                    idle "btn ok"
                    hover "hover ok"
                    #activate_sound 
                    action Hide("permission") xalign 0.5


style titles_text is text:
    size 20

style titles_text is text:
    variant "small"
    size 25

screen titlestart():

    vbox:
        style_prefix "titles"
        xalign 0.03
        yalign 0.98
        text _("Оригинальная игра: Project Sekai: Colorful Stage!"):
            outlines [(1, "#00000078", 3, 2)]
        text _('Все авторские права и кредиты указаны во вкладке "Об игре"'):
            outlines [(1, "#00000078", 3, 2)]

    vbox:
        xalign 0.03
        yalign 0.03
        text "v. [config.version]":
            outlines [(1, "#00000078", 3, 2)]

    if renpy.variant("touch"):
        text _("{font=good timing.ttf}Нажмите на экран, чтобы начать игру{/font}") at tapatl:
            outlines [ (20, "#98000306", 0, 0), (15, "#9800030e", 0, 0), (10, "#98000314", 0, 0), (7, "#98000320", 0, 0), (3, "#98000326", 0, 0), (2, "#9800033b", 0, 0), (2, "#98000363", 0, 0)]
    else:
        text _("{font=good timing.ttf}Нажмите Enter, чтобы начать игру{/font}") at tapatl:
            outlines [ (20, "#98000306", 0, 0), (15, "#9800030e", 0, 0), (10, "#98000314", 0, 0), (7, "#98000320", 0, 0), (3, "#98000326", 0, 0), (2, "#9800033b", 0, 0), (2, "#98000363", 0, 0)]

transform tapatl:
    xalign 0.5 yalign 0.85 alpha 0.0
    pause 0.5
    
    block:
        ease 1.0 alpha 1.0
        pause 0.8
        ease 1.0 alpha 0.0
        pause 0.1
        repeat



define vol_show = 0.2

screen soon():
    modal True
    if persistent.low != 2:
        timer 0.01 action Play("ui", "audio/ui_sfx/show.flac", relative_volume=vol_show)
    frame at showframe(0.05):
        style_prefix "styleframe"
        xalign 0.5
        yalign 0.5
        padding (frpadx, frpady)

        vbox:
            text _("Новый персонаж будет добавлен") xalign 0.5
            text _("в следующих версиях игры...") xalign 0.5
            null height nullsp
            text _("Следите за новостями!") xalign 0.5
            null height nullbt
            hbox:              
                ysize framey
                xalign 0.5
                imagebutton:
                    ycenter ycen
                    idle "btn ok"
                    hover "hover ok"
                    keysym('K_RETURN')
                    activate_sound "audio/ui_sfx/close.flac"
                    action Hide("soon") xalign 0.5
                    
image btn ok:
    "bt ok"
    btn

image hover ok:
    "bt ok"
    bt_hover

image btn yes:
    "bt yes"
    btn

image hover yes:
    "bt yes"
    bt_hover

image btn no:
    "bt no"
    btn

image hover no:
    "bt no"
    bt_hover

transform showframe(pe):
    choice(persistent.low == 0):
        zoom 0.1 alpha 0.0
        pause pe
        alpha 1.0
        ease 0.2 zoom 1.0
    choice(persistent.low == 1):
        alpha 0.0
        pause 0.08
        ease 0.15 alpha 1.0
    choice(persistent.low == 2):
        pause 0.08
        alpha 1.0

    on hide:
        choice(persistent.low == 0):
            pause 0.05
            ease 0.2 zoom 0.1
            alpha 0.0
        choice(persistent.low == 1):
            pause 0.05
            ease 0.15 alpha 0.0
        choice(persistent.low == 2):
            pause 0.05
            alpha 0.0
        

define nullsp = 40
define nullbt = 70

define frpadx = 75 if renpy.variant("small") else 55
define frpady = 75 if renpy.variant("small") else 65
define framey = 110 if renpy.variant("small") else 80

define ycen = 60 if renpy.variant("small") else 45

define twobt = 320 if renpy.variant("small") else 250
define twobtx = 160 if renpy.variant("small") else 125

# подтверждение об начале игры (Руи)
screen Rui_play():
    modal True
    if persistent.low != 2:
        timer 0.01 action Play("ui", "audio/ui_sfx/show.flac", relative_volume=vol_show)

    frame at showframe(0.08):
        style_prefix "styleframe"
        xalign 0.5
        yalign 0.5
        padding (frpadx, frpady)
        $ ends = len(all_rui_end_code)

        vbox:
            null height 10
            text _("Яндере партнёр Камиширо Руи") xalign 0.5
            text _("Открыто концовок: [persistent.rui_ends] из [ends]") xalign 0.5
            null height 30
            text _("{size=-12}Содержащиеся триггеры:{/size}") xalign 0.5
            text _("{size=-12}секс, насилие, изнасилование,{/size}") xalign 0.5
            text _("{size=-12}абьюз, похищение, нездоровые фетиши,{/size}") xalign 0.5
            text _("{size=-12}полиаморные отношения{/size}") xalign 0.5
            null height nullsp
            text _("Начать игру?") xalign 0.5
            null height nullsp

            hbox:
                ysize framey
                xalign 0.5
                vbox:
                    xsize twobt
                    imagebutton:
                        ycenter ycen xcenter twobtx
                        idle "btn no"
                        hover "hover no"
                        keysym('K_ESCAPE')
                        activate_sound "audio/ui_sfx/close.flac"
                        action Hide("Rui_play")
                null width 10
                vbox:
                    xsize twobt           
                    imagebutton:
                        ycenter ycen xcenter twobtx
                        idle "btn yes"
                        hover "hover yes"
                        keysym('K_RETURN')
                        activate_sound "audio/ui_sfx/choice.flac"
                        action [SetField(persistent, 'markerr', 'startRui'), Show("timestart")]  #startRui    

screen timestart():
    timer tmstart action [SetField(persistent, 'in_game_menu', False), Start(persistent.markerr)]

define tmstart = 0.12 if renpy.variant("touch") else 0.01

# таймер
screen timerr():
    timer 0.05 repeat True action If(timerr>0, SetVariable('timerr', timerr-0.05), Jump(marker))

# timerr - время 
# marker - переход к лейблу, если игрок не успел выбрать

screen timewh():
    timer 0.05 repeat True action SetVariable('timerr', timerr+0.05)
    

screen secret1():
    imagebutton:
        idle "secret1"
        action Call("secret1")
        xalign 0.468

screen return_s():
    timer 0.05 repeat True action If(timerr>0, SetVariable('timerr', timerr-0.05), MainMenu(confirm=False, save=False))
    imagebutton:
        idle "secret1-1"
        action MainMenu(confirm=False, save=False)












transform showmoremain(pe):
    choice(persistent.low == 0):
        zoom 0.1 alpha 0.0
        pause pe
        alpha 1.0
        ease 0.2 zoom 1.0
    choice(persistent.low == 1):
        alpha 0.0
        pause 0.08
        ease 0.15 alpha 1.0
    choice(persistent.low == 2):
        pause 0.08
        alpha 1.0

    on hide:
        choice(persistent.low < 2):
            pause 0.05
            ease 0.15 alpha 0.0
        choice(persistent.low == 2):
            pause 0.05
            alpha 0.0
        # ease 0.2 alpha 0.0



screen endswait():
    timer 0.1 action [Hide("endswait"),  Hide("moremain"), ShowMenu("ends")]

screen setwait():
    timer 0.05 action [Hide("setwait"),  Hide("moremain"), ShowMenu("settings")]


# экран с параметрами в главном меню
screen moremain():
    modal True
    if persistent.low != 2:
        timer 0.01 action Play("ui", "audio/ui_sfx/show.flac", relative_volume=vol_show)
    add "gui/overlay/confirm.png" alpha 0.7 at disall(0.0, 0.03, 0.07, 0.03)
    frame at showmoremain(0.08):
        style_prefix "styleframe"
        xalign 0.5
        yalign 0.5
        ysize moreysize 
        xsize morexsize

        hbox:
            xcenter morexposeall

            vbox:
                xsize twobt 
                imagebutton:
                    ycenter moreypose1 xcenter morexpose1
                    idle "btn save"
                    hover "hover save"
                    keysym('K_1', 'K_s')
                    activate_sound "audio/ui_sfx/touch.flac"
                    action [Hide("moremain"), ShowMenu("load")]

            vbox:
                xsize twobt 
                imagebutton:
                    ycenter moreypose1 xcenter morexpose2
                    idle "btn ends"
                    hover "hover ends"
                    keysym('K_2', 'K_e')
                    if renpy.get_screen('ends'):
                        activate_sound "audio/ui_sfx/touch.flac"
                        action Hide("moremain")
                    else:
                        activate_sound "audio/ui_sfx/touch.flac"
                        action [Show("loading"), Show("endswait")]

            vbox:
                xsize twobt 
                imagebutton:
                    ycenter moreypose1 xcenter morexpose3
                    idle "btn ach"
                    hover "hover ach"
                    keysym('K_3', 'K_a')
                    activate_sound "audio/ui_sfx/touch.flac"
                    action [Hide("moremain"), ShowMenu("achievements")] 

        hbox:
            xcenter morexposeall

            vbox:
                xsize twobt 
                imagebutton:
                    ycenter moreypose2 xcenter morexpose1
                    idle "btn set"
                    hover "hover set"
                    keysym('K_4', 'K_p')
                    if renpy.get_screen('settings'):
                        activate_sound "audio/ui_sfx/touch.flac"
                        action Hide("moremain")
                    else:
                        activate_sound "audio/ui_sfx/touch.flac"
                        action [SetField(persistent, 'mainmenu', True), Show("loading"), Show("setwait")]

            vbox:
                xsize twobt 
                imagebutton:
                    ycenter moreypose2 xcenter morexpose2
                    idle "btn about"
                    hover "hover about"
                    keysym('K_5', 'K_j')
                    activate_sound "audio/ui_sfx/touch.flac"
                    action [Hide("moremain"), ShowMenu("info")]

            vbox:
                xsize twobt 
                imagebutton:
                    ycenter moreypose2 xcenter morexpose3
                    idle "btn exit"
                    hover "hover exit"
                    keysym('K_6', 'K_q')
                    activate_sound "audio/ui_sfx/touch.flac"
                    action Quit(confirm=True)

        imagebutton:
            ycenter moreclosepose 
            idle "btn close"
            hover "hover close"
            keysym('K_ESCAPE')
            activate_sound "audio/ui_sfx/close.flac"
            action Hide("moremain") xalign 0.5

        text _("{=framename}Меню") xalign 0.5 yalign -0.02

style framename:
    color "#fff"
    font "gt"
    size 40

style framename:
    variant "small"
    color "#fff"
    font "gt"
    size 55

define morexposeall = 550 if renpy.variant("small") else 418

define moreypose1 = 160 if renpy.variant("small") else 130
define moreypose2 = 330 if renpy.variant("small") else 250
define morexpose1 = 200 if renpy.variant("small") else 200
define morexpose2 = 250 if renpy.variant("small") else 250
define morexpose3 = 300 if renpy.variant("small") else 300

define moreysize = 700 if renpy.variant("small") else 550
define morexsize = 1300 if renpy.variant("small") else 1100
define moreclosepose = 560 if renpy.variant("small") else 430

image btn close:
    "bt close"
    btn

image hover close:
    "bt close"
    bt_hover

default persistent.mainmenu = False



# надпись об необходимости перезагрузить игру
screen reload():
    modal True
    if persistent.low != 2:
        timer 0.01 action Play("ui", "audio/ui_sfx/show.flac", relative_volume=vol_show)
    add "gui/overlay/confirm.png" alpha 0.7 at disall(0.0, 0.03, 0.07, 0.03)
    frame at showframe(0.05):
        style_prefix "styleframe"
        xalign 0.5
        yalign 0.5
        padding (frpadx, frpady)

        vbox:
            text _("Для вступления изменений в силу игра") xalign 0.5
            text _("будет перезапущено!") xalign 0.5
            if renpy.variant("android"):
                null height nullsp
            text _("На адроид-устройствах после выхода закройте") xalign 0.5
            text _("вкладку с игрой и зайди в игру заново!") xalign 0.5
            null height nullbt
            hbox:
                ysize framey
                xalign 0.5
                vbox:
                    xsize twobt
                    imagebutton:
                        ycenter ycen xcenter twobtx
                        idle "btn cancel"
                        hover "hover cancel"
                        keysym('K_ESCAPE')
                        activate_sound "audio/ui_sfx/close.flac"
                        action Hide("reload")
                null width 10
                vbox:
                    xsize twobt           
                    imagebutton:
                        ycenter ycen xcenter twobtx
                        idle "btn okred"
                        hover "hover okred"
                        keysym('K_RETURN')
                        activate_sound "audio/ui_sfx/touch.flac"
                        action [SetField(persistent, setpername, setperval), Function(renpy.quit, relaunch=True, save=True)]

define setpername = ""
define setperval = ""













#######################################################################################################
## Экран для всех меню ################################################################################
#######################################################################################################
#######################################################################################################

define posreturn = 80 if renpy.variant("small") else 70
define poslinemenu = 380 if renpy.variant("small") else 300
define textlinesize = 40 if renpy.variant("small") else 30
define ypostextline = 110 if renpy.variant("small") else 107
define xpostextline = 150 if renpy.variant("small") else 125

style frameside_frame:
    background Frame("side_frame", tile=gui.frame_tile)

style framesideline_frame:
    background Frame("side_frame_line", tile=gui.frame_tile)

define frmsidesize = 300 if renpy.variant("small") else 250
define frmsideline = 7

screen menus(title, frmside = False):

    modal True
    if persistent.low != 2:
        timer 0.01 action Play("ui", "audio/ui_sfx/show.flac", relative_volume=vol_show)

    add "main bg"
    if renpy.variant("small") and persistent.low != 2:
        add "main bg-tex" alpha 0.2 zoom 1.5 xalign 0.5 yalign 0.5
    elif persistent.low != 2:
        add "main bg-tex" alpha 0.2

    if persistent.low == 0:
        add "main_line" xalign 0.05 yalign 1.0

    if frmside:
        hbox:
            xalign 0.0
            frame:
                style_prefix "frameside"
                yfill True
                xsize frmsidesize
            frame:
                style_prefix "framesideline"
                yfill True
                xsize frmsideline

    add "menuline" anchor (0.5, 0.5) xpos poslinemenu ypos 88
    text "{image=textmenueim} [title]" anchor (0.0, 0.5) xpos xpostextline ypos ypostextline size textlinesize
    imagebutton:
        anchor (0.5, 0.5) xpos posreturn ypos 88
        idle "btn_return"
        hover "hover_return"
        keysym ('K_ESCAPE')
        activate_sound "audio/ui_sfx/close.flac"
        action Return()

    if not persistent.in_game_menu:
        imagebutton:
            anchor (0.5, 0.5) xpos 1835 ypos 88
            idle "btn more"
            hover "hover more"
            keysym ('K_SPACE')
            activate_sound "audio/ui_sfx/touch.flac"
            action Show("moremain")

define titleimsize = 0.8 if renpy.variant("small") else 0.5

image textmenueim:
    "text_menu"
    ypos 10
    zoom titleimsize

image menuline:
    "menuframe"
    zoom btnsize

image btn_return:
    "bt return"
    btn

image hover_return:
    "bt return"
    bt_hover




#######################################################################################################
## Экран об игре ######################################################################################
#######################################################################################################
#######################################################################################################

define abtsize = 600 if renpy.variant("small") else 510

default persistent.info = "about"

screen info():

    modal True
    tag menu
    use menus(_("Об игре"))

    frame at showframemenu(0.25):
        style_prefix "styleframemenu"
        padding (frpadx, frpady)
        xalign 0.5
        yalign yposset
        ysize setysize 
        xsize setxsize

        imagebutton:
            anchor (0.5, 0.5) xpos 150 ypos 20
            idle "btn info"
            hover "hover info"
            selected_idle "btnsel info"
            selected_hover "hoversel info"
            activate_sound "audio/ui_sfx/touch.flac"
            action SetField(persistent, 'info', "about")

        imagebutton:
            anchor (0.5, 0.5) xpos 480 ypos 20
            idle "btn credits"
            hover "hover credits"
            selected_idle "btnsel credits"
            selected_hover "hoversel credits"
            activate_sound "audio/ui_sfx/touch.flac"
            action SetField(persistent, 'info', "credits")

        imagebutton:
            anchor (0.5, 0.5) xpos 810 ypos 20
            idle "btn update"
            hover "hover update"
            selected_idle "btnsel update"
            selected_hover "hoversel update"
            activate_sound "audio/ui_sfx/touch.flac"
            action SetField(persistent, 'info', "update")

        hbox:
            xfill True
            ysize abtsize
            yalign 0.6
            spacing setnull1

            viewport id "abt":
                yinitial 0.0
                mousewheel True
                draggable True

                xfill True

                vbox:
                    xfill True
                    spacing -5

                    if persistent.info == 'about':

                        label "Yandere pjSEKAI boys"
                        null height 20
                        text _("{size=-5}Версия: [config.version]{/size}")
                        text _("{size=-5}Создатель: N0Fanru{/size}")
                        text _("{size=-5}Коротное название: Yandere SEKAI или Яндере Руи{/size}")
                        null height 40
                        text _p("""Yandere pjSEKAI boys - это фанатская визуальная треш-новелла, сделанная по ритм-игре Project SEKAI: COLORFUL STAGE! и основанная на тренде из TikTok "Яндере Партнёр".
                        
                        Изночально в игре пларировались разные ветки со всеми мужскими персонажами из секая, но проект из-за личных объстоятельтв создание Яндере Руи сильно затянулась, а потом интерес к игре утух.
                        
                        Жанр треш-новеллы подразумевает под собой абсурдный, местами сюрреалистический, контент, выходящий за рамки адекватности и здравого смысла. Игра сделана в несерьёзной форме, ради шутки и получения опыта.
                        
                        В игре используется хедканоны и АУ, в том числе и на то, что все персонажи достигли 18 лет! Характер персонажей также изменён и практически не имеет ничего общего с каноном.
                        """)

                        null height 20 

                    elif persistent.info == 'credits':

                        label _("Разработчики")
                        null height 40
                        text _("Главный разрабтчик, сценарист, кодер, MMDer:")
                        null height 20
                        hbox:
                            add "nofim"
                            null width 20
                            vbox:
                                ypos -5
                                text "{size=+8}{color=#ffa800}N0Fanru{/color}{/size}"
                                text "{size=-8}Telegram: {a=https://t.me/nofanru}@nofanru{/a}{/size}"
                                text _("{size=-8}Все ссылки: {a=https://tapy.me/nofanru}tapy.me/nofanru{/a}{/size}")
                                text "{size=-8}Gmail: nofanru@gmail.com{/size}"
                        

                        null height 70
                        label _("Главные спонсоры с {a=https://boosty.to/nofanru}Boosty{/a}")
                        null height 40
                        text "- Ари"
                        text "- Angrrry Panda"


                        null height 70
                        label _("Авторские права и используемые материалы")
                        null height 40

                        text _p("""Оригинальные авторские права и персонажи:
                        {p}{size=-8}SEGA, Colorful Pallet, Crypton Future Media{/size}

                        Ren'Py плагины, ассеты и готовые коды:
                        {p}{size=-8}Kinetic-Text-Tags (SoDaRa), Renpy Auto Highlight, 7Dots, Knickknack PJ, RenpyRemix{/size}
                        
                        Музыка и звуки взяты с сайта {a=freesound.org}Freesound.org{/a}:
                        {p}{size=-8}Ghost Experiences, FoolBoyMedia, ispeakwaves, Setuniman, zagi2, Beetlemuse, SergeQuadrado, newlocknew, Sirkoto51{/size}
                        
                        Исходный интерфейс:
                        {p}{size=-8}SEGA, Colorful Pallet, Craft Egg{/size}
                        
                        Голос персонажей:
                        {p}{size=-8}VOCALOID, Proseka TTS, Easy GUI RVC (RVC v2){/size}
                        
                        Фоны:
                        {p}{size=-8}SEGA, Colorful Pallet; некоторые сгенерированы ИИ; некоторые сделаны при помощи MMD{/size}
                        
                        MikuMikuDance (спрайты и фоны):
                        {p}{size=-8}Сцены: amiamy111, shyuugah, gale-kun{/size}
                        {p}{size=-8}Модели персонажей: SEGA, Colorful Pallet, TearlessHen{/size}
                        {p}{size=-8}Используемые базы: Cham, Cyunaaa, Astria-MMD, TDA, onigiridojo, VRoid Studio{/size}
                        {p}{size=-8}Дополнительные модели: Jjinomu{/size}
                        {p}{size=-8}Эффекты для MME: ray-mmd, Junk Toon Shader, M4Toon2, Shadekai, PaletteShader{/size}
                        {p}
                        {p}Всё неуказаное использует лицензию CC0 или распространялось в интернете без указания автора.
                        """)

                    elif persistent.info == 'update':

                        label ("Обновление ver. 1.0.1")
                        null height 10
                        text _("Дата выхода в общий доступ: 19.06.2025")
                        null height 40
                        text _p("""- Исправлены ошибки...
                        """)
                        null height 50

                        label ("Обновление ver. 1.0")
                        null height 10
                        text _("Дата выхода на бусти: 28.04.2025")
                        text _("Дата выхода в общий доступ: 3.05.2025")
                        null height 40
                        text _p("""- 5 новых концовок
                        {p}- Новые секретные концовки
                        {p}- Добавлена мини-игра карточного дурака
                        {p}- Полностью доделана ветка с Руи
                        {p}- Финальная версия игры
                        """)
                        null height 50

                        label ("Обновление Beta 0.0.4")
                        null height 10
                        text _("Дата выхода на бусти: 17.08.2023")
                        text _("Дата выхода в общий доступ: 21.08.2023")
                        null height 40
                        text _p("""- Полностью изменён интерфейс игры, сделан более красивым, удобным и похожий на оригинальный интерфейс Project SEKAI
                        {p}- Добавлено информация об обновлении при первом заходе
                        {p}- Добавлены ачивки (27 ачивок, 193 шагов для получения каждой)
                        {p}- Добавлен титульный экран
                        {p}- Сжат размер файла игры
                        {p}- Добавление некоторых новых функций
                        {p}- Исправлены ошибки
                        {p}- Habet vocem
                        """)
                        null height 50

                        label _("Обновление Beta 0.0.3")
                        null height 10
                        text _("Дата выхода на бусти: 12.06.2023")
                        text _("Дата выхода в общий доступ: 16.06.2023")
                        null height 40
                        text _p("""- Добавлены 5 новых концовок
                        {p}- Добавлены новые секретные концовки
                        {p}- Растянута концовка с Руи-собачкой
                        {p}- Изменены некоторые части интерфейса
                        {p}- Исправлены ошибки
                        {p}- Nunc Lbjup te spectat
                        """)
                        null height 50

                        label ("Обновление Beta 0.0.2.1")
                        null height 10
                        text _("Дата выхода: 05.05.2023")
                        null height 40
                        text _("- Исправлены ошибки и баги")
                        null height 50

                        label ("Обновление Beta 0.0.2")
                        null height 10
                        text _("Дата выхода: 03.05.2023")
                        null height 40
                        text _p("""- Добавлены 10 новых концовок
                        {p}- Добавлены секретные концовки
                        {p}- Добавлена галерея концовок
                        {p}- Имя вводится один раз и изменяется в настройках 
                        """)
                        null height 50

                        label ("Обновление Beta 0.0.0 (Первоапрельская)")
                        null height 10
                        text _("Дата выхода: 01.04.2023")
                        null height 40
                        text _("Заходят в бар Руи и т/и...")
                        null height 50

                        label ("Обновление Beta 0.0.1")
                        null height 10
                        text _("Дата выхода: 25.03.2023")
                        null height 40
                        text _p("""- Первая версия игры
                        {p}- Всего 7 концовок
                        """)


            vbar value YScrollValue("abt") xpos -5

image nofim:
    "nofanruim"
    zoom nofimsize

define nofimsize = 0.5 if renpy.variant("small") else 0.4


image btn update:
    "bt update_unselect"
    btn_all

image hover update:
    "bt update_unselect"
    bt_all_hover

image btnsel update:
    "bt update_select"
    btn_all

image hoversel update:
    "bt update_select"
    bt_all_hover

image btn info:
    "bt info_unselect"
    btn_all

image hover info:
    "bt info_unselect"
    bt_all_hover

image btnsel info:
    "bt info_select"
    btn_all

image hoversel info:
    "bt info_select"
    bt_all_hover

image btn credits:
    "bt credits_unselect"
    btn_all

image hover credits:
    "bt credits_unselect"
    bt_all_hover

image btnsel credits:
    "bt credits_select"
    btn_all

image hoversel credits:
    "bt credits_select"
    bt_all_hover
            
                
transform bt_all_hover:
    zoom 1.0
    ease 0.1 zoom btnsizehoverall

transform btn_all:
    zoom 1.0

# define btnsize = 1.3 if renpy.variant("small") else 1.0
define btnsizehoverallsize = 0.96 if renpy.variant("small") else 0.93

define btnsizehoverall = btnsizehoverallsize if persistent.low == 0 else 1.0

# define btmsize = 1.5 if renpy.variant("small") else 1.1
# define btmsizehover = 1.35 if renpy.variant("small") else 1.0




#######################################################################################################
## Экран настроек #####################################################################################
#######################################################################################################
#######################################################################################################

define setysize = 900 if renpy.variant("small") else 800
define setxsize = 1700 if renpy.variant("small") else 1500
define setsize = 650 if renpy.variant("small") else 600

define yposset = 1.1 if renpy.variant("small") else 0.75

define setnull0 = 10 if renpy.variant("small") else 0.0
define setnull1 = 30 if renpy.variant("small") else 20
define setnull2 = 50 if renpy.variant("small") else 30
define setnull3 = 20 if renpy.variant("small") else 0.0
define setnull4 = 65 if renpy.variant("small") else 50

define spset = 35 if renpy.variant("small") else 5
define btsetypos1 = 35 if renpy.variant("small") else 30
define frsetypos1 = 560 if renpy.variant("small") else 500

define setlinesize = setxsize-200 if renpy.variant("small") else setxsize-150
define setbaresize = setxsize-450 if renpy.variant("small") else setxsize-400
define setbaresize2 = setxsize-1070 if renpy.variant("small") else setxsize-900


define posforshowframe = 10.0 if renpy.variant("small") else 5.0

transform showframemenu(pe):
    choice(persistent.low == 0):
        xalign posforshowframe
        pause pe
        linear 0.2 xalign 0.5
    choice(persistent.low > 0):
        xalign 0.5

style styleframemenu_text is text:
    color "#000"

style styleframemenu_text is text:
    variant "small"
    color "#000"
    size 40

style styleframemenu_frame:
    padding gui.frame_borders.padding
    background Frame("framemenus", gui.frame_borders, tile=gui.frame_tile)

screen settings():

    modal True
    tag menu

    use menus(_("Настройки"))

    timer 0.01 action Hide("loading")

    frame at showframemenu(0.25):
        style_prefix "styleframemenu"
        padding (frpadx, frpady)
        xalign 0.5
        yalign yposset
        ysize setysize 
        xsize setxsize

        hbox:
            xfill True
            ysize setsize

            viewport id "st":
                xfill True
                draggable True
                mousewheel True
                arrowkeys True

                vbox:
                    xfill True
                    spacing 2

                    null height setnull0

                    text _("{image=icontext1} {=settitle}Игровой процесс")
                    frame:
                        xsize setlinesize
                        ysize 5
                        style_prefix "textline"
                    null height setnull1

                    hbox:
                        vbox:
                            frame:
                                style_prefix "frametextred"
                                text _("Качество эффектов и переходов")
                            null height 20
                            hbox:
                                xalign 0.5
                                spacing spset
                                button:
                                    text _("{image=set_low0} Высокое")
                                    activate_sound "audio/ui_sfx/touch.flac"
                                    action [SetVariable("setpername", "low"), SetVariable("setperval", 0), Show("reload")]
                                    #action SetField(persistent, 'low', 0)
                                button:
                                    text _("{image=set_low1} Среднее")
                                    activate_sound "audio/ui_sfx/touch.flac"
                                    action [SetVariable("setpername", "low"), SetVariable("setperval", 1), Show("reload")]
                                button:
                                    text _("{image=set_low2} Низкое")
                                    activate_sound "audio/ui_sfx/touch.flac"
                                    action [SetVariable("setpername", "low"), SetVariable("setperval", 2), Show("reload")]
                        null width 70
                        if renpy.variant("pc") or renpy.variant("web"):
                            vbox:
                                frame:
                                    xalign 0.5
                                    style_prefix "frametextred"
                                    text _("Режим экрана")
                                null height 20
                                hbox:
                                    spacing 5
                                    button:
                                        text _("{image=set_screenwin} Оконный")
                                        activate_sound "audio/ui_sfx/touch.flac"
                                        action Preference("display", "window")
                                    button:
                                        text _("{image=set_screenfull} Полный")
                                        activate_sound "audio/ui_sfx/touch.flac"
                                        action Preference("display", "fullscreen")

                    null height setnull2
                    vbox:
                        frame:
                            style_prefix "frametextred"
                            text _("Имя персонажа: [persistent.name]")
                        null height setnull3
                        hbox:
                            null height 100
                            anchor (0.5, 0.5) xalign 0.5 ypos 50
                            imagebutton:
                                anchor (0.5, 0.5) xalign 0.5 ypos 40
                                idle "btn change"
                                hover "hover change"
                                activate_sound "audio/ui_sfx/touch.flac"
                                action [Show("inputtoo")]                    

                    null height setnull4
                    text _("{image=icontext1} {=settitle}Настройки громкости")
                    frame:
                        xsize setlinesize
                        ysize 5
                        style_prefix "textline"
                    null height setnull1

                    vbox:

                        hbox:
                            frame:
                                style_prefix "frametextred"
                                xsize 220
                                yalign 0.5
                                text _("Музыка") xalign 0.5
                            null width 20 height 80
                            hbox:
                                bar value Preference("music volume") xsize setbaresize xalign 0.0

                        null height 30
                        hbox:
                            frame:
                                style_prefix "frametextred"
                                xsize 220
                                yalign 0.5
                                text _("Звуки") xalign 0.5
                            null width 20 height 80
                            hbox:
                                bar value Preference("sound volume") xsize setbaresize xalign 0.0 changed play_sound_check()

                        null height 30
                        hbox:
                            frame:
                                style_prefix "frametextred"
                                xsize 220
                                yalign 0.5
                                text _("Текст") xalign 0.5
                            null width 20 height 80
                            hbox:
                                bar value Preference("mixer text volume") xsize setbaresize xalign 0.0

                        if dmt == 2:
                            null height 30
                            hbox:
                                frame:
                                    style_prefix "frametextred"
                                    xsize 220
                                    yalign 0.5
                                    text _("Голос") xalign 0.5
                                null width 20 height 80
                                hbox:
                                    bar value Preference("voice volume") xsize setxsize-400 xalign 0.0

                        null height 20
                        hbox:
                            ysize 70
                            xfill True
                            button:
                                xalign 0.0 
                                text _("{image=set_all_mute} Отключить всё")
                                if not persistent.allmute:
                                    activate_sound "audio/ui_sfx/touch.flac"
                                    action [SetField(persistent, 'allmute', True), Preference("all mute", "toggle")]
                                else:
                                    activate_sound "audio/ui_sfx/touch.flac"
                                    action [SetField(persistent, 'allmute', False), Preference("all mute", "toggle")]
                            vbox:
                                xsize 500
                                hbox:
                                    null height 100
                                    imagebutton:
                                        anchor (0.5, 0.5) ypos btsetypos1 xpos 650
                                        idle "btn reset"
                                        hover "hover reset"
                                        activate_sound "audio/ui_sfx/touch.flac"
                                        action [Preference("mixer text volume", 0.7), Preference("music volume", config.default_music_volume), Preference("sound volume", config.default_sfx_volume), Preference("voice volume", config.default_voice_volume)]
                            
                    null height setnull4
                    text _("{image=icontext1} {=settitle}Диалоги и пропуск")
                    frame:
                        xsize setlinesize
                        ysize 5
                        style_prefix "textline"
                    
                    null height setnull2
                    vbox:

                        hbox:
                            frame:
                                style_prefix "frametextred"
                                xsize frsetypos1
                                yalign 0.5
                                text _("Скорость текста") xalign 0.5
                            null width 20 height 100
                            hbox:
                                bar value Preference("text speed") xsize setbaresize2 xalign 0.0 ypos 10
                            null width setnull3
                            imagebutton:
                                anchor (0.5, 0.5) ypos 50 xpos 130
                                idle "btn reset"
                                hover "hover reset"
                                activate_sound "audio/ui_sfx/touch.flac"
                                action [Preference("text speed", 30)]

                        null height 10
                        hbox:
                            frame:
                                style_prefix "frametextred"
                                xsize frsetypos1
                                yalign 0.5
                                text _("Скорость авточтения") xalign 0.5
                            null width 20 height 100
                            hbox:
                                bar value Preference("auto-forward time") xsize setbaresize2 xalign 0.0 ypos 10
                            null width setnull3
                            imagebutton:
                                anchor (0.5, 0.5) ypos 50 xpos 130
                                idle "btn reset"
                                hover "hover reset"
                                activate_sound "audio/ui_sfx/touch.flac"
                                action [Preference("auto-forward time", 15)]

                    null height 30
                    hbox:
                        spacing spset
                        frame:
                            style_prefix "frametextred"
                            text _("Пропуск")
                        if not renpy.variant("small"):
                            null width 10
                        button:
                            text _("{image=set_skip0} Всего текста")
                            if not persistent.skip0:
                                activate_sound "audio/ui_sfx/touch.flac"
                                action [SetField(persistent, 'skip0', True), Preference("skip", "toggle")]
                            else:
                                activate_sound "audio/ui_sfx/touch.flac"
                                action [SetField(persistent, 'skip0', False), Preference("skip", "toggle")]
                        button:
                            text _("{image=set_skip1} После выборов")
                            if not persistent.skip1:
                                activate_sound "audio/ui_sfx/touch.flac"
                                action [SetField(persistent, 'skip1', True), Preference("after choices", "toggle")]
                            else:
                                activate_sound "audio/ui_sfx/touch.flac"
                                action [SetField(persistent, 'skip1', False), Preference("after choices", "toggle")]
                        button:
                            text _("{image=set_skip2} Переходов")
                            if not persistent.skip2:
                                activate_sound "audio/ui_sfx/touch.flac"
                                action [SetField(persistent, 'skip2', True), InvertSelected(Preference("transitions", "toggle"))]
                            else:
                                activate_sound "audio/ui_sfx/touch.flac"
                                action [SetField(persistent, 'skip2', False), InvertSelected(Preference("transitions", "toggle"))]

                    null height setnull4
                    text _("{image=icontext1} {=settitle}Прочее")
                    frame:
                        xsize setlinesize
                        ysize 5
                        style_prefix "textline"
                    null height 30
                    button:
                        text _("{image=set_debug} Режим откладки")
                        if persistent.debugmode == 0:
                            activate_sound "audio/ui_sfx/touch.flac"
                            action Show("debugtrue")
                            #action [SetField(persistent, 'debugmode', True)]
                        else:
                            activate_sound "audio/ui_sfx/touch.flac"
                            action [SetVariable("setpername", "debugmode"), SetVariable("setperval", 0), Show("reload")]
                            #action [SetField(persistent, 'debugmode', False)]

                    null height 50
            
            vbar value YScrollValue("st")









image bt unsel:
    "bt set_unsel"
    zoom btsetsize

image bt sel:
    "bt set_sel"
    zoom btsetsize

image set_debug = ConditionSwitch (
    "persistent.debugmode > 0", "bt sel",
    "True", "bt unsel" 
)

image set_screenfull = ConditionSwitch (
    "preferences.fullscreen == True", "bt sel",
    "True", "bt unsel" 
)

image set_screenwin = ConditionSwitch (
    "preferences.fullscreen == False", "bt sel",
    "True", "bt unsel" 
)

image set_skip0 = ConditionSwitch (
    "persistent.skip0 == True", "bt sel",
    "True", "bt unsel" 
)

image set_skip1 = ConditionSwitch (
    "persistent.skip1 == True", "bt sel",
    "True", "bt unsel" 
)

image set_skip2 = ConditionSwitch (
    "persistent.skip2 == True", "bt sel",
    "True", "bt unsel" 
)

image set_all_mute = ConditionSwitch (
    "persistent.allmute == True", "bt sel",
    "True", "bt unsel" 
)

default persistent.allmute = False

default persistent.skip0 = False
default persistent.skip1 = False
default persistent.skip2 = False

image set_low0 = ConditionSwitch (
    "persistent.low == 0", "bt sel",
    "True", "bt unsel" 
)

image set_low1 = ConditionSwitch (
    "persistent.low == 1", "bt sel",
    "True", "bt unsel" 
)

image set_low2 = ConditionSwitch (
    "persistent.low == 2", "bt sel",
    "True", "bt unsel" 
)

define btsetsize = 0.4 if renpy.variant("small") else 0.3

style textline_frame:
    background Frame("text line", textline_borders, tile=True)
    padding textline_borders.padding

style frametextred_frame is empty

style frametextred_frame:
    background Frame("frtextred", frtext2_borders, tile=True)
    padding frtext2_borders.padding

style frametextred_text:
    variant "small"
    size 40

define frtext2_borders = Borders (70, 0, 70, 5) if renpy.variant("small") else Borders (50, 1, 50, 5)

image frtextred:
    "frametextred"
    zoom frtextsize

image icontext1:
    "iconknife"
    zoom icontextsize yalign 1.1

style settitle:
    font "gt"
    color "#980002"

define icontextsize = 0.8 if renpy.variant("small") else 0.5

define textline_borders = Borders(0, 0, 0, 0)

define setclosepose = 770 if renpy.variant("small") else 610

image btn change:
    "bt change"
    btn

image hover change:
    "bt change"
    bt_hover

image btn reset:
    "bt reset"
    btn

image hover reset:
    "bt reset"
    bt_hover




## Экран разговора #############################################################
##
## Экран разговора используется для показа диалога игроку. Он использует два
## параметра — who и what — что, соответственно, имя говорящего персонажа и
## показываемый текст. (Параметр who может быть None, если имя не задано.)
##
## Этот экран должен создать текст с id "what", чтобы Ren'Py могла показать
## текст. Здесь также можно создать наложения с id "who" и id "window", чтобы
## применить к ним настройки стиля.
##
## https://www.renpy.org/doc/html/screen_special.html#say


screen say(who, what):
    zorder 60
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

transform nameshow:

    on show:
        alpha 0.0
        linear 0.3 alpha 1.0
    on hide:
        linear 0.3 alpha 0.0

## Делает namebox доступным для стилизации через объект Character.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default:
    color '#000000'
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Экран ввода #################################################################
##
## Этот экран используется, чтобы показывать renpy.input. Это параметр запроса,
## используемый для того, чтобы дать игроку ввести в него текст.
##
## Этот экран должен создать наложение ввода с id "input", чтобы принять
## различные вводимые параметры.
##
## https://www.renpy.org/doc/html/screen_special.html#input


screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

screen inputtoo():

    if persistent.low != 2:
        timer 0.01 action Play("ui", "audio/ui_sfx/show.flac", relative_volume=vol_show)

    add "gui/overlay/confirm.png" alpha 0.7

    frame at showframe(0.05):
        style_prefix "styleframe"
        xalign 0.5
        padding (frpadx, frpady)
        if renpy.variant("touch"):
            yalign 0.05
        else:
            yalign 0.5

        vbox:
            xalign 0.5
            yalign 0.5
            text _("Введите новое имя:")
            null height 10

            input default "":
                length(12)
                allow(allow_text_input)
                value VariableInputValue("thisname")

            null height nullsp

            hbox:
                ysize framey
                xalign 0.5
                vbox:
                    xsize twobt
                    imagebutton:
                        ycenter ycen xcenter twobtx
                        idle "btn cancel"
                        hover "hover cancel"
                        keysym('K_ESCAPE')
                        activate_sound "audio/ui_sfx/close.flac"
                        action [Hide("inputtoo"), Function(renpy.restart_interaction)]
                null width 10
                vbox:
                    xsize twobt           
                    imagebutton:
                        ycenter ycen xcenter twobtx
                        idle "btn okred"
                        hover "hover okred"
                        keysym('K_RETURN')
                        activate_sound "audio/ui_sfx/touch.flac"
                        action [SetField(persistent, "name", thisname.strip()), Hide("inputtoo"), Show('NewName'), Function(renpy.restart_interaction)]

image btn okred:
    "bt okred"
    btn

image hover okred:
    "bt okred"
    bt_hover

image btn cancel:
    "bt cancel"
    btn

image hover cancel:
    "bt cancel"
    bt_hover

screen NewName():

    if persistent.low != 2:
        timer 0.01 action Play("ui", "audio/ui_sfx/show.flac", relative_volume=vol_show)

    add "gui/overlay/confirm.png" alpha 0.7

    modal True
    frame at showframe(0.1):
        style_prefix "styleframe"
        xalign 0.5
        padding (frpadx, frpady)
        yalign 0.5

        vbox:
            xalign 0.5
            yalign 0.5
            text _("Новое имя вступит в силу в новой игре.") xalign 0.5
            text _("Старые сохранения не изменились.") xalign 0.5
        
            null height nullbt
            hbox:              
                ysize framey
                xalign 0.5
                imagebutton:
                    ycenter ycen
                    idle "btn ok"
                    hover "hover ok"
                    keysym('K_RETURN')
                    activate_sound "audio/ui_sfx/close.flac"
                    action Hide("NewName") xalign 0.5



screen inputstart():

    if persistent.low != 2:
        timer 0.01 action Play("ui", "audio/ui_sfx/show.flac", relative_volume=vol_show)

    modal True
    frame at showframe(0):
        style_prefix "styleframe"
        xalign 0.5
        padding (frpadx, frpady)
        if renpy.variant("touch"):
            yalign 0.05
        else:
            yalign 0.5

        vbox:
            spacing 10
            xalign 0.5
            yalign 0.5
            text _("Введите ваше имя:")

            input default "":
                length(12)
                allow(allow_text_input)
                value VariableInputValue("thisname")
        
            null height 10
            hbox:              
                ysize framey
                xalign 0.5
                imagebutton:
                    ycenter ycen
                    idle "btn ok"
                    hover "hover ok"
                    keysym('K_RETURN')
                    activate_sound "audio/ui_sfx/touch.flac"
                    action [SetField(persistent, "name", thisname.strip()), Hide("inputstart"), Return()] xalign 0.5


screen inputcode():

    if persistent.low != 2:
        timer 0.01 action Play("ui", "audio/ui_sfx/show.flac", relative_volume=vol_show)

    modal True
    frame at showframe(0):
        style_prefix "styleframe"
        xalign 0.5
        padding (frpadx, frpady)
        if renpy.variant("touch"):
            yalign 0.05
        else:
            yalign 0.4

        vbox:
            spacing 10
            xalign 0.5
            yalign 0.5
            text _("[nv]")

            input default "":
                length(n)
                allow("1234567890")
                value VariableInputValue("code")
        
            null height 10
            hbox:              
                ysize framey
                xalign 0.5
                imagebutton:
                    ycenter ycen
                    idle "btn ok"
                    hover "hover ok"
                    keysym('K_RETURN')
                    activate_sound "audio/ui_sfx/touch.flac"
                    action [Hide("inputcode"), Return()] xalign 0.5



screen inputrangen():

    if persistent.low != 2:
        timer 0.01 action Play("ui", "audio/ui_sfx/show.flac", relative_volume=vol_show)

    modal True
    frame at showframe(0):
        style_prefix "styleframe"
        xalign 0.5
        padding (frpadx, frpady)
        if renpy.variant("touch"):
            yalign 0.05
        else:
            yalign 0.4

        vbox:
            spacing 10
            xalign 0.5
            yalign 0.5
            text _("Число от [gen_n1] до [gen_n2]:")

            input default "":
                length(1)
                allow(gen_allow)
                value VariableInputValue("gen_value")
        
            null height 10
            hbox:              
                ysize framey
                xalign 0.5
                imagebutton:
                    ycenter ycen
                    idle "btn ok"
                    hover "hover ok"
                    keysym('K_RETURN')
                    activate_sound "audio/ui_sfx/touch.flac"
                    action [Hide("inputrangen"), Return()] xalign 0.5


screen rangen():

    if persistent.low != 2:
        timer 0.01 action Play("ui", "audio/ui_sfx/show.flac", relative_volume=vol_show)

    modal True
    frame at showframe(0.05):
        style_prefix "styleframe"
        xalign 0.5
        padding (frpadx, frpady)
        yalign 0.4

        vbox:
            xalign 0.5
            yalign 0.5
            text _("Сгенерируемое число:")

            text "[gen_tr]" xalign 0.5
        
            null height nullsp
            hbox:              
                ysize framey
                xalign 0.5
                imagebutton:
                    ycenter ycen
                    idle "btn ok"
                    hover "hover ok"
                    keysym('K_RETURN')
                    activate_sound "audio/ui_sfx/touch.flac"
                    action [Hide("rangen"), Return()] xalign 0.5



## Экран выбора ################################################################
##
## Этот экран используется, чтобы показывать внутриигровые выборы,
## представленные оператором menu. Один параметр, вложения, список объектов,
## каждый с заголовком и полями действия.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen timerz():
    timer 0.05 repeat True action If(timerz>0, SetVariable('timerz', timerz-0.05), Jump(marker))
    bar:
        xsize 800
        ysize 50
        xalign 0.5
        ypos ypostimer
        value AnimatedValue (value=timerz, range=time_range, delay=0.1)
        bar_invert True
        left_bar Frame ("gui/bar/left.png", 10,10)
        right_bar Frame ("gui/bar/right.png", 10,10)

define ypostimer = 40 if renpy.variant("small") else 50

# timermenu - время 
# time_range - должно быть равно времени
# marker - переход к лейблу, если игрок не успел выбрать

screen choice(items):
    style_prefix "choice"

    if timerm:
        use timerz

    vbox:
        for i in items:
            textbutton i.caption activate_sound "audio/ui_sfx/tap.ogg" action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

define yposchoice = 370 if renpy.variant("small") else 405

style choice_vbox:
    xalign 0.5
    ypos yposchoice
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


default persistent.tv_rui = False

screen block_scr(flag, t):
    timer t action Hide("block_scr") repeat False
    $ keys_list = ["dismiss", "game_menu", "rollback", "rollforward"]
    if not flag:
        for k in keys_list:
            key k action [[]]




## Экран быстрого меню #########################################################
##
## Быстрое меню показывается внутри игры, чтобы обеспечить лёгкий доступ к
## внеигровым меню.

screen quick_menu():

    ## Гарантирует, что оно появляется поверх других экранов.
    zorder 101

    if quick_menu:

        # hbox:
        #     style_prefix "quick"

        #     xalign 0.5
        #     yalign 1.0

        #     textbutton _("Назад") action Rollback()
        #     textbutton _("Пропуск") action Skip() alternate Skip(fast=True, confirm=True)
        #     textbutton _("Авто") action Preference("auto-forward", "toggle")
        #     textbutton _("Сохранить") action ShowMenu("save")
        #     # textbutton _("Б.Сохр") action QuickSave()
        #     # textbutton _("Б.Загр") action QuickLoad()
        #     textbutton _("Опции") action ShowMenu('preferences')
        #     textbutton _("Меню") action MainMenu()

        imagebutton:
            xalign 0.94 yalign yposgmmenu
            anchor (0.5, 0.5)
            idle "bt game_menu"
            hover "hover game_menu"
            keysym('K_ESCAPE')
            if persistent.in_game_menu:
                activate_sound "audio/ui_sfx/close.flac"
                action [SetField(persistent, 'in_game_menu', False), Hide('gm_menu')]
            else:
                activate_sound "audio/ui_sfx/touch.flac"
                action [SetField(persistent, 'in_game_menu', True), Show('gm_menu')]

        imagebutton:
            xalign 0.94 yalign yposgmmenu+0.13
            anchor (0.5, 0.5)
            idle "bt gm q_save"
            hover "hover gm q_save"
            keysym('K_q')
            activate_sound "audio/ui_sfx/touch.flac"
            action QuickSave()

        if dmt == 2:
            textbutton "Назад" xalign 0.94 yalign yposgmmenu+0.23 anchor (0.5, 0.5) action Rollback()




screen gm_menu():
    zorder 99

    if quick_menu:

        if persistent.low != 2:
            timer 0.01 action Play("ui", "audio/ui_sfx/show.flac", relative_volume=vol_show)

        imagebutton at sidegmmenu(0.85, 0.05):
            anchor (0.5, 0.5)  
            idle "bt gm menu"
            hover "hover gm_menu"
            activate_sound "audio/ui_sfx/touch.flac"
            action MainMenu()

        imagebutton at sidegmmenu(0.76, 0.1):
            idle "bt gm set"
            hover "hover gm set"
            activate_sound "audio/ui_sfx/touch.flac"
            action [SetField(persistent, 'mainmenu', False), Function(renpy.music.stop, channel="text"), ShowMenu("settings")]

        imagebutton at sidegmmenu(0.67, 0.15):
            idle "bt gm save"
            hover "hover gm save"
            activate_sound "audio/ui_sfx/touch.flac"
            action [Function(renpy.music.stop, channel="text"), ShowMenu("save")]

        imagebutton at sidegmmenu(0.58, 0.2):
            idle "bt gm ach"
            hover "hover gm ach"
            activate_sound "audio/ui_sfx/touch.flac"
            action [Function(renpy.music.stop, channel="text"), ShowMenu("achievements")]

        imagebutton at sidegmmenu(0.49, 0.25):
            idle "bt gm auto_unsel"
            hover "hover gm auto_unsel"
            selected_idle "bt gm auto_sel"
            selected_hover "hover gm auto_sel"
            if renpy.get_screen('auto_indicator'):
                activate_sound "audio/ui_sfx/touch.flac"
                action [Preference("auto-forward", "toggle"), Hide('auto_indicator')]
            else:
                activate_sound "audio/ui_sfx/touch.flac"
                action [Preference("auto-forward", "toggle"), Show('auto_indicator')]

        imagebutton at sidegmmenu(0.40, 0.3):
            insensitive "bt gm skip_unact"
            idle "bt gm skip_unsel"
            hover "hover gm skip_unsel"
            selected_idle "bt gm skip_sel"
            selected_hover "hover gm skip_sel"
            activate_sound "audio/ui_sfx/touch.flac"
            action Skip() alternate Skip(fast=True, confirm=True)

            


transform sidegmmenu(xpos, tm):
    choice(persistent.low < 2):
        xalign 0.94 yalign yposgmmenu
        anchor (0.5, 0.5)
        easein tm xalign xpos anchor (0.5, 0.5)
    choice(persistent.low == 2):
        yalign yposgmmenu xalign xpos anchor (0.5, 0.5)

    on hide:
        choice(persistent.low < 2):
            linear tm+0.05 xalign 0.94 anchor (0.5, 0.5)
            alpha 0.0
        choice(persistent.low == 2):
            alpha 0.0      

            
define yposgmmenu = 0.095
        

define bt_gm_hover_size = 0.95 if persistent.low == 0 else 1.0

transform bt_gm_hover:
    ease 0.1 zoom bt_gm_hover_size

image bt game_menu = ConditionSwitch(
    "persistent.in_game_menu == True", "bt game_menu_sel",
    "True", "bt game_menu_unsel"
)

image hover game_menu:
    "bt game_menu"
    bt_gm_hover

image hover gm_menu:
    "bt gm menu"
    bt_gm_hover

image hover gm set:
    "bt gm set"
    bt_gm_hover

image hover gm ach:
    "bt gm ach"
    bt_gm_hover

image hover gm save:
    "bt gm save"
    bt_gm_hover

image hover gm q_save:
    "bt gm q_save"
    bt_gm_hover

image hover gm auto_unsel:
    "bt gm auto_unsel"
    bt_gm_hover

image hover gm auto_sel:
    "bt gm auto_sel"
    bt_gm_hover

image hover gm skip_unsel:
    "bt gm skip_unsel"
    bt_gm_hover

image hover gm skip_sel:
    "bt gm skip_sel"
    bt_gm_hover


## Данный код гарантирует, что экран быстрого меню будет показан в игре в любое
## время, если только игрок не скроет интерфейс.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text


################################################################################
## Экраны Главного и Игрового меню
################################################################################

## Экран навигации #############################################################
##
## Этот экран включает в себя главное и игровое меню, и обеспечивает навигацию к
## другим меню и к началу игры.

screen navigation():

    modal True

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Играть") action ShowMenu("GameStart")

        else:

            textbutton _("Сохранить") action ShowMenu("save")

        textbutton _("Загрузить") action ShowMenu("load")


        textbutton _("Настройки") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("Завершить повтор") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Главное меню") action MainMenu()

        if main_menu:

            textbutton _("Концовки") action ShowMenu("ends_secret")

        textbutton _("Выход") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Экран главного меню #########################################################
##
## Используется, чтобы показать главное меню после запуска игры.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

define mainlbsize = 1.52 if renpy.variant("small") else 1.08
define mainlbpos = 0.45 if renpy.variant("small") else 0.425

screen main_menu():

    modal True
    tag menu
    $ ends = len(all_rui_end_code)

    add "main bg"
    if renpy.variant("small"):
        add "main bg-tex" alpha 0.2 zoom 1.5 xalign 0.5 yalign 0.5
    else:
        add "main bg-tex" alpha 0.2

    if persistent.low == 2:
        add "main_line_low" xalign 0.05 yalign 1.0
    else:
        add "main_line" xalign 0.05 yalign 1.0

    add "main lable" xalign 0.5 yalign mainlbpos alpha 0.8 zoom mainlbsize

    vbox:
        yalign 0.99 xalign 0.02
        style_prefix "main_nofanru"
        text _("Разработчик: {a=https://tapy.me/nofanru}{color=#8893e7}NoFanru{/color}{/a}"):
            outlines [(1, "#000", 0, 0)]
        text _("Отдельная благодарность: Ари, Angrrry Panda"):
            outlines [(1, "#000", 0, 0)]

    vbox:
        yalign 0.99 xalign 0.98
        style_prefix "main_sega"
        text _("Оригинальные авторские права:") xalign 1.0:
            outlines [(1, "#000", 0, 0)]
        if renpy.variant("small"):
            text "SEGA, Colorful Palette," xalign 1.0:
                outlines [(1, "#000", 0, 0)]
            text "Crypton Future Media" xalign 1.0:
                outlines [(1, "#000", 0, 0)]
        else:
            text "SEGA, Colorful Palette, Crypton Future Media":
                outlines [(1, "#000", 0, 0)]

    text _("{size=-5}Версия игры: [config.version]{/size}") yalign 0.01 xalign 0.02:
        outlines [(1, "#000", 0, 0)]

    
    hbox:
        xalign 0.5
        if renpy.variant("small"):
            yalign 0.42
            spacing 40
        else:
            yalign 0.42
            spacing 30

        vbox:
            text "[persistent.rui_ends]/[ends]" xalign 0.5 at dison(0.6, 0.1)
            imagebutton at chrup:
                if persistent.low > 0:
                    idle "main rui"
                else:
                    idle "main rui"
                    hover "hover rui"
                    selected_idle "hover rui"
                    selected_hover "hover rui"
                keysym('K_1')
                activate_sound "audio/ui_sfx/touch.flac"
                action Show("Rui_play")

        # vbox:
        #     text "0/0" xalign 0.5 at dison(0.6, 0.1)
        #     imagebutton at chrdown:
        #         if persistent.low:
        #             idle "chr akito"
        #         else:
        #             idle "main akito"
        #             hover "hover akito"
        #             selected_idle "hover akito"
        #             selected_hover "hover akito"
        #         action Show("soon")

        # vbox:
        #     text "0/0" xalign 0.5 at dison(0.6, 0.1)
        #     imagebutton at chrup:
        #         if persistent.low:
        #             idle "chr tsukasa"
        #         else:
        #             idle "main tsukasa"
        #             hover "hover tsukasa"
        #             selected_idle "hover tsukasa"
        #             selected_hover "hover tsukasa"
        #         action Show("soon")

        # vbox:
        #     text "0/0" xalign 0.5 at dison(0.6, 0.1)
        #     imagebutton at chrdown:
        #         if persistent.low:
        #             idle "chr toya"
        #         else:
        #             idle "main toya"
        #             hover "hover toya"
        #             selected_idle "hover toya"
        #             selected_hover "hover toya"
        #         action Show("soon")

        # vbox:
        #     text "0/0" xalign 0.5 at dison(0.6, 0.1)
        #     imagebutton at chrup:
        #         if persistent.low:
        #             idle "chr kaito"
        #         else:
        #             idle "main kaito"
        #             hover "hover kaito"
        #             selected_idle "hover kaito"
        #             selected_hover "hover kaito"
        #         action Show("soon")

        # vbox:
        #     text ""
        #     imagebutton at chrdown:
        #         idle "main soon"
        #         keysym('K_2')
        #         activate_sound "audio/ui_sfx/touch.flac"
        #         action Show("soon")

    frame at main_select:
        style_prefix "frametext"
        text _("Выберите персонажа") at main_select_text 

    if not renpy.variant("small"):
        add "main logo"

    imagebutton:
        anchor (0.5, 0.5) xpos 1835 ypos 88
        idle "btn more"
        hover "hover more"
        keysym ('K_ESCAPE')
        activate_sound "audio/ui_sfx/touch.flac"
        action [SetField(persistent, 'in_game_menu', False), Show("moremain")]

    if not persistent.update_end:
        timer 0.01 action [SetField(persistent, "update_im", 1), Show('update_info')]


screen update_info():
    modal True
    add "gui/overlay/confirm.png"

    if renpy.variant("small"):
        add "update_im" xalign 0.5 ypos -50 zoom 0.8
    else:
        add "update_im" xalign 0.5 yalign 0.2 zoom 0.6

    if persistent.update_im != 2:
        imagebutton:
            xalign rarrowpos
            yalign 0.4
            idle "up_r_arrow"
            keysym('K_RIGHT')
            action SetField(persistent, "update_im", persistent.update_im+1)

    if persistent.update_im != 1:
        imagebutton:
            xalign lrarrowpos
            yalign 0.4
            idle "up_l_arrow"
            keysym('K_LEFT')
            action SetField(persistent, "update_im", persistent.update_im-1)

    if persistent.update_im == 2:
        imagebutton:
            xcenter updbtrxpos
            ycenter updbtypos
            idle "btn closered"
            hover "hover closered"
            action SetField(persistent, "update_end", True), [Hide("update_info", transition=Dissolve(0.15))]
    else:
        imagebutton:
            xcenter updbtrxpos
            ycenter updbtypos
            idle "btn next"
            hover "hover next"
            action SetField(persistent, "update_im", persistent.update_im+1)
    
    if persistent.update_im == 1:
        imagebutton:
            xcenter updbtlxpos
            ycenter updbtypos
            idle "btn ret_un"
    else:
        imagebutton:
            xcenter updbtlxpos
            ycenter updbtypos
            idle "btn ret"
            hover "hover ret"
            action SetField(persistent, "update_im", persistent.update_im-1)

define updbtypos = 950 if renpy.variant("small") else 820
define updbtrxpos = 1400 if renpy.variant("small") else 1300
define updbtlxpos = 530 if renpy.variant("small") else 630

define rarrowpos = 0.9 if renpy.variant("small") else 0.8
define lrarrowpos = 0.1 if renpy.variant("small") else 0.2

default persistent.update_im = 1

image update_im = ConditionSwitch(
    "persistent.update_im == 1", "update1",
    "True", "update2"
)

define arrowsize = 1.0 if renpy.variant("small") else 0.8

image up_r_arrow:
    "update_rarrow"
    zoom arrowsize
    block:
        easein 0.7 xoffset 20
        easein 0.7 xoffset 0
        repeat

image up_l_arrow:
    "update_larrow"
    zoom arrowsize
    block:
        easein 0.7 xoffset -20
        easein 0.7 xoffset 0
        repeat

image hover next:
    "bt next"
    zoom btmsize
    ease 0.1 zoom btmsizehover 

image btn next:
    "bt next"
    zoom btmsize

image hover ret:
    "bt ret"
    zoom btmsize
    ease 0.1 zoom btmsizehover 

image btn ret:
    "bt ret"
    zoom btmsize

image btn ret_un:
    "bt ret_un"
    zoom btmsize

image hover closered:
    "bt closered"
    zoom btmsize
    ease 0.1 zoom btmsizehover 

image btn closered:
    "bt closered"
    zoom btmsize


style main_sega_text is text:
    size 20

style main_sega_text is text:
    variant "small"
    size 25

style main_nofanru_text is text:
    size 25

style main_nofanru_text is text:
    variant "small"
    size 30

style frametext_text is text:
    variant "small"
    size 40

style frametext_frame is empty

style frametext_frame:
    background Frame("frtext", frtext_borders, tile=True)
    padding frtext_borders.padding

define frtext_borders = Borders(150, 0, 150, 7) if renpy.variant("small") else Borders(140, 0, 155, 5)

image frtext:
    "frametext"
    zoom frtextsize

define frtextsize = 1.0 if renpy.variant("small") else 0.86

define selpos = 0.89 if renpy.variant("small") else 0.78
define selsize = 1.0 if renpy.variant("small") else 1.0

transform main_select:
    choice(persistent.low < 2):
        xalign 0.5 yalign selpos alpha 0.0
        pause 0.4
        ease 0.2 alpha 1.0
    choice(persistent.low == 2):
        xalign 0.5 yalign selpos alpha 1.0

transform main_select_text:
    zoom selsize

    choice(persistent.low == 0):
        block:
            ease 1.5 alpha 0.3
            ease 1.5 alpha 1.0
            repeat
    choice(persistent.low > 0):
        alpha 1.0

transform bt_hover:
    zoom btnsize
    ease 0.1 zoom btnsizehover 

transform btn:
    zoom btnsize

define btnsizehoversmall = 1.2 if persistent.low == 0 else 1.3
define btnsizehovebig = 0.93 if persistent.low == 0 else 1.0

define btmsizehoversmall = 1.35 if persistent.low == 0 else 1.5
define btmsizehovebig = 1.0 if persistent.low == 0 else 1.1

define btnsize = 1.3 if renpy.variant("small") else 1.0
define btnsizehover = btnsizehoversmall if renpy.variant("small") else btnsizehovebig

define btmsize = 1.5 if renpy.variant("small") else 1.1
define btmsizehover = btmsizehoversmall if renpy.variant("small") else btmsizehovebig

# default persistent.morenoti = False

image hover more:
    "bt more"
    zoom btmsize
    ease 0.1 zoom btmsizehover 

image btn more:
    "bt more"
    zoom btmsize

image bt more = ConditionSwitch (
    "persistent.morenoti == True", "bt morenoti",
    "True", "bt morenormal"
)

image bt ends = ConditionSwitch (
    "persistent.morenoti == True", "bt ends_noti",
    "True", "bt ends_normal"
)

image hover exit:
    "bt exit"
    bt_hover

image hover save:
    "bt save"
    bt_hover

image hover about:
    "bt about"
    bt_hover

image hover ends:
    "bt ends"
    bt_hover

image hover set:
    "bt set"
    bt_hover

image hover ach:
    "bt ach"
    bt_hover

image btn ach:
    "bt ach"
    btn

image btn exit:
    "bt exit"
    btn

image btn save:
    "bt save"
    btn

image btn about:
    "bt about"
    btn

image btn ends:
    "bt ends"
    btn

image btn set:
    "bt set"
    btn      

image main logo:
    "logo"
    choice(persistent.low < 2):
        zoom logosize yalign logopos xalign -0.5
        pause 0.2
        ease 0.25 xalign 0.51
        ease 0.05 xalign 0.5
    choice(persistent.low == 2):
        zoom logosize yalign logopos xalign 0.5

define logosize = 0.22 if renpy.variant("small") else 0.2
define logopos = 0.02 if renpy.variant("small") else 0.03

image main kaito:
    "chr kaito"
    chr

image hover kaito:
    "chr kaito"
    chr_hover

image main rui:
    "chr rui"
    chr

image hover rui:
    "chr rui"
    chr_hover

image main akito:
    "chr akito"
    chr

image hover akito:
    "chr akito"
    chr_hover

image main tsukasa:
    "chr tsukasa"
    chr

image hover tsukasa:
    "chr tsukasa"
    chr_hover

image main toya:
    "chr toya"
    chr

image hover toya:
    "chr toya"
    chr_hover

image main soon:
    "chr soon"
    chr

define chrsize = 1.0 if renpy.variant("small") else 0.7

transform chr:
    yoffset poshoverchr zoom chrsize
    ease 0.1 yoffset 0
        
transform chrup:
    choice(persistent.low < 2):
        alpha 0.0 yoffset -200
        pause 0.2
        ease 0.3 alpha 1.0 yoffset 0
    choice(persistent.low == 2):
        alpha 1.0

transform chrdown:
    choice(persistent.low < 2):
        alpha 0.0 yoffset 200
        pause 0.2
        ease 0.3 alpha 1.0 yoffset 0
    choice(persistent.low == 2):
        alpha 1.0

transform chr_hover:
    zoom chrsize
    ease 0.1 yoffset poshoverchr

define poshoverchr = -45 if renpy.variant("small") else -40

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

image line1:
    "pr1"
    zoom 0.85 alpha 0.1+linealpha

image line2:
    "pr2"
    zoom 0.85 alpha linealpha

image line3:
    "pr3"
    zoom 0.85 alpha linealpha

image line4:
    "pr4"
    zoom 0.85 alpha linealpha

image line5:
    "pr5"
    zoom 0.85 alpha linealpha

image line6:
    "pr6"
    zoom 0.85 alpha linealpha

image line7:
    "pr7"
    zoom 0.85 alpha linealpha

image line8:
    "pr8"
    zoom 0.85 alpha linealpha-0.05

define linetime = 15.0
default linealpha = 0.21

image line_all_pr:
    contains:
        "line1"
        xoffset -120 yoffset 140
    contains:
        "line2"
        xoffset -60 yoffset 70
    contains:
        "line1"
        xoffset 0 yoffset 0
    contains:
        "line3"
        xoffset 60 yoffset -70
    contains:
        "line1"
        xoffset 120 yoffset -140
    contains:
        "line4"
        xoffset 180 yoffset -210
    contains:
        "line1"
        xoffset 240 yoffset -280
    contains:
        "line5"
        xoffset 300 yoffset -350
    contains:
        "line1"
        xoffset 360 yoffset -420
    contains:
        "line6"
        xoffset 420 yoffset -490
    contains:
        "line1"
        xoffset 480 yoffset -560
    contains:
        "line7"
        xoffset 540 yoffset -630

image line_all:
    contains:
        "line_all_pr"
        xoffset -720 yoffset 840
        linear linetime xoffset 0 yoffset 0
        repeat
    contains:
        "line_all_pr"
        xoffset 0 yoffset 0
        linear linetime xoffset 720 yoffset -840
        repeat
    contains:
        "line_all_pr"
        xoffset 720 yoffset -840
        linear linetime xoffset 1440 yoffset -1680
        repeat

image line_all_low:
    contains:
        "line_all_pr"
        xoffset -720 yoffset 840
    contains:
        "line_all_pr"
        xoffset 0 yoffset 0
    contains:
        "line_all_pr"
        xoffset 720 yoffset -840

image line_kaito_pr:
    contains:
        "line6"
        xoffset -120 yoffset 140
    contains:
        "line7"
        xoffset -60 yoffset 70
    contains:
        "line1"
        xoffset 0 yoffset 0
    contains:
        "line8"
        xoffset 60 yoffset -70
    contains:
        "line6"
        xoffset 120 yoffset -140
    contains:
        "line7"
        xoffset 180 yoffset -210
    contains:
        "line1"
        xoffset 240 yoffset -280
    contains:
        "line8"
        xoffset 300 yoffset -350
    contains:
        "line6"
        xoffset 360 yoffset -420
    contains:
        "line7"
        xoffset 420 yoffset -490
    contains:
        "line1"
        xoffset 480 yoffset -560
    contains:
        "line8"
        xoffset 540 yoffset -630

image line_none_pr:
    contains:
        "line7"
        xoffset -120 yoffset 140
    contains:
        "line1"
        xoffset -60 yoffset 70
    contains:
        "line8"
        xoffset 0 yoffset 0
    contains:
        "line1"
        xoffset 60 yoffset -70
    contains:
        "line7"
        xoffset 120 yoffset -140
    contains:
        "line1"
        xoffset 180 yoffset -210
    contains:
        "line8"
        xoffset 240 yoffset -280
    contains:
        "line1"
        xoffset 300 yoffset -350
    contains:
        "line7"
        xoffset 360 yoffset -420
    contains:
        "line1"
        xoffset 420 yoffset -490
    contains:
        "line8"
        xoffset 480 yoffset -560
    contains:
        "line1"
        xoffset 540 yoffset -630

image line_none:
    contains:
        "line_none_pr"
        xoffset -720 yoffset 840
        linear linetime xoffset 0 yoffset 0
        repeat
    contains:
        "line_none_pr"
        xoffset 0 yoffset 0
        linear linetime xoffset 720 yoffset -840
        repeat
    contains:
        "line_none_pr"
        xoffset 720 yoffset -840
        linear linetime xoffset 1440 yoffset -1680
        repeat

image line_none_low:
    contains:
        "line_none_pr"
        xoffset -720 yoffset 840
    contains:
        "line_none_pr"
        xoffset 0 yoffset 0
    contains:
        "line_none_pr"
        xoffset 720 yoffset -840

image line_kaito:
    contains:
        "line_kaito_pr"
        xoffset -720 yoffset 840
        linear linetime xoffset 0 yoffset 0
        repeat
    contains:
        "line_kaito_pr"
        xoffset 0 yoffset 0
        linear linetime xoffset 720 yoffset -840
        repeat
    contains:
        "line_kaito_pr"
        xoffset 720 yoffset -840
        linear linetime xoffset 1440 yoffset -1680
        repeat

image line_kaito_low:
    contains:
        "line_kaito_pr"
        xoffset -720 yoffset 840
    contains:
        "line_kaito_pr"
        xoffset 0 yoffset 0
    contains:
        "line_kaito_pr"
        xoffset 720 yoffset -840

image lines:
    contains:
        "line_kaito"
        xoffset -800 yoffset 1000 
    contains:
        "line_all"
        xoffset -400 yoffset 1000
    contains:
        "line_none"
        xoffset 0 yoffset 1000
    contains:
        "line_all"
        xoffset 400 yoffset 1000
    contains:
        "line_none"
        xoffset 800 yoffset 1000
    contains:
        "line_all"
        xoffset 1200 yoffset 1000
    contains:
        "line_kaito"
        xoffset 1600 yoffset 1000

image lines_low:
    contains:
        "line_kaito_low"
        xoffset -800 yoffset 1000 
    contains:
        "line_all_low"
        xoffset -400 yoffset 1000
    contains:
        "line_none_low"
        xoffset 0 yoffset 1000
    contains:
        "line_all_low"
        xoffset 400 yoffset 1000
    contains:
        "line_none_low"
        xoffset 800 yoffset 1000
    contains:
        "line_all_low"
        xoffset 1200 yoffset 1000
    contains:
        "line_kaito_low"
        xoffset 1600 yoffset 1000

image main_line:
    "lines"
    xoffset 100    

image main_line_low:
    "lines_low"
    xoffset 100   

## Экран игрового меню #########################################################
##
## Всё это показывает основную, обобщённую структуру экрана игрового меню. Он
## вызывается с экраном заголовка и показывает фон, заголовок и навигацию.
##
## Параметр scroll может быть None, или "viewport", или "vpgrid", когда этот
## экран предназначается для использования с более чем одним дочерним экраном,
## включённым в него.

screen game_menu(title, scroll=None, yinitial=0.0):

    modal True

    if persistent.low != 2:
        timer 0.01 action Play("ui", "audio/ui_sfx/show.flac", relative_volume=vol_show)

    add "main bg"
    if renpy.variant("small") and persistent.low != 2:
        add "main bg-tex" alpha 0.2 zoom 1.5 xalign 0.5 yalign 0.5
    elif persistent.low != 2:
        add "main bg-tex" alpha 0.2

    if persistent.low == 0:
        add "main_line" xalign 0.05 yalign 1.0

    add "menuline" anchor (0.5, 0.5) xpos poslinemenu ypos 88
    text "{image=textmenueim} [title]" anchor (0.0, 0.5) xpos xpostextline ypos ypostextline size textlinesize
    imagebutton:
        anchor (0.5, 0.5) xpos posreturn ypos 88
        idle "btn_return"
        hover "hover_return"
        keysym ('K_ESCAPE')
        activate_sound "audio/ui_sfx/close.flac"
        action Return()


    if not persistent.in_game_menu:

        imagebutton:
            anchor (0.5, 0.5) xpos 1835 ypos 88
            idle "btn more"
            hover "hover more"
            keysym ('K_SPACE')
            activate_sound "audio/ui_sfx/touch.flac"
            action Show("moremain")

    # style_prefix "game_menu"

    # if main_menu:
    #     add gui.main_menu_background
    # else:
    #     add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        # hbox:

        #     ## Резервирует пространство для навигации.
        #     # frame:
        #     #     style "game_menu_navigation_frame"

        #     frame:
        #         style "game_menu_content_frame"

        if scroll == "viewport":

            viewport:
                yinitial yinitial
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                side_yfill True

                vbox:
                    transclude

        elif scroll == "vpgrid":

            vpgrid:
                cols 1
                yinitial yinitial

                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                side_yfill True

                transclude

        else:

            transclude

    # use navigation

    # textbutton _("Вернуться"):
    #     style "return_button"

    #     action Return()

    # label title

    # if main_menu:
    #     key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "nothing"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## Экран Об игре ###############################################################
##
## Этот экран показывает авторскую информацию об игре и Ren'Py.
##
## В этом экране нет ничего особенного, и он служит только примером того, каким
## можно сделать свой экран.

# screen about():

#     modal True

#     tag menu

#     ## Этот оператор включает игровое меню внутрь этого экрана. Дочерний vbox
#     ## включён в порт просмотра внутри экрана игрового меню.
#     use game_menu(_("Об игре"), scroll="viewport"):

#         style_prefix "about"

#         vbox:

#             label "[config.name!t]"
#             text _("Версия: [config.version!t]\n")

#             ## gui.about обычно установлено в options.rpy.
#             if gui.about:
#                 text "[gui.about!t]\n"


# style about_label is gui_label
# style about_label_text is gui_label_text
# style about_text is gui_text

# style about_label_text:
#     size gui.label_text_size


## Экраны загрузки и сохранения ################################################
##
## Эти экраны ответственны за возможность сохранять и загружать игру. Так
## как они почти одинаковые, оба реализованы по правилам третьего экрана —
## file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save 

# screen save():

#     modal True

#     tag menu

#     use file_slots(_("Сохранить"))


# screen load():

#     modal True

#     tag menu

#     use file_slots(_("Загрузить"))


# screen file_slots(title):

#     default page_name_value = FilePageNameInputValue(pattern=_("{} страница"), auto=_("Автосохранения"), quick=_("Быстрые сохранения"))

#     use game_menu(title):

#         fixed:

#             ## Это гарантирует, что ввод будет принимать enter перед остальными
#             ## кнопками.
#             order_reverse True

#             ## Номер страницы, который может быть изменён посредством клика на
#             ## кнопку.
#             button:
#                 style "page_label"

#                 key_events True
#                 xalign 0.5
#                 action page_name_value.Toggle()

#                 input:
#                     style "page_label_text"
#                     value page_name_value

#             ## Таблица слотов.
#             grid gui.file_slot_cols gui.file_slot_rows:
#                 style_prefix "slot"

#                 xalign 0.5
#                 yalign 0.5

#                 spacing gui.slot_spacing

#                 for i in range(gui.file_slot_cols * gui.file_slot_rows):

#                     $ slot = i + 1

#                     button:
#                         action FileAction(slot)

#                         has vbox

#                         add FileScreenshot(slot) xalign 0.5

#                         text FileTime(slot, format=_("{#file_time}%A, %d %B %Y, %H:%M"), empty=_("Пустой слот")):
#                             style "slot_time_text"

#                         text FileSaveName(slot):
#                             style "slot_name_text"

#                         key "save_delete" action FileDelete(slot)

#             ## Кнопки для доступа к другим страницам.
#             hbox:
#                 style_prefix "page"

#                 xalign 0.5
#                 yalign 1.0

#                 spacing gui.page_spacing

#                 textbutton _("<") action FilePagePrevious()

#                 if config.has_autosave:
#                     textbutton _("{#auto_page}А") action FilePage("auto")

#                 if config.has_quicksave:
#                     textbutton _("{#quick_page}Б") action FilePage("quick")

#                 ## range(1, 10) задаёт диапазон значений от 1 до 9.
#                 for page in range(1, 10):
#                     textbutton "[page]" action FilePage(page)

#                 textbutton _(">") action FilePageNext()


# style page_label is gui_label
# style page_label_text is gui_label_text
# style page_button is gui_button
# style page_button_text is gui_button_text

# style slot_button is gui_button
# style slot_button_text is gui_button_text
# style slot_time_text is slot_button_text
# style slot_name_text is slot_button_text

# style page_label:
#     xpadding 75
#     ypadding 5

# style page_label_text:
#     text_align 0.5
#     layout "subtitle"
#     hover_color gui.hover_color

# style page_button:
#     properties gui.button_properties("page_button")

# style page_button_text:
#     properties gui.button_text_properties("page_button")

# style slot_button:
#     properties gui.button_properties("slot_button")

# style slot_button_text:
#     properties gui.button_text_properties("slot_button")


## Экран настроек ##############################################################
##
## Экран настроек позволяет игроку настраивать игру под себя.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    modal True

    tag menu

    use game_menu(_("Настройки"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Режим экрана")
                        textbutton _("Оконный") action Preference("display", "window")
                        textbutton _("Полный") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Пропуск")
                    textbutton _("Всего текста") action Preference("skip", "toggle")
                    textbutton _("После выборов") action Preference("after choices", "toggle")
                    textbutton _("Переходов") action InvertSelected(Preference("transitions", "toggle"))

                #vbox:
                    #style_prefix "check"
                    #label _("Галерея концовок")
                    #textbutton _("Изображения") action SetField(persistent, "ends_spisok", False)
                    #textbutton _("Список") action SetField(persistent, "ends_spisok", True)

                #vbox:
                    #style_prefix "radio"
                    #label _("Стиль рисовки")
                    #textbutton _("Оригинал") action [SetField(persistent, "styleart", False), Show("reload")]
                    #textbutton _("Арты") action [SetField(persistent, "styleart", True), Show("reload")]

                #vbox:
                    #style_prefix "radio"
                    #label _("Язык")
                    #textbutton _("Русский") action Language(None)
                    #textbutton _("English") action Language("english")

                ## Дополнительные vbox'ы типа "radio_pref" или "check_pref"
                ## могут быть добавлены сюда для добавления новых настроек.

            null height (4 * gui.pref_spacing)

            vbox:
                text _("{color=#980002}Имя персонажа:{/color}")
                textbutton ([persistent.name]) action Show ("inputtoo")


            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Скорость текста")

                    bar value Preference("text speed")

                    label _("Скорость авточтения")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Громкость музыки")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Громкость звуков")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Тест") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Громкость голоса")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Тест") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Без звука"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## Экран истории ###############################################################
##
## Этот экран показывает игроку историю диалогов. Хотя в этом экране нет ничего
## особенного, он имеет доступ к истории диалогов, хранимом в _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    modal True

    tag menu

    ## Избегайте предсказывания этого экрана, так как он может быть очень
    ## массивным.
    predict False

    use game_menu(_("История"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## Это всё правильно уравняет, если history_height будет
                ## установлен на None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Берёт цвет из who параметра персонажа, если он
                        ## установлен.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("История диалогов пуста.")


## Это определяет, какие теги могут отображаться на экране истории.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Экран помощи ################################################################
##
## Экран, дающий информацию о клавишах управления. Он использует другие экраны
## (keyboard_help, mouse_help, и gamepad_help), чтобы показывать актуальную
## помощь.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Помощь"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Клавиатура") action SetScreenVariable("device", "keyboard")
                textbutton _("Мышь") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Геймпад") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Прохождение диалогов, активация интерфейса.")

    hbox:
        label _("Пробел")
        text _("Прохождение диалогов без возможности делать выбор.")

    hbox:
        label _("Стрелки")
        text _("Навигация по интерфейсу.")

    hbox:
        label _("Esc")
        text _("Вход в игровое меню.")

    hbox:
        label _("Ctrl")
        text _("Пропускает диалоги, пока зажат.")

    hbox:
        label _("Tab")
        text _("Включает режим пропуска.")

    hbox:
        label _("Page Up")
        text _("Откат назад по сюжету игры.")

    hbox:
        label _("Page Down")
        text _("Откатывает предыдущее действие вперёд.")

    hbox:
        label "H"
        text _("Скрывает интерфейс пользователя.")

    hbox:
        label "S"
        text _("Делает снимок экрана.")

    hbox:
        label "V"
        text _("Включает поддерживаемый {a=https://www.renpy.org/l/voicing}синтезатор речи{/a}.")

    hbox:
        label "Shift+A"
        text _("Открывает меню специальных возможностей.")


screen mouse_help():

    hbox:
        label _("Левый клик")
        text _("Прохождение диалогов, активация интерфейса.")

    hbox:
        label _("Клик колёсиком")
        text _("Скрывает интерфейс пользователя.")

    hbox:
        label _("Правый клик")
        text _("Вход в игровое меню.")

    hbox:
        label _("Колёсико вверх\nКлик на сторону отката")
        text _("Откат назад по сюжету игры.")

    hbox:
        label _("Колёсико вниз")
        text _("Откатывает предыдущее действие вперёд.")


screen gamepad_help():

    hbox:
        label _("Правый триггер\nA/Нижняя кнопка")
        text _("Прохождение диалогов, активация интерфейса.")

    hbox:
        label _("Левый Триггер\nЛевый Бампер")
        text _("Откат назад по сюжету игры.")

    hbox:
        label _("Правый бампер")
        text _("Откатывает предыдущее действие вперёд.")


    hbox:
        label _("Крестовина, Стики")
        text _("Навигация по интерфейсу.")

    hbox:
        label _("Start, Guide")
        text _("Вход в игровое меню.")

    hbox:
        label _("Y/Верхняя кнопка")
        text _("Скрывает интерфейс пользователя.")

    textbutton _("Калибровка") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Дополнительные экраны
################################################################################


## Экран подтверждения #########################################################
##
## Экран подтверждения вызывается, когда Ren'Py хочет спросить у игрока вопрос
## Да или Нет.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Гарантирует, что другие экраны будут недоступны, пока показан этот экран.
    modal True

    if persistent.low != 2:
        timer 0.01 action Play("ui", "audio/ui_sfx/show.flac", relative_volume=vol_show)

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame at showframe(0.05):

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                ysize framey
                xalign 0.5
                vbox:
                    xsize twobt
                    imagebutton:
                        ycenter ycen xcenter twobtx
                        idle "btn no"
                        hover "hover no"
                        keysym('K_ESCAPE')
                        activate_sound "audio/ui_sfx/close.flac"
                        action no_action
                null width 10
                vbox:
                    xsize twobt           
                    imagebutton:
                        ycenter ycen xcenter twobtx
                        idle "btn yes"
                        hover "hover yes"
                        keysym('K_RETURN')
                        activate_sound "audio/ui_sfx/choice.flac"
                        action yes_action    

    ## Правый клик и esc, как ответ "Нет".
    key "game_menu" activate_sound "audio/ui_sfx/close.flac" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    color "#000"
    font "lal"
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Экран индикатора пропуска ###################################################
##
## Экран индикатора пропуска появляется для того, чтобы показать, что идёт
## пропуск.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:
        yalign 0.97
        xalign xposskip

        hbox:
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "{font=lal} SKIP{/font}"

define xposskip = 0.995 if renpy.variant("small") else 0.95

screen auto_indicator():

    zorder 99
    style_prefix "skip"

    frame:
        yalign 0.97
        xalign xposskip

        hbox:
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "{font=lal} AUTO{/font}"

## Эта трансформация используется, чтобы мигать стрелками одна за другой.
transform delayed_blink(delay, cycle):
    alpha 0.0

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.0
        pause .2
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size 30

style skip_triangle:
    ## Нам надо использовать шрифт, имеющий в себе символ U+25B8 (стрелку выше).
    font "DejaVuSans.ttf"


## Экран уведомлений ###########################################################
##
## Экран уведомлений используется, чтобы показать игроку оповещение. (Например,
## когда игра автосохранилась, или был сделан скриншот)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 99
    style_prefix "notify"

    frame at notify_appear:
        xalign 0.03
        yalign 0.05
        ysize 80
        #xsize 500
        hbox:
            yalign 0.5 xalign 0.0
            text "{image=noti_small}{size=+13}{color=#000} [message!tq]{/color}{/size}"
            timer 0.01 action Play("ui", "audio/ui_sfx/show.flac", relative_volume=vol_show+0.2)

    timer 3.25 action Hide('notify')

image noti_small:
    "noti"
    zoom 0.65 ypos 17

transform notify_appear:
    on show:
        xalign -1.0 alpha 1.0
        easein .25 xalign 0.04
    on hide:
        linear .3 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    # ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Экран NVL ###################################################################
##
## Этот экран используется в диалогах и меню режима NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Показывает диалог или в vpgrid, или в vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Это контролирует максимальное число строк NVL, могущих показываться за раз.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Мобильные варианты
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Раз мышь может не использоваться, мы заменили быстрое меню версией,
## использующей меньше кнопок, но больших по размеру, чтобы их было легче
## касаться.
# screen quick_menu():
#     variant "touch"

#     zorder 100

#     if quick_menu:

#         hbox:
#             style_prefix "quick"

#             xalign 0.5
#             yalign 1.0

#             textbutton _("Назад") action Rollback()
#             textbutton _("Пропуск") action Skip() alternate Skip(fast=True, confirm=True)
#             textbutton _("Авто") action Preference("auto-forward", "toggle")
#             textbutton _("Сохранить") action QuickSave()
#             textbutton _("Меню") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style namebox:
    variant "small"
    background "gui/phone/namebox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

# style main_menu_frame:
#     variant "small"
#     background "gui/phone/overlay/main_menu.png"

# style game_menu_outer_frame:
#     variant "small"
#     background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

# style bar:
#     variant "small"
#     ysize gui.bar_size
#     left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
#     right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

# style vbar:
#     variant "small"
#     xsize gui.bar_size
#     top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
#     bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

# style scrollbar:
#     variant "small"
#     ysize gui.scrollbar_size
#     base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
#     thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

# style vscrollbar:
#     variant "small"
#     unscrollable "hide"
#     xsize gui.scrollbar_size
#     base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
#     thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

# style slider:
#     variant "small"
#     ysize gui.slider_size
#     base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
#     thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

# style vslider:
#     variant "small"
#     xsize gui.slider_size
#     base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
#     thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

# style slider_vbox:
#     variant "small"
#     xsize None

# style slider_slider:
#     variant "small"
#     xsize 900
