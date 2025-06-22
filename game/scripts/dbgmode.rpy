define dmt = 2

default persistent.debugmode = 2

define platform = "Mobile" if renpy.mobile else "PC"
define sizeplatform = "Small" if renpy.variant("small") else "Normal"

init python:
    import pygame

    def scresize():
        if renpy.mobile:
            pygame.init()
            persistent.sizee1 = pygame.display.Info().current_w
            persistent.sizee2 = pygame.display.Info().current_h
        else:
            persistent.sizee1, persistent.sizee2 = renpy.get_physical_size()

        persistent.sreenot = (persistent.sizee1 / persistent.sizee2)*9
        persistent.sreenover = False if persistent.sreenot == 16 else True        
        persistent.sreenot = round(persistent.sreenot, 1)
        

screen scrover():
    zorder 1000
    if persistent.sreenover:
        add "screenover"
    else:
        add "nothing"

define mobsmall = True if renpy.variant("small") else False

# label splashscreen:

#     $ scresize()
#     if not renpy.mobile:
#         $ config.overlay_functions.append(scresize)

#     show screen scrover
#     show screen debugscreen

#     pause 0.01

screen debugtrue():
    add "gui/overlay/confirm.png" alpha 0.7 at disall(0.0, 0.03, 0.07, 0.03)
    modal True
    frame at showframe(0.05):
        style_prefix "styleframe"
        xalign 0.5
        yalign 0.5
        padding (frpadx, frpady)

        vbox:
            text _("Режим откладки показывает дополнительную информацию на экране") xalign 0.5
            text _("и нужен только для облегчения поиска проблем и багов в игре.") xalign 0.5
            text _("В иных случаях экран будет только мешать вашей игре.") xalign 0.5
            null height nullsp
            text _("Для включения этой функции также требуется перезагрузка.") xalign 0.5
            text _("Вы уверены, что хотите включить режим откладки?") xalign 0.5
            null height nullbt
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
                        action Hide("debugtrue")
                null width 10
                vbox:
                    xsize twobt           
                    imagebutton:
                        ycenter ycen xcenter twobtx
                        idle "btn yes"
                        hover "hover yes"
                        keysym('K_RETURN')
                        action [SetField(persistent, "debugmode", dmt), Function(renpy.quit, relaunch=True, save=True)]

default persistent.dbgshow = True

style dbgframe_frame:
    padding gui.frame_borders.padding
    background Frame("dbg_frame", gui.frame_borders, tile=gui.frame_tile)

style dbgnone_frame:
    padding gui.frame_borders.padding
    background Frame("nothing", gui.frame_borders, tile=gui.frame_tile)

screen debugscreen():

    zorder 1001

    drag:

        xalign 1.0 yalign 1.0
        drag_name "dbg"

        frame:

            style_prefix "dbgframe"

            vbox:
                if persistent.dbgshow:
                    textbutton "Обновить" action renpy.restart_interaction
                    null height 10
                    textbutton "Скрыть" action [SetField(persistent, 'dbgshow', False), Hide("_performance")] xalign 0.5 
                else:
                    textbutton "Показать" action [SetField(persistent, 'dbgshow', True), Show("_performance")] xalign 0.5

    if persistent.dbgshow:

        vbox: 
            xalign 0.0 yalign 0.05
            text "[persistent.sizee1]:[persistent.sizee2]"
            text "[persistent.sreenot]"
            text "[platform] | [sizeplatform] | [persistent.sreenover]"
            text "lowmode: [persistent.low]"

        vbox: 
            xalign 1.0 yalign 0.05
            text "coins: [persistent.coins]"
            text "crystal: [persistent.crystal]"
            text "fl_chance: [persistent.chance_flo]"

        if dmt == 2:
            drag:
                yalign 0.8
                frame:
                    ysize 200
                    xfill False
                    style_prefix "dbgnone"
                    hbox:
                        xfill False
                        $ ach_dbg_len = len(persistent.ach)
                        viewport id "ach_dbg":
                            mousewheel True
                            xfill False
                            vbox:
                                xfill False
                                for i_ach_dbg in range(0, ach_dbg_len):
                                    $ text_dbg_ach = persistent.ach[i_ach_dbg]
                                    text "[text_dbg_ach]"
                        vbar value YScrollValue("ach_dbg")

        # drag:
        #     yalign 1.0
        #     frame:
        #         style_prefix "dbgnone"
        #         vbox:
        #             text "[persistent.done_ach]"
        #             null height 20
        #             text "[persistent.ach_code]"
        #             null height 20
        #             text "[persistent.ach_rui_100]"
        #             text "[persistent.ach_com_100]"
        #             null height 20
        #             text "[persistent.rui_ach_pct]"
        #             text "[persistent.common_ach_pct]"

        # drag:
        #     yalign 0.2
        #     frame:
        #         style_prefix "dbgnone"
        #         vbox:
        #             text "[persistent.kaito]"

        # drag:
        #     yalign 0.3
        #     vbox:
        #         text "rui_ends: [persistent.rui_ends_list_per]"
        #         null height 20
        #         text "secret_ends: [persistent.secret_ends_list_per]"

        drag:
            text "[persistent.aaaaaaaa]"
                

        timer 0.01 action Show("_performance")