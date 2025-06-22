define fast_start = False # True if dmt == 2 else False

default persistent.chance_flo = 100

label splashscreen:

    scene black

    show screen loading

    $ config.overlay_functions.append(game_end)

    # $ persistent.kaito = []
    # $ persistent.rui_end = []
    # $ persistent.secret_end = []
    # $ persistent.coins = 0
    # $ persistent.ach = ach_ru
    # $ persistent.ach_code = ach_code_def
    # $ persistent.done_ach = []
    # $ persistent.crystal

    # $ persistent.main_ach = False
    # $ persistent.all_ach_pct = 0
    # $ persistent.ach[1][4] = False
    # $ n_list = persistent.done_ach
    # $ n_list.pop(1)

    $ scresize()
    if not renpy.mobile:
        $ config.overlay_functions.append(scresize)

    # show screen scrover

    # $ renpy.show_screen('scrover', _layer='forever', _zorder=9998)
    
    # if persistent.debugmode > 0:
    #     $ renpy.show_screen('debugscreen', _layer='forever', _zorder=9999)
        # show screen debugscreen(_layer='master', _transient=False)

    $ noti_more_or_not()
    $ config.overlay_functions.append(noti_more_or_not)

    $ persistent.petlya = 0
    $ persistent.rui_ends = len(persistent.rui_ends_list_per)
    $ persistent.secret_ends = len(persistent.secret_ends_list_per)
    $ persistent.ends_spisok = True

    if 'rui_bum' in persistent.rui_ends_list_per:
        $ x_list = persistent.rui_ends_list_per
        $ x = x_list.index('rui_bum')
        $ persistent.rui_ends_list_per[x] = 'bum'

    $ kx = len(persistent.kaito)

    if "show" in persistent.kaito:
        $ kx -= 1

    if kx > 1:
        $ kaitoim = True

    if persistent.rui_ends > 0:

        if persistent.last_end == "null":
            $ persistent.last_end = persistent.rui_ends_list_per[0]

        $ n = persistent.last_end

        if n == "orgia":
            $ kaitoim = True  

        $ s1 = ["tsu_die", "tsu_bum", "tsu_pain", "orgia"]
        $ s2 = ["ebi", "molchun_ebka", "rui_dog", "minet", "the_best", "anal"]
        $ s3 = ["ne_ebi", "iznos", "zastavlal", "izmena", "podval"]
        $ s4 = ["bum", "ne_molchi", "ubeysa", "turma", "bum_bum", "die", "suid", "the_end"]
        $ s5 = ["yaderka", "rui_ps", "happy", "home"]

        if n in s1:
            $ startim = 1

        elif n in s2:
            $ startim = 2

        elif n in s3:
            $ startim = 3

        elif n in s4:
            $ startim = 4

        elif n in s5:
            $ startim = 5

        elif n == "secret":
            $ startim = 0

    else:
        $ startim = 0

    hide screen loading

    if fast_start:
        pause 0.3
        return

    if renpy.variant("android"):
        #if renpy.request_permission("android.permission.WRITE_EXTERNAL_STORAGE") and renpy.request_permission("android.permission.READ_EXTERNAL_STORAGE"):
        if renpy.request_permission("android.permission.MANAGE_EXTERNAL_STORAGE"):
            pause 0.01
        else:
            show screen permission
            pause 0.5

    pause 0.5

    show nofanru_logo1 at truecenter with dissolve

    pause 0.3

    if persistent.chance_flo < 10:
        $ persistent.chance_flo = 10

    $ chance_f = random.randint(1, persistent.chance_flo)
    $ chance_k = random.randint(1, 4)

    if chance_f == 1:
        play sound [ "<silence .04>", "audio/start/nofanru_flower.wav" ]
        $ get_ach('voca', tm=0.6)
        $ persistent.chance_flo = 100
        $ game_end()
    elif kaitoim == True and chance_k == 1:
        play sound [ "<silence .02>", "audio/start/nofanru_kaito.wav" ]
        call kaito_list_lable('voice') from _call_kaito_list_lable_8
    else:
        play sound [ "<silence .05>", "audio/start/nofanru_rui.wav" ]

        if persistent.chance_flo > 10:
            $ n1 = len(persistent.rui_ends_list_per)
            $ n2 = len(persistent.secret_ends_list_per) * 2
            $ n3 = len(persistent.done_ach) // 2
            $ n = 1+n1+n2+n3
            $ persistent.chance_flo -= n
        
    show nofanru_logo2 at truecenter with Dissolve(.3)

    pause 2.5

    scene black with dissolve

    if _preferences.language == None:
        play sound "audio/start/sponsors_ru_rui.wav"
    else:
        play sound "audio/start/sponsors_en_rui.wav"
    queue sound [ "<silence .1>", "audio/start/ari_rui.wav"] 

    show screen sponsors

    pause 2.5

    hide screen sponsors with dissolve

    show screen waring with dissolve

    pause

    hide screen waring with Dissolve(.3)

    $ _dismiss_pause = False

    pause 0.5

    if kaitoim == True and chance_k == 2:
        play sound [ "<silence .1>", "audio/start/sekai_kaito.wav" ]
        call kaito_list_lable('voice') from _call_kaito_list_lable_9
    else:
        play sound [ "<silence .1>", "audio/start/sekai_rui.wav" ]

    show logo zorder 3:
        zoom 0.5 yalign 0.03 xalign 0.97 alpha 0.0
        ease 1.0 zoom 0.2 alpha 1.0
        ease 0.3 zoom 0.23

    pause 0.3

    play music dillema fadein 2.0

    $ persistent.markshortclick = "splashscreen.h"

    if persistent.low == 2:
        show titleim zorder 1
        with Dissolve(1.0)
    else:
        show expression Par(("bgtitleim"), ("startimglitch"), ("titleimchr")) as titleim zorder 1
        show overtitleim zorder 2
        with Dissolve(1.0)

    pause 0.2

    show nofanru_logo2 zorder 2:
        xalign 0.97 zoom 0.23 yalign 0.98 alpha 0.0
        pause 0.01
        linear 0.3 alpha 1.0

    show screen titlestart with Dissolve(.3)

    if kaitoim:
        call kaito_list_lable('startim') from _call_kaito_list_lable_10

    if persistent.low == 2:
        $ _dismiss_pause = True
    pause

    label .h:

        $ _dismiss_pause = True

        play sound "audio/ui_sfx/choice.flac"

        stop music fadeout 1.0

        hide screen titlestart
        scene black
        with Dissolve(.7)

        pause 0.2

        play music main fadein 1.0

        pause 0.1

        return