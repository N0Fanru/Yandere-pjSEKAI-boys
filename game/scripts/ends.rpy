define ends_what = "ends_secret"

style end_text_button is button

style end_text_button_text is button_text:

    hover_color '#707070'
    idle_color '#ffffff'

default persistent.last_end = "null"

default persistent.rui_ends = int(0)
default persistent.rui_ends_list_per = [] # только кодовое имя
default persistent.rui_end = [] # матрица [новое или нет, имя, лейбл, изображение]
default rui_ends_list = []

default persistent.secret_ends = int(0)
default persistent.secret_ends_list_per = [] # только кодовое имя
default persistent.secret_end = [] # матрица [новое или нет, имя, лейбл]
default secret_ends_list = []

default this_end = []

define all_rui_end_ru = ["Бомбезная концовка", "Концовка молчуна", "Идеальный мир", "Хорни концовка", "Молчание - знак согласия", "Обречённая концовка", "Вечные слёзы",
"Двойное желание", "Завтра забудем", "Смачная пизделовка", "Ядерно-приторная концовка", "Концовка любителей животных", "Комфорти концовка", "Руи заставлял тебя сосать",
"Сосательная концовка", "Руи лучший", "Концовка изменика", "Ядерный анал", "Великий учёный", "Ты меня бум-бум-бум", "Вот и помер наш Руй", "С днём полиамории",
"Счастливая концовка", "Двойное самоубийство?", "The End", "Подвальный пиздец", "Переезд"]

define all_rui_end_code = ['bum', 'ne_molchi', 'yaderka', 'ebi', 'molchun_ebka', 'ne_ebi', 'iznos', 'ubeysa', 'tsu_die', 'tsu_pain', 'tsu_bum', 'rui_dog', 'rui_ps',
'zastavlal', 'minet', 'the_best', 'izmena', 'anal', 'turma', 'bum_bum', 'die', 'orgia', 'happy', 'suid', 'the_end', 'podval', 'home']

define all_secret_end_ru = ['Генератор рандомных чисел', 'Концовка благодарности', 'Спасибо, что доводите рассказчика!', persistent.time_secret, "Кайто~"]

define all_secret_end_code = ['genran', 'thank', 'name', 'time', 'kaito']

define all_rui_end_eng = []
define all_secret_end_eng = []

default persistent.coins = int(0)
default persistent.crystal = int(0)

init python:

    if _preferences.language == None:
        all_rui_end = all_rui_end_ru
        all_secret_end = all_secret_end_ru
    elif _preferences.language == 'english':
        all_rui_end = all_rui_end_eng
        all_secret_end = all_secret_end_eng
    elif translation:
        all_rui_end = all_rui_end_tl
        all_secret_end = all_secret_end_tl

    def what_rui_end(end_code, new_or_not):
        get_ach("rui_fan")
        get_ach("fan")
        ie = all_rui_end_code.index(end_code)
        this_end_im = 'end rui ' + end_code
        this_end_lable = 'rui_end_label.' + end_code
        this_end = [new_or_not, all_rui_end[ie], this_end_lable, this_end_im]
        return this_end

    def what_secret_end(end_code, new_or_not):
        get_ach("secret_ends")
        get_ach("fan")
        ie = all_secret_end_code.index(end_code)
        this_end_lable = 'secret_end_label.' + end_code
        this_end = [new_or_not, all_secret_end[ie], this_end_lable]
        return this_end



    if len(persistent.rui_ends_list_per) > 0 and len(persistent.rui_end) == 0:
        new_rui_end_list = []
        n = len(persistent.rui_ends_list_per)
        persistent.coins = persistent.coins + 2000 * n
        for i in range(0, n):
            end_name = persistent.rui_ends_list_per[i]
            end = what_rui_end(end_name, False)
            new_rui_end_list.append(end)
        persistent.rui_end = new_rui_end_list

    if len(persistent.secret_ends_list_per) > 0 and len(persistent.secret_end) == 0:
        new_secret_end_list = []
        n = len(persistent.secret_ends_list_per)
        persistent.coins = persistent.coins + 1000 * n
        persistent.crystal = persistent.crystal + 500 * n
        for i in range(0, n):
            end_name = persistent.secret_ends_list_per[i]
            end = what_secret_end(end_name, False)
            new_secret_end_list.append(end)
        persistent.secret_end = new_secret_end_list

define endnotizoom = 1.3 if renpy.variant("small") else 1.0

screen new_end_noti(end, what):
    zorder 100
    if what == 'rui':
        $ end_id = all_rui_end_code.index(end)
        $ end_name = all_rui_end[end_id]
    frame at notify_appear:
        yalign 0.04
        xalign 0.04
        style_prefix "end_noti"
        hbox:
            add "end_noti" yalign 0.6 zoom endnotizoom
            null width 20
            vbox:
                text _("{font=gt}Вы открыли новую концовку!{/font}")
                text _("{size=-5}[end_name]{/size}")
    timer 3.25 action Hide('new_end_noti')

screen new_secret_end_noti(end):
    zorder 100
    $ end_id = all_secret_end_code.index(end)
    $ end_name = all_secret_end[end_id]
    frame at notify_appear:
        yalign 0.04
        xalign 0.04
        style_prefix "end_noti"
        hbox:
            add "end_noti" yalign 0.6 zoom endnotizoom
            null width 20
            vbox:
                text _("{font=gt}Вы открыли {color=#ffd700}секрутную{/color} концовку!{/font}")
                text _("{size=-5}[end_name]{/size}")
                timer 0.01 action Play("ui", "audio/ui_sfx/end.flac")
    timer 3.25 action Hide('new_secret_end_noti')

style end_noti_frame:
    # ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding (50, 20, 50, 20)

style end_noti_text:
    color '#000'


label ends_rui(end):

    $ persistent.last_end = end

    if not end in persistent.rui_ends_list_per:
        $ renpy.show_screen('new_end_noti', end, 'rui')
        $ rui_ends_list = persistent.rui_ends_list_per 
        $ rui_ends_list.insert(0, end)
        $ persistent.rui_ends_list_per = rui_ends_list
        $ persistent.rui_ends = len(persistent.rui_ends_list_per)
        $ rui_ends_list = persistent.rui_end
        $ new_end = what_rui_end(end, True)
        $ rui_ends_list.insert(0, new_end)
        $ persistent.rui_end = rui_ends_list
        $ persistent.morenoti = True
        $ persistent.coins += 2000
    return

label ends_secret(end):

    $ persistent.last_end = "secret"

    if not end in persistent.secret_ends_list_per:
        $ renpy.show_screen('new_secret_end_noti', end)
        $ secret_ends_list = persistent.secret_ends_list_per 
        $ secret_ends_list.insert(0, end)
        $ persistent.secret_ends_list_per = secret_ends_list
        $ persistent.secret_ends = len(persistent.secret_ends_list_per)
        $ secret_ends_list = persistent.secret_end
        $ new_end = what_secret_end(end, True)
        $ secret_ends_list.insert(0, new_end)
        $ persistent.secret_end = secret_ends_list
        $ persistent.morenoti = True
        $ persistent.coins += 1000
        $ persistent.crystal += 500
    return



transform showendsmenu(pe):
    choice(persistent.low == 0):
        xalign posforshowframe
        pause pe
        linear 0.2 xalign endxpos
    choice(persistent.low > 0):
        xalign endxpos

define btsidesize = 130 if renpy.variant("small") else 115
define endssize = 600 if renpy.variant("small") else 560
define endxpos = 0.9 if renpy.variant("small") else 0.8
# define endxsize = 1500 if renpy.variant("small") else 1500
define xposnotiend = 250 if renpy.variant("small") else 210
define sizenotiend = 1.0 if renpy.variant("small") else 0.8

style stylebtside_button:
    background Frame("text line", 0, 0, tile=gui.frame_tile)
    selected_background Frame("btside", 0, 0, tile=gui.frame_tile)

style stylebtside_text:
    font "gt"
    outlines [(2, "#000000b0")]

style frameendslot_frame:
    background Frame("slot_save")

style frameendslot_text:
    color "#000"
    size 45

style endtextsz is stylebtside_text:
    size 30

style endtextsz is stylebtside_text:
    variant "small"
    size 37

default persistent.what_ends_show = [persistent.secret_end, 'secret']


screen waitruiends():
    timer .01 action [Hide("loading"), SetField(persistent, 'what_ends_show', [persistent.rui_end, 'rui'])]

screen ends():

    modal True
    tag menu
    use menus(_("Концовки"), frmside = True)

    if persistent.what_ends_show[1] == 'rui':
        timer 0.01 action Show("waitruiends")

    timer 0.01 action Hide("loading")

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
                text _("{=endtextsz}Секретные")
            activate_sound "audio/ui_sfx/touch.flac"
            action [Hide("waitruiends"), SetField(persistent, 'what_ends_show', [persistent.secret_end, 'secret'])]

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
            if not renpy.get_screen("waitruiends"):
                activate_sound "audio/ui_sfx/touch.flac"
                action [Show("loading"), Show("waitruiends")]
            else:
                action SetField(persistent, 'what_ends_show', [persistent.rui_end, 'rui'])

    vbox:
        yalign 0.5
        spacing 40
        xpos xposnotiend
        $ new_rui_end = True if contains_element(persistent.rui_end, True) else False
        $ new_secret_end = True if contains_element(persistent.secret_end, True) else False
        button:
            ysize btsidesize
            if new_secret_end:
                add "noti" zoom sizenotiend ypos -20
        button:
            ysize btsidesize
            if new_rui_end:
                add "noti" zoom sizenotiend ypos -20



    
    frame at showendsmenu(0.25):
        style_prefix "styleframemenu"
        padding (frpadx, frpady)
        yalign yposset
        ysize setysize 
        xsize 1500

        vbox:
            ypos -30
            if persistent.what_ends_show[1] == 'secret':
                text _("{image=icontext1} {=settitle}Открыто концовок: [persistent.secret_ends]")
            else:
                if persistent.what_ends_show[1] == 'rui':
                    $ x1 = persistent.rui_ends
                    $ x2 = len(all_rui_end_code)
                text _("{image=icontext1} {=settitle}Открыто концовок: [x1] из [x2]")
            null width 20
            frame:
                xfill True
                ysize 5
                style_prefix "textline"

        hbox:
            xfill True
            ysize endssize
            yalign 0.6
            viewport id "ends":
                xfill True
                xpos -20
                draggable True
                mousewheel True
                arrowkeys True
                
                vbox:
                    xfill True
                    spacing -5
                    $ real_ends = persistent.what_ends_show[0]
                    $ n = len(real_ends)

                    if n == 0:
                        text _("Вы ещё не открыли ни одной концовки!") xalign 0.5 ypos 240

                    else:
                        null height 30

                        for j in range(0, n):

                            $ name = real_ends[j][1]
                            $ num = j + 1

                            button:
                                frame:
                                    style_prefix "frameendslot"
                                    xfill True
                                    ysize 228
                                    if persistent.what_ends_show[1] != 'secret':
                                        add AlphaMask (real_ends[j][3], "alpha_end") zoom 0.2 xalign 1.002 ypos -1
                                    hbox:
                                        yalign 0.5
                                        null width 80
                                        text '[num]. [name]'
                                activate_sound "audio/ui_sfx/touch.flac" 
                                action MyCall('end_not_new', persistent.what_ends_show[1], j, real_ends[j][2])

                            if real_ends[j][0] == True:
                                add "new" xalign 1.0 ypos -250 zoom 0.8
                            else:
                                add "not_new" xalign 1.0 ypos -250 zoom 0.8

            null width 5

            vbar value YScrollValue("ends")

label end_not_new(what_ends, what_index, what_label):

    if what_ends == 'rui':
        $ persistent.rui_end[what_index][0] = False
    elif what_ends == 'secret':
        $ persistent.secret_end[what_index][0] = False

    $ noti_more_or_not()

    $ renpy.jump(what_label)

    

label rui_end_label:

    label .bum:

        window hide
        scene end rui bum 


        '''"Бомбезная концовка"

        У многих людей есть привычка игнорить...

        А теперь посмотрите до чего она может довести и сделайте выводы.

        '''

        window hide
         

        pause

        $ MyReturn()()
        return

    label .ne_molchi:

        window hide

        scene end rui ne_molchi


        '''"Концовка молчуна"

        Мда, вам стоит перестать вечно молчать, иначе подобное может и в реальной жизни произойти...

        '''

        window hide
         

        pause
        $ MyReturn()()

        return

    label .yaderka:

        window hide

        scene end rui yaderka


        '''Концовка: "Идеальный мир"

        Не важно, что ты сделаешь, если в голову Руи уже пришла идея, он её воплотит...

        В любом случае, вы чувствуете себя счастливо. Есть ли разница как было вызвано это счастье?

        Теперь ваша любовь будет существовать вечно, ничто не сможет вам помешать...

        '''

        window hide
         

        pause
        $ MyReturn()()

        return

    label .ebi:

        window hide

        scene end rui ebi


        '''"Хорни концовка"

        Вы готовы вечность кувыркаться в кровати с Руи.

        Этот парень безумен: он всегда найдёт способ сам получить удовольствие и вас заствит побывать на 7 небе.

        Не важно сколько раз вы уже этим занимались, Камиширо заставит вас почувствовать всё также как в первый раз.

        Вы навечно влюблены в Руи и в Руи-младшего.

        '''

        window hide
         

        pause
        $ MyReturn()()

        return

    label .molchun_ebka:

        window hide

        scene end rui molchun_ebka


        '''Концовка: "Молчание - знак согласия"

        Вы молчали в первые разы, вы не были уверены в том действительно ли вы хотели заниматься с Руи сексом...

        Но со временем вы вошли во вкус и теперь каждый день наслаждаетесь этим.
        
        '''

        window hide
         

        pause
        $ MyReturn()()

        return

    label .ne_ebi:

        window hide

        scene end rui ne_ebi
 

        '''"Обречённая концовка"

        Вы навечно обречены быть с Руи. Вы навечно обречены заниматься с ним сексом. Вы не сможете убежать, вы ничего не можете поделать...

        Вы останетесь с ним до конца своих дней.

        '''

        window hide
         

        pause
        $ MyReturn()()

        return

    label .iznos:

        window hide

        scene end rui iznos


        '''Концовка: "Вечные слёзы"

        Вы будете много плакать, но чтобы вы не пытались сделать, Руи вас всегда остановит.

        Есть ли смысл с этим бороться? Есть ли смысл продолжать так жить?

        '''

        window hide
         

        pause
        $ MyReturn()()

        return

    label .ubeysa:

        window hide

        scene end rui ubeysa


        '''Концовка: "Двойное желание"

        Вы подумали, что сказав Руи убиться вы избавитесь от него...

        Было действительно глупо предполагать, что это сработает.

        Руи действительно умер ради вас, но и вас он с собой прихватил, потому что его счастье - это быть вместе с вами, а в отношениях оба партнёра должны быть счастливы.

        Довольны ли вы таким концом?

        '''

        window hide
         

        pause
        $ MyReturn()()

        return

    label .tsu_die:

        window hide

        scene end rui tsu_die

        '''Концовка: "Завтра забудем"

        После этого инцидента ваши отношения с Руи совсем не поменялись...

        Но...

        ...

        '''

        scene black with dissolve

        show end rui tsu die movie with dissolve

        window hide
         

        pause
        $ MyReturn()()

        return

    label .tsu_pain:

        window hide

        scene end rui tsu_pain


        '''Концовка: "Смачная пизделовка"

        Руи смачно отпиздил Цукасу на ваших глазах. Вы решили ничего не делать.

        После этого, Цукаса понял, что вы такие же ебанутые, как и Руи.

        Вы жили с Руи долго и счастливо, ура-ура.

        '''

        window hide
         

        pause
        $ MyReturn()()

        return

    label .tsu_bum:

        window hide

        scene end rui tsu_bum


        '''"Ядерно-приторная концовка"

        Руи скинул ядерку на дом Тенмы... 
        
        Вся семья Цукасы и он сам умерли на месте.

        Полиция хуй пойми как, но не смогла раскрыть это дело.

        Кажется, вы стали ещё более привязаны к Руи! {p}Из-за любви или из-за страха - хороший вопрос...

        Вывод: не играйтесь с ядеркой.

        '''

        window hide
         

        pause
        $ MyReturn()()

        return

    label .rui_dog:

        window hide

        scene end rui rui_dog


        '''"Концовка любителей животных"

        Руи стал вашей собачкой и теперь готов выполнить любую вашу просьбу!

        ...

        И вам действительно нравится это, грязный извращенец?..

        '''

        window hide
         

        pause
        $ MyReturn()()

        return

    label .rui_ps:

        window hide

        scene end rui rui_ps


        '''"Комфорти концовка"

        Вы смогли уговорить Руи пройти курс психотерапии...

        Спустя пару терапий его ментальное здоровье и впрямь начало улучшаться. Ваши отношения наконец-таки стали здоровыми.

        В будущем вы выйдите за Руи замуж, у вас родится ребёнок, он будет гением и в 16 лет создаст игру "Yandere pjSEKAI boys"!

        Самая адекватная концовка в этой игре, ура-ура.

        '''

        window hide
        show end rui rui_ps2 with Dissolve(.3)
         

        pause
        $ MyReturn()()

        return

    label .zastavlal:

        window hide

        scene end rui zastavlal


        '''Концовка: "Руи заставлял тебя сосать"

        Странно было, конечно, предлагать минет, а потом отказывать такому неадеквату как Руи, но вы это сделали!

        Конечно же он разозлился и ваши отношения стали ещё более больными.

        Теперь он будет заставлять сосать вас каждый день....

        Теперь вы просто мечтаете предъявить ему перед судом что-то вроде "ты заставлял меня сосать", но это так и останется вашей мечтой... навечно...

        '''

        window hide
         

        pause
        $ MyReturn()()

        return

    label .minet:

        window hide

        scene end rui minet


        '''"Сосательная концовка"

        Вы сделали Руи смачный минет...

        Что ж, вам понравилось такое общение с Руи-младшим!

        Теперь вы готовы сосать вечность.

        '''

        window hide
         

        pause
        $ MyReturn()()

        return

    label .the_best:

        window hide

        scene end rui the_best


        '''Концовка: "Руи лучший"

        Вы попытались пофлиртовать с Цукасой, но потерпели неудачу!

        Потом пришёл ваш любимый Руи и понял вас по одному только взгляду.

        Теперь вы поняли то, что вам нужен только он. Только Руи. Руи лучший.

        '''

        window hide
         

        pause
        $ MyReturn()()

        return

    label .izmena:

        window hide

        scene end rui izmena


        '''"Концовка изменника"

        Вы решили попробовать изменить Руи с Цукасей. {w=1}Результаты оказались достаточно плачевные...

        Руи сильно избил Цукасу, тот по какой-то причине не стал докладывать о случившимся.

        Теперь Руи контролирует каждый ваш шаг.
        
        Он не позволяет вам даже в туалет одной сходить... Ну а вдруг вы там будете дрочить на лысого мужика, изображённого на упаковке чистящего средства!

        '''

        window hide
         

        pause
        $ MyReturn()()

        return

    label .anal:

        window hide

        scene end rui anal


        '''Концовка: "Ядерный анал"

        У вас действительно был крайне интересный и уникальный опыт...

        Сначала Руи засунул вам в жопу ядерку, затем трахнул вас туда же, дроча вашу пизду ядеркой... {p=1}И после этого вы уютно посидели вместе, поели пиццы и посмотрели сериалы.

        Эхх.. отношения мечты.

        '''

        window hide
         

        pause
        $ MyReturn()()

        return

    label .turma:

        window hide

        scene end rui turma


        '''Концовка: "Великий учёный"

        Удивительно, как сложилась ваша жизнь.

        Вы выиграли суд над Руи, но его из тюрьмы вытащило правительство...

        Теперь он известен по всему миру как великий учёный.

        В целом, вас устраивает такой исход, ведь так вы точно полностью в безопасности.{w=0.5}.. так ведь? 

        '''

        window hide
         

        pause
        $ MyReturn()()

        return

    label .bum_bum:

        window hide

        scene end rui bum_bum


        '''Концовка: "Ты меня бум-бум-бум"

        Жила была на свете [persistent.name], и однажды ей стало очень скучно...

        Тогда к ней пришёл её парень и поделился своим изобретением: ядерная бомба с размером чуть меньше его члена.

        [persistent.name] подумала: "а что есть эту бомбу вставить мне в жопу?"

        Её парень был поражён такой идеи, но не мог ей отказать...

        Но как оказалась, у нашей героине не было дома смазки! Её парень предложил сходить до магазина, но она не могла больше ждать...

        Он вставил ядерную бомбу ей в анал без смазки... {w=1}Бомба взорвалась, наша героиня умерла, а её парень был обречён страдать до тех пор, пока не скончается от переизбытка алкоголя...

        Мороль сей басни такова: если вы и решились сувать странный предмет себе в задницу, то тогда и всех мерах безопасности подумаете.

        Помните, дети, анальные потехи хороши, но не так просты и безопасны, как кажутся...

        (Тут могла быть ваша реклама смазки)

        '''

        window hide
         

        pause
        $ MyReturn()()

        return

    label .die:

        window hide

        scene end rui die


        '''Концовка: "Вот и помер наш Руй"

        P.s. нет, это не отпечатся, так и задумано

        В первое вы очень сильно переживали из-за смерти Руи...

        Он героически вытащил ядерку из вашей задницы, убежал из вашего дома, чтобы бомба не навредила вам и по итогу умер сам...

        По истину героический поступок...

        На следующий день вы забыли про Руи и начали встречаться с каким-то папиком.

        Ну и по классике уже...

        '''

        scene black with dissolve

        show end rui die movie with dissolve

        window hide
         

        pause
        $ MyReturn()()

        return

    label .orgia:

        window hide

        scene end rui orgia


        '''Концовка: "С днём полиамории"

        Вы вступили в отношения со всеми из Wonderlands x Showtime сразу...

        Как бы странно это ни выглядило со стороны, но вы действительно счастливы в этих отношениях.

        Ваш быт идеально построен. Вы часто ходите на свидание со всеми сразу или с по отдельности. Вы хорошо провдите время вместе, все друг друга поддерживают. А то, как вы проводите ночь... {w=0.5}это невероятно

        Удивительно, когда такие, как казалось бы, странные вещи могут приносить истинное счастье...

        '''

        window hide
         

        pause
        $ MyReturn()()

        return

    label .happy:

        window hide

        scene end rui happy

        '''"Счастливая концовка!"

        С названием, наверное можно попросить, но тем не менее...

        Вы остались с Руи вместе навсегда и будете действительно счастливы!

        Ваша и его жизнь наладиться по всем фронтам.

        Мечта просто~
        
        '''

        window hide
         
        pause
        $ MyReturn()()

        return

    label .suid:

        window hide

        scene end rui suid

        '''Концовка "Двойное самоубийство?"

        Руи, кажется, осознал, что не сможет заставить вас полюбить его и... сдался.

        Тяжесть ошибки только ухудшило его положение и он не нашёл другого варианта.

        А вы решили последовать за ним... но правильное ли это решение?

        такого конца вы хотели?
        
        '''

        window hide
         
        pause
        $ MyReturn()()

        return

    label .the_end:

        window hide

        scene end rui suid

        '''Концовка "The End"

        Наконец-то все ваши бысчисленные страдания закончены.

        Теперь вы полностью свободны... Больше никакого Руи, никакой ядерки, никаких страданий...

        Вы начнёте жизнь с чистого листа и всё будет хорошо.
        
        '''

        window hide
         
        pause
        $ MyReturn()()

        return

    label .podval:

        window hide

        scene end rui podval

        '''Подвальная концовка.

        Ебанутая хуйня, придуманная за пять секунд до выхода игры.

        Поздравляю, вы попали в мир гача лайф и теперь вам ещё больший пиздец!
        
        '''

        window hide
         
        pause
        $ MyReturn()()

        return

    label .home:

        window hide

        scene end rui suid

        '''Концовка "Переезд"

        Вы переехали к Руи и на удивление его состояние сильно улучшилось.

        Он перестал ревновать вас к каждому столбу и стао действительно заботиться о вас.

        Вы наконец-то пришли с ним к нормальным здоровым отношениям, мои поздравления!
        
        '''

        window hide
         
        pause
        $ MyReturn()()

        return




label secret_end_label:

    label .genran:
        window hide
        scene black


        '''Секретная концовка: "Генератор рандомных чисел"

        Вы решили вместо того, чтобы саморазвиваться и общаться с людьми, сидеть в генераторе рандомных чисел... Вау, поздравляю!

        В конечном итоге от вас отвернулись, даже Руи... Делайте выводы.

        '''

        ks "{glitch=10}Ты действительно доволен этой концовкой?..{/glitch}"

        window hide
         

        pause
        $ MyReturn()()

        return

    label .thank:
        window hide
        scene black


        '''Секретная концовка благодарности

        Я действительно крайне благодарна вам всем за всю поддержку и интерес, который вы проявляете по отношению ко мне и моему творчеству!

        Серьёзно... Эдиты, арты, мемы, озвучка. {w=1}Боже, да год назад я бы ни в жизнь бы не поверила, что это реально!

        Спасибо вам за всё. За то, что просто знаете эту игру.

        Сейчас я одна работаю над игрой. Сюжет, код, поиск нужного материала, MMD - всё на меня. Исключениями являются перевод для английской версией и арты для будующей функцией по смену рисовки.

        Да, в соло работать не просто, но тем не менее, я действительно счастлива создавать эту игру.

        Спасибо за всё. (разработчик игры, ваша NoFanru)

        '''

        window hide
         

        pause
        $ MyReturn()()

        return

    label .name:

        window hide
        scene black


        '''Секретная концовка: "Спасибо, что доводите рассказчика!"

        Ваша гениальность не знает границ!

        Вы таки типо "О, назову ка я себя Руи или Цукасой или вообще Нофом! Ха-ха"

        Мда...

        Я в шоке от вас... Вы довольны получением этой секретной концовки?

        Я даже фон не стал делать для неё...

        ...

        '''

        window hide
         

        pause
        $ MyReturn()()

        return

    label .time:

        window hide
        scene black


        '''Секретная концовка: "[persistent.time_secret]"

        Я всё ещё не знаю почему игра делает то, чего в коде нет. Я связался с Нофанру, она проверила код, ничего связанного с временем там нет...

        Она сказала, что даже не знала о том, что на этом движке можно узнать время игрока.

        Тем не менее сейчас есть переменная в которой хранится информация о времени получении этой концовки.

        '''

        $ minute = persistent.time_secret_list[2]

        $ hour = persistent.time_secret_list[1]

        $ dow = persistent.time_secret_list[0]

        '''

        [persistent.time_secret] в [hour]:[minute], день недели: [dow].

        Кстати, название у этой переменной очень странное... Это "lbjup_jt_xbudijoh". Может быть у вас есть догадки, {i}{b}что это может значить?{/b}{/i}

        В любом случае, мы будем пытаться исправить этот {i}"сдвиг"{/i} в коде.

        '''

        window hide
         
        pause
        $ MyReturn()()

        return

    label .kaito:

        window hide
        scene black

        play sound k_ahaha
        k "Спасибо, за всё~"

        window hide
         
        pause
        $ MyReturn()()

        return
