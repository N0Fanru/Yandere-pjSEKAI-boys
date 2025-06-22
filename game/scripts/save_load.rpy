init -1 python hide:

    if persistent.locked is None:
        persistent.locked = []

default playtime = 0


init 2 python:

    #The following is for the last line displayed in saves.
    ##IMPORTANT: The number in the brackets is CHARACTER COUNT! This is how many characters will be displayed. It also includes spaces and punctuation as characters, but later in the code I add Quotation Marks and Elipses. Depending on the font you use, adjust the number accordingly!

    #Also, keep in mind the font your using! If you have a feature that changes fonts for the UI, it could mess with the length that could mess with the size of the container. I recommend just using one font only for this.

    number_last = 23 if renpy.variant("small") else 30

    def the_lastline(d):
        mylast_line = getattr(store, '_last_raw_what', '',)
        line_take = renpy.substitute(renpy.filter_text_tags(mylast_line, allow=[]))[:number_last] #<--that number is the character count! adjust as needed
        d["last_line"] = line_take

    def save_playtime(d):
        renpy.store.playtime += renpy.get_game_runtime()
        renpy.clear_game_runtime()
        d["playtime"] = renpy.store.playtime

    config.save_json_callbacks = [save_playtime, the_lastline]

    #The following is for the save lock feature. Not much to note here.
    def lockSave(slotname):
        persistent.locked.append(slotname)
        if persistent.locked is None:
            persistent.locked = []

    def unlockSave(slotname):
        persistent.locked.remove(slotname)
        if persistent.locked is None:
            persistent.locked = []

    #And this controls how large your thumbnail screenshots are!
    # config.thumbnail_width = 300
    # config.thumbnail_height = 169

screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    #use navigation
    use file_picker(_("Сохранения"))

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    #use navigation
    use file_picker(_("Сохранения"))



image btn auto:
    "bt auto_unselect"
    btn_all

image hover auto:
    "bt auto_unselect"
    bt_all_hover

image btnsel auto:
    "bt auto_select"
    btn_all

image hoversel auto:
    "bt auto_select"
    bt_all_hover

image btn fast:
    "bt fast_unselect"
    btn_all

image hover fast:
    "bt fast_unselect"
    bt_all_hover

image btnsel fast:
    "bt fast_select"
    btn_all

image hoversel fast:
    "bt fast_select"
    bt_all_hover


define savelinesize = 580 if renpy.variant("small") else 420
define savelinepos = 1270 if renpy.variant("small") else 1180
define possavebt = 150 if renpy.variant("small") else 117
define ypossave = 1.0 if renpy.variant("small") else 0.75

screen file_picker(title):

    # if main_menu:
    #     add gui.main_menu_background
    # else:
    #     add gui.game_menu_background
    tag menu

    #use navigation

    # default page_name_value = FilePageNameInputValue(pattern=_("Страница {}"), auto=_("Автоматические сохранения"), quick=_("Быстрые сохранения"))

    use game_menu(title):
        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            # button:
            #     style "page_label"

            #     key_events True
            #     xalign 0.5
            #     action page_name_value.Toggle()

            #     input:
            #         style "page_label_text"
            #         value page_name_value

        #the grid of file slots

        frame at showframemenu(0.25):
            style_prefix "styleframemenu"
            padding (frpadx, frpady)
            xalign 0.5
            yalign ypossave
            if renpy.variant("small"):
                ypos 900
            ysize setysize 
            xsize setxsize

            imagebutton:
                anchor (0.5, 0.5) xpos 150 ypos 20
                idle "btn auto"
                hover "hover auto"
                selected_idle "btnsel auto"
                selected_hover "hoversel auto"
                activate_sound "audio/ui_sfx/touch.flac"
                action FilePage("auto")

            imagebutton:
                anchor (0.5, 0.5) xpos 480 ypos 20
                idle "btn fast"
                hover "hover fast"
                selected_idle "btnsel fast"
                selected_hover "hoversel fast"
                activate_sound "audio/ui_sfx/touch.flac"
                action FilePage("quick")

            imagebutton:
                anchor (0.5, 0.5) xpos 810 ypos 20
                idle "btn info"
                hover "hover info"
                selected_idle "btnsel info"
                selected_hover "hoversel info"
                activate_sound "audio/ui_sfx/touch.flac"
                action FilePage(1)

            frame:
                xsize savelinesize
                ysize 5
                style_prefix "textline"
                anchor (0.5, 0.5) xpos savelinepos ypos 40

            hbox:
                xalign .85
                yalign .5
                $ columns = 1
                $ rows = 10

                # Display a grid of file slots.            

                hbox:
                    xfill True
                    ysize abtsize
                    yalign 0.6
                    spacing setnull1

                    viewport id "saves":

                        yinitial 0.0
                        mousewheel True
                        draggable True
                        xfill True  

                        vbox:
                            style_group "file_picker"
                            xfill True

                            null height 20

                            # Display ten file slots, numbered 1 - 10.
                            for i in range(1, columns * rows + 1):

                                #add "slot_save"

                                # Each file slot is a button.
                                button: #note that if you put ANY IMAGE in the following, it will add and stretch the bg. Trust me, I tried lol
                                    xfill True
                                    # action FileLoad(i)
                                    has hbox
                                    null width 5
                                    use file_info
                                    null width 4
                                    # use file_butt
                                # OKAY THIS IS REALLY SILLY IN HOW THIS WORKS:
                                # So the background for the file slots is actually a button! The reason why it's a button is because the FileSave, FileLoad, and FileAction functions have a feature to show which save file is the newest. The button will be marked as *selected* if it is the newest, so the images used for ‘selected_background’ and ‘selected_hover_background’ are used to denote that it’s the newest file. I didnt assign a ‘selected_’ function to the save and load buttons specifically because it looks weird and doesn't clearly signal to the player that it's the newest save.
                                # Because of this though, that means the background of the save file is hoverable and clickable. I have it set so that it loads because I figured a locked file would still be able to load, just not delete or save over.

                                null height 30

                    vbar value YScrollValue("saves")

    if persistent.sreenover:
        add "screenover"

#This screen has all the info of the save/load
screen file_info:

        frame:

            has hbox

            xfill False
            yfit True

            #adds the screenshot
            add AlphaMask (FileScreenshot(i), "alpha_slot") yalign .5 # xalign .5

            vbox:

                #adds the last phrase that was defined earlier
                $ last_phrase = FileJson(i, "last_line", empty="", missing="")

                #adds the time whe the player saves their file
                $ file_time = FileTime(i, format=u'%b %d %Y, %I:%M %p', empty="")

                $ file_name = FileSlotName(i, columns * rows)

                hbox:

                    #and the phrase itself! In here, I included quotation marks around the phrase and ... at the end of it, but those marks are not included in the character limit defined earlier.
                    if file_time != "" and last_phrase == "":
                        text _("{color=#000}Без имени  {size=-10}Файл [file_name]{/size}{/color}") xpos 22
                    elif file_time != "":
                        text _("{color=#000}\"[last_phrase]...\"  {size=-10}Файл [file_name]{/size} {/color}") xpos 22
                    elif file_time == "":
                        text _("{color=#000}Пустой слот{/color}") xpos 22

                    null width 40

                    #LOCK BUTTON#
                    #AND BEHOLD THE LOCK BUTTON!
                    if(file_name in persistent.locked): #this means that if the slot is locked, then the following happens
                        imagebutton: #which is that the Unlock is selectable!
                            if renpy.variant("small"):
                                ypos 12
                            idle "gui/lock.png"
                            hover "gui/unlock_hov.png"
                            activate_sound "audio/ui_sfx/tap.flac"
                            action [Function(unlockSave, file_name)] #and the function to get it to run!
                    else:                             #this means that if the slot shows that it is not locked, then the following happens
                        if file_time != "": #this means that if the file_time does not show "Empty Slot", then the following happens. Which is the opposite of before!
                            imagebutton: #which is that the Lock is selectable!
                                if renpy.variant("small"):
                                    ypos 12
                                idle "gui/unlock.png"
                                hover "gui/lock_hov.png"
                                activate_sound "audio/ui_sfx/tap.flac"
                                action [Function(lockSave, file_name)]
                        elif file_time == "": #And if it does show Empty Slot, then its untoggleable but still shows the image. Which means you can't lock and unlock empty saves!
                            imagebutton:
                                if renpy.variant("small"):
                                    ypos 12
                                idle "gui/unlock_insens.png"

                hbox:

                    frame:

                        has vbox
                        # yalign .5
                        # xalign .5
                        style_group "saveload"
                        spacing 0
                        #Yes, I had to rename this here. idk why but if I take this out the code breaks, so...
                        $ file_time = FileTime(i, format=u'%b %d %Y, %I:%M %p ', empty="")

                        #This adds the name of the file, which is a number
                        $ file_name = FileSlotName(i, columns * rows)

                        $ playtime = FileJson(i, "playtime", empty=0, missing=0) 
                        $ minutessave, secondssave = divmod(int(playtime), 60)
                        $ hourssave, minutessave = divmod(minutessave, 60)


                        # text _("{color=#000}Файл [file_name]{/color}") xalign .5

                        text "{color=#000}{size=-5}[hourssave:02d]:[minutessave:02d]:[secondssave:02d]{/size}{/color}" xpos 18

                        #SAVE BUTTON#
                        if(file_name in persistent.locked): #this means that if the slot is locked, then the following happens
                            textbutton _("Сохранить") xpos possavebt #By not assigning an option, the button shows but doesnt do anything
                        else: #and if its not locked, then this button is useable!
                            textbutton _("Сохранить") xpos possavebt activate_sound "audio/ui_sfx/touch.flac" action FileSave(i, confirm=True, page=None)

                        #LOAD BUTTON#
                        #Not much to do here. Load is always showing and intereactable even if the save is locked.
                        textbutton _("Загрузить") activate_sound "audio/ui_sfx/touch.flac" action FileLoad(i, confirm=True, page=None)


                    hbox:

                        xfill True
                        xalign 1.0
                        yalign 1.0
                        spacing 0

                        style_group "saveload"

                        $ file_time = FileTime(i, format=u'%b %d %Y, %I:%M %p', empty="")

                        #and then you put it in text! Here I changed the size and alignment to the specifc text
                        text "{color=#000}[file_time]{/color}" size 22 yalign 0.85 xpos 250
                        #DELETE BUTTON#
                        #same as before in save~
                        button:
                            xalign 1.0
                            frame:
                                style_prefix "frametextred"
                                if(file_name in persistent.locked):
                                    text _("{color=#be4e4f}{font=gt}{size=-5}Удалить{/size}{/font}{/color}")
                                else:
                                    text _("{font=gt}{size=-5}Удалить{/size}{/font}")
                            if not (file_name in persistent.locked):
                                activate_sound "audio/ui_sfx/touch.flac"
                                action FileDelete(i, confirm=True, page=None)

                                # "#be4e4f"

                        # if(file_name in persistent.locked):
                        #     textbutton _("Удалить") xalign 1.0
                        # else:
                        #     textbutton _("Удалить") action FileDelete(i, confirm=True, page=None) xalign 1.0

#This is the vertical selection of buttons, which include Save, Load, Delete, and Lock/Unlock
# screen file_butt:

#         frame:

#             has vbox
#             yalign .5
#             xalign .5
#             style_group "saveload"
#             #Yes, I had to rename this here. idk why but if I take this out the code breaks, so...
#             $ file_time = FileTime(i, format=u'%b %d %Y, %I:%M %p', empty=_("Empty Slot"))

#             #This adds the name of the file, which is a number
#             $ file_name = FileSlotName(i, columns * rows)

#             text _("Файл [file_name]") xalign .5

#             null height 10

#             #SAVE BUTTON#
#             if(file_name in persistent.locked): #this means that if the slot is locked, then the following happens
#                 textbutton _("Сохранить") #By not assigning an option, the button shows but doesnt do anything
#             else: #and if its not locked, then this button is useable!
#                 textbutton _("Сохранить") action FileSave(i, confirm=True, page=None) xalign .5

#             #LOAD BUTTON#
#             #Not much to do here. Load is always showing and intereactable even if the save is locked.
#             textbutton _("Загрузить") action FileLoad(i, confirm=True, page=None) xalign .5

#             #DELETE BUTTON#
#             #same as before in save~
#             if(file_name in persistent.locked):
#                 textbutton _("Удалить")
#             else:
#                 textbutton _("Удалить") action FileDelete(i, confirm=True, page=None) xalign .5

#             #LOCK BUTTON#
#             #AND BEHOLD THE LOCK BUTTON!
#             if(file_name in persistent.locked): #this means that if the slot is locked, then the following happens
#                 imagebutton: #which is that the Unlock is selectable!
#                     idle "gui/lock.png"
#                     hover "gui/unlock_hov.png"
#                     xalign .5
#                     action [Function(unlockSave, file_name)] #and the function to get it to run!
#             else:                             #this means that if the slot shows that it is not locked, then the following happens
#                 if file_time != "": #this means that if the file_time does not show "Empty Slot", then the following happens. Which is the opposite of before!
#                     imagebutton: #which is that the Lock is selectable!
#                         idle "gui/unlock.png"
#                         hover "gui/lock_hov.png"
#                         xalign .5
#                         action [Function(lockSave, file_name)]
#                 elif file_time == "": #And if it does show Empty Slot, then its untoggleable but still shows the image. Which means you can't lock and unlock empty saves!
#                     imagebutton:
#                         idle "gui/unlock_insens.png"
#                         xalign .5

            #BTW You can use the word Unlock as a textbutton, but i found that it changes the width very slightly when toggling between locked and not locked. I kept it here just in case though

            # if(file_name in persistent.locked): #this means that if the slot is locked, then the following happens
            #         textbutton _("Unlock"): #which is that the Unlock is selectable
            #             xalign .5
            #             action [Function(unlockSave, file_name)] #and the function to get it to run!
            #
            # else:                             #this means that if the slot shows that it is not locked, then the following happens
            #     if file_time != "Empty Slot": #this means that if the file_time does not show "Empty Slot", then the following happens. Which is the opposite of before!
            #         textbutton _("Lock"):
            #             xalign .5
            #             action [Function(lockSave, file_name)]
            #     elif file_time == "Empty Slot": #And if it does show Empty Slot, then its untoggleable. Which means you can't lock and unlock empty saves!
            #         textbutton _("Lock"):
            #             xalign .5


style saveload_button:
    right_padding 15
    left_padding 15
    insensitive_background None
    xalign .5
    xmaximum 500

style saveload_button_text:
    size gui.interface_text_size
    idle_color gui.idle_color
    hover_color gui.hover_color
    insensitive_color gui.insensitive_color

#This controls the background of the button. Take note of anything with the "selected_" prefix, because that is what shows the new file
style file_picker_button:
    #padding gui.frame_borders.padding
    background Frame("slot_save")

style file_picker_frame:
    background None

style file_picker_nav_button_text:
    left_margin 30
    size 38
    idle_color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.selected_color
    insensitive_color gui.insensitive_color
    xalign .5

style file_picker_nav_button:
    background None
    hover_background None
    selected_background None
    insensitive_background None
    xpadding 10
    xmargin 2