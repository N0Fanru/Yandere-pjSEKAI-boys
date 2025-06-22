# жёсткий игнор (КОНЦОВКА)
label ignor:
    
    play sound knock2
    queue sound knock3
    queue sound knock1

    p "Пошёл в пизду, Руи-кун!"

    play sound knock1
    queue sound knock1
    queue sound knock1
    queue sound knock1 
    queue sound knock1
    queue sound knock1

    p "..."

    stop sound fadeout 0.5
    stop music fadeout 1.5

    "Спустя время этот еблан успокоился, победа!"

    scene bum

    $ renpy.movie_cutscene ('videos/bumover.webm') 
    
    play music rui_bum fadein 1.0

    scene bg street
    show rui bum

    $ rui_pain_add('1')

    "Блять, кто дал этому еблану пульт от ядерки... {w=2}\nОн обиделся и взорвал ваш дом нахуй."

    "Потом он не выдержит жизни без вас и взорвёт весь город вместе с собой, лол."

    window hide

    call ends_rui("bum") from _call_ends_rui

    pause 5.0

    return


# игрок разделся до трусов 
label trusiki:

    play sound knock2
    queue sound knock2
    queue sound knock3

    "Вам в голову пришла просто наипиздейшая идея раздеться до трусов!"

    play sound undress
    pause 3.0

    p "Хе-хе..."

    scene black with Dissolve(.3)

    pause 1.0

    scene bg corridor with Dissolve(.3)

    pause 0.5

    if persistent.kaito_int > 0 and not persistent.showkaito_rui:

        show rui hello with Dissolve(.3)

        voice k_ja
        show rui likekaito1

        call kaito_list_lable("show") from _call_kaito_list_lable_1

        $ persistent.showkaito_rui = True
    
    else:

        show rui hello with Dissolve(.3):
            xalign 0.5

    show rui hello say at sd

    r "Я...{w=0.3}{nw}"

    show rui shock at sd

    r "..."

    stop music fadeout 1.5

    p "..."
    
    play sound udar
    with hpunch
    show rui angry at sd

    $ rui_pain_add('2')

    p "А!.."

    play music dark fadein 1.5

    r "Живо отвечай: кто тут ещё есть?!"

    p "Руи, я просто..."

    play sound udar2
    with vpunch

    r "С дороги!"

    hide rui with moveoutright

    r "Я зарежу этого подонка, кем бы он ни был!"

    p "Пон..."

    scene bg room
    with Fade(0.3, 0.8, 0.3)

    show rui angry with Dissolve(.3):
        xalign 0.5

    r "Где он? Кто он? {w=0.5}Какого чёрта ты в одних трусах?"

    show rui panic at sd

    r "Тут точно кто-то был."

    menu:

        "[[Промолчать]":

            show rui panic1

            pause 1.5

            show rui angry at sd

            r "Почему ты молчишь?!"

            $ molchun1 = True

        "Руи, я просто...":

            show rui panic1

            p "Руи, я просто хотела тебя удивить..."

            show rui crazy at sd

            r "Ха-ха, думаешь я поверю в эту чушь?"

            show rui angry at sd

            r "Нет... Я давно знал, что что-то в наших отношениях не так."

            $ opravdan1 = True

    r "Он уже ушёл, да?"

    play sound udar 
    with hpunch

    show rui crazy at sd

    $ rui_pain_add('3')

    r "Хаа... {w=0.5}Кто это был? Цукаса? {w=0.3}Вы ведь достаточно хорошо общаетесь, я прав?.."

    show rui crazy2 at sd

    r "Я скину на его дом ядерку!"

    p "Руи!"

    menu:

        "Я разделась ради тебя":

            p "Руи, я разделась ради тебя! {w=0.3}Я думала, ты обрадуешься..."

            if opravdan1:

                show rui angry at sd

                r "Опять ты за своё? Это тупое оправдание."

            else:

                show rui crazy at sd

                r "Ха-ха, думаешь я поверю в эту чушь?"

                show rui angry at sd

                r "Нет... Я давно знал, что что-то в наших отношениях не так."

                r "Такое оправдание со мной не прокатит!"

            p "Руи, ты считаешь меня тупой?"

            r "К чему это?"

            p "А к тому, что если б я действительно решила тебе изменить, то выходя тебя встретить, оделась бы, долбаёб."

            show rui shock at sd

            r "..."

            p "Как мне тебе доказать, что я не вру..."

            p "Мх.. хнык"

            show rui blush at sd

            r "Ладно я тебе верю. "

            show rui blush:
                ease 0.5 zoom 1.5 yalign 0.3

            extend "Но в следующий раз говорю всё прямо..."

            show rui blush:
                zoom 1.5 yalign 0.3

            play sound bed volume 2.5
            with hpunch
            
            p "!!!"

            jump ruisex

        "Откуда у тебя ядерка?":

            jump yaderka  

        "[[Молчать]":

            p "..."

            jump ne_molchi

    return

# игрок молчал (кОНЦОВКА)
label ne_molchi:

    if molchun1:

        show rui angry at sd

        r "Ты снова молчишь? Ну чего же ты..."

    else:

        show rui angry at sd

        r "Почему ты молчишь? Отвечай!"

        r "Что, те твои слова о том, что ты ради меня разделась были ложью?"

    play sound udar
    with hpunch

    $ rui_pain_add('4')

    p "Руи! Не бей меня, мне больно!"

    r "Ооо, теперь заговорила..."

    play sound udar2
    with vpunch

    scene bg ruisex
    show rui udar1
    with Fade(0.3, 0.5, 0.3)

    play sound udar
    with hpunch

    p "Руи! Пожалуйста, прекрати!"

    play sound udar2
    queue sound udar
    queue sound udar2
    queue sound udar

    $ rui_pain_add('5')

    r "Заткнись! Заткнись! Заткнись!" with vpunch

    r "Почему ты молчишь, почему?!"

    p "Руи, ты...{w=0.3}{nw}"

    r "Не желаю больше слышать пустых оправданий..."

    menu:

        "Оправдываться":

            p "Руи, послушай, возникло недоразумение, я-{w=0.3}{nw}"

            r "О, недоразумение, значит? {w=0.2}Так что, хочешь сказать, что ты меня любишь?"

            p "Да..."

            window show

            r "Тогда я заставлю тебя доказать это и сам покажу тебе {sc}{=norm_style}свою любовь.{/sc}"

            play sound udar2 volume 1.3

            scene black with Dissolve(.3)

            jump rui_home_poh

        "Молчать":

            p "..."

    play sound udar2
    with vpunch

    r "Да ты даже не пытаешься оправдаться."

    p "Руи, так мне молчать или гово-{w=0.3}{nw}"

    play sound udar2 volume 1.3

    $ rui_pain_add('6')

    p "А!.."

    scene black with Dissolve(.3)

    p "..."

    pause 1.0

    ks2 "You {swap=wont die.@will die.@1.0}{=norm_style}wont die.{/swap}"

    call kaito_list_lable("die") from _call_kaito_list_lable_2

    $ persistent.showkaito_rui = False
    
    pause 0.7

    call ends_rui("ne_molchi") from _call_ends_rui_1

    pause 5.0

    return

# гг спрашивает откуда у руи пульт от ядерки (КОНЦОВКА)
label yaderka:

    stop music fadeout 1.5
    play music dillema fadein 1.5 volume 0.7

    p "Где ты достал ядерку..."

    show rui sad at sd

    r "Обижаешь..."

    show rui happy at sd

    r "Конечно же я сам сделал!"

    p "Ты сам собрал ядерную бомбу?.."

    show rui hello at sd

    r "Ну да, а что?"

    r "Что ты так смотришь... {w=0.3}Ты сомневалась в моих способностях?"

    p "Нет, просто..."

    menu:

        "Дай мне пульт от ядерки":

            p "Просто дай мне пульт от ядерки."

        "Это меня пугает...":

            jump yaderka_pugaet

    show rui shock at sd

    r "Э?... {w=0.3}Зачем тебе пульт от ядерки?"

    p "Меня всё достало, хочу взорвать весь мир... Я... просто хочу..."

    show rui crazy at sd

    r "Ох, [player_name]... Как я тебя понимаю..."
    show rui crazy2 at sd
    extend "\nРади тебя я готов собрать оружие, которое убьёт всех людей на планете, кроме нас с тобой!"

    r "Я построю собственную ноосферу! Мы ни в чём не будем нуждаться, нас будут обслуживать мои роботы. Они же заменят людей всех профессий. Мы сможем заниматься только тем, чем захотим!"

    r "И никто... {w=1}никто не сможет нам помешать!"

    r "Ох, [player_name]! Моя [player_name]!"

    p "Руи..."

    menu:

        "Это именно то, чего я хочу!":

            p "Это именно то, что мне нужно!"

            show rui happy at sd

            p "Руи! Воплотим же вместе твой план!"

            show rui crazy at sd

            r "[player_name]! Я так тебя люблю! Бесконечно люблю! Совсем скоро мы обретём полное счастье..."

            $ yaderka_true = True

        "Я пошутила...":

            $ haha_add('1')
            
            p "Это была шутка..."

            show rui shock at sd

            r "..."

            show rui angry at sd

            r "Не смей так говорить!"

            play sound udar 
            with hpunch

            play sound udar2 
            with vpunch

            play sound udar 
            with hpunch

            $ rui_pain_add('7')

            p "Руи! Мне больно!"

            play sound udar2 
            with vpunch

            play sound udar 
            with hpunch

            play sound udar2 
            with vpunch

            show rui crazy at sd

            $ rui_pain_add('8')

            r "Нет... Ты ведь врёшь, я прав? Это не может быть правдой.. не может..."

            show rui crazy2 at sd

            r "Ты просто сама ещё не понимаешь, насколько сильно хочешь такого исхода..."

            p "..."

            p "*хнык*"

            show rui crazy at sd

            r "Почему же ты плачешь, [player_name]? {w=1}Ты не хочешь найти своё истинное желание?"

            show rui hello at sd

            r "У тебя нет выбора, [player_name]. У тебя нет выбора."

            r "Скоро ты всё поймёшь, осознаешь..."

            menu:

                "...":

                    p "Ладно..."

                    $ yaderka_ladno = True

                "Нет, я найду способ этого избежать":

                    p "Нет! Я не буду тебя слушать! Я найду способ этого избежать..."

                    play sound udar 
                    with hpunch

                    $ rui_pain_add('9')

                    show rui angry at sd

                    r "Ты не сможешь. {p=0.8}С этого момента всё для тебя решено."

                    p "Пиздец..."

                    play sound udar2 
                    with vpunch

                    $ rui_pain_add('10')

                    p "A!"

                    $ yaderka_sila = True
                
    scene black with dissolve

    pause 0.5

    if yaderka_true:

        if 'true' not in persistent.pr_world:
            $ nn_list = persistent.pr_world
            $ nn_list.append('true')
            $ persistent.pr_world = nn_list
            $ get_ach('pr_world_all')

        "Руи дал вам пульт от ядерки, вы ради эксперимента скинули бомбу на Америку... Это было началом для третьей мировой..."

        "Но Руи сделал то, что обещал... Он изобрёл вирус и искусственные антитела к нему. Антитела, которые генетически подходят только вам двоим."

        "Боясь, что ваша любовь угаснет, Камиширо изобрёл некий препарат, способный вызывать те же реакции в организме, как и при первой любви."

    elif yaderka_ladno:

        if 'ladno' not in persistent.pr_world:
            $ nn_list = persistent.pr_world
            $ nn_list.append('ladno')
            $ persistent.pr_world = nn_list
            $ get_ach('pr_world_all')

        "Руи изобрёл вирус и искусственные антитела к нему. Антитела, которые генетически подходят только вам двоим."

        "По началу вы плакали из-за происходящего, но позже смирились."

        "Кажется, Руи подмешивал что-то вам в еду, а может быть вам всего лишь приснилось..."
        
        "Со временем вы поняли, что полностью поддерживаете его план."

    elif yaderka_sila:

        if 'sila' not in persistent.pr_world:
            $ nn_list = persistent.pr_world
            $ nn_list.append('sila')
            $ persistent.pr_world = nn_list
            $ get_ach('pr_world_all')

        "Вы не смогли найти способ избежать того, про что говорил Руи..."

        "В тот день он вас вырубил и увёз к себе в подвал. Вы там пробыли несколько месяцев..."

        "Руи давал вам вкусную еду, предоставил все удобства, покупал всё, о чём вы могли бы его попросить, но не разрешал вам покидать подвал."

        "Однажды он воткнул в вас какое-то странное вещество, вы до сих не уверенны, что это было..."

        "После этого вы стали буквально одержимы Камиширо и были согласны с его планом..."

        "Руи изобрёл вирус и искусственные антитела к нему. Антитела, которые генетически подходят только вам двоим."

    scene end rui yaderka with dissolve

    "Спустя год, всё человечество вымерло. {p=0.5}К этому времени Руи уже автомизировал весь ваш быт с помощью своих роботов."

    "Руи смог изобрести зелье бессмертия..."

    "Теперь вам двоим ничего не угрожает."

    "Вы будете счастливы вместе навечно... {w=1}До тех пор, пока существует эта вселенная, будет существовать и ваша любовь"

    window hide

    call ends_rui("yaderka") from _call_ends_rui_2

    pause 5.0

    return

# игрок говорит, что ядерка пугает
label yaderka_pugaet:

    p "Это меня пугает..."

    r "Ха-ха... {w=0.5}Со мной шутки плохи, как видишь~"

    p "..."

    p "(Мне стало как-то слишком тревожно...)"

    r "..."
    r "....."
    r "........."

    $ get_ach('...')

    p "..."

    show rui angry at sd

    r "Так.... {w=0.2}Почему ты в одних трусах?"

    p "А, это..."

    menu:

        "В одежде дрочит неудобно":
            
            p "В одежде дрочить неудобно, знаешь ли."

            show rui shock at sd

            r "А?.."

            p "Я дрочила, думая о тебе, дурень..."

            show rui blush at sd

            $ lie_add('1')

            r "Ты могла бы просто попросить."

            show rui blush:
                ease 0.5 zoom 1.5 yalign 0.3

            r "..." 

            show rui blush:
                zoom 1.5 yalign 0.3

            play sound bed volume 2.5
            with hpunch
            
            p "!!!"

            jump ruisex

        "Я разделась ради тебя":
            
            p "Руи, я разделась ради тебя! {w=0.3}Я думала, ты обрадуешься..."

            if opravdan1:

                show rui angry at sd

                r "Опять ты за своё? Это тупое оправдание."

            else:

                show rui crazy at sd

                r "Ха-ха, думаешь я поверю в эту чушь?"

                show rui angry at sd

                r "Нет... Я давно знал, что что-то в наших отношениях не так."

                r "Такое оправдание со мной не прокатит!"

            p "Руи, ты считаешь меня тупой?"

            r "К чему это?"

            p "А к тому, что если б я действительно решила тебе изменить, то выходя тебя встретить, оделась бы, долбоящер."

            show rui shock at sd

            r "..."

            p "Как мне тебе доказать, что я не вру..."

            p "Мх.. хнык"

            show rui blush at sd

            r "Ладно я тебе верю."

            show rui blush:
                ease 0.5 zoom 1.5 yalign 0.3

            r "Хм?"

            show rui blush:
                zoom 1.5 yalign 0.3 

            play sound bed volume 2.5
            with hpunch
            
            p "!!!"

            jump ruisex

        "[[Молчать]":

            p "..."

            jump ne_molchi

    return

# постельная сцена 1
label ruisex:

    scene bg ruisex with Fade(0.3, 0.8, 0.3)

    stop music fadeout 1.5

    show rui s normal with Dissolve(.3)

    play music sexmusic fadein 1.5 volume 0.1

    pause 1.5

    p "..."

    p "Руи..."

    show rui s normal:
        "rui s crazy" with Dissolve(.1)

    r "Чш.. ты ведь именно этого хотела?"

    p "Я..."

    play sound bed volume 2.5
    with hpunch

    show rui s zcrazy with Dissolve(.1)

    pause 0.3

    p "Ах!"

    show rui s zcrazy:
        "rui s znormal" with Dissolve(.1)

    r "Спокойно, я буду осторожен..."

    p "..."

    menu:

        "А у тебя есть презерватив?":

            p "А у тебя есть презерватив?..."
 
            r "Хи-хи... Не бойся, я всегда его с собой беру, когда иду увидеться с тобой."

            r "Мне тоже лишние проблемы не нужны, знаешь ли."

            p "Хорошо..."

        "Мне страшно...":

            p "Мне страшно... {w=0.5}Это мой первый раз."

            r "Не бойся, всё будет хорошо, я обещаю."

            show rui s znormal:
                "rui s zcrazy" with Dissolve(.1)

            r "Я буду осторожен. Я сделаю всё, чтобы ты смогла получить максимум удовольствия~"

            show rui s zcrazy:
                "rui s znormal" with Dissolve(.1)

            r "И можешь не переживать насчёт предохранения, я взял презерватив с собой."

            p "М..."

        "Не останавливайся":

            p "Не смей останавливаться..."

            r "И в мыслях не было."

            $ rui_ebi += 1

        "Пожалуйста, перестань...":

            p "Руи! Пожалуйста, перестань..."

            show rui s znormal:
                "rui s sad" with Dissolve(.1)

            r "Чшшш... {w=0.3}Не говори так... {w=0.5}Не говори так..."

            show rui s sad:
                "rui s znormal" with Dissolve(.1)

            $ rui_ne_ebi += 1

    p "!!!"

    show rui s znormal:
        "rui s zcrazy" with Dissolve(.1)

    r "М?.."

    p "(У него, кажется, встал?..)"

    r "Как видишь пути назад нет."

    show rui s zcrazy:
        "rui s droch1" with Dissolve(.1)

    p "А, ээ..."

    show sex rui1:
        zoom 0.0 alpha 0.0 xalign 0.80 yalign 0.35 anchor (0.5, 0.5)
        ease 0.4 zoom 0.65 alpha 1.0 xalign 0.80 yalign 0.35 anchor (0.5, 0.5)
        ease 0.1 zoom 0.6 alpha 1.0 xalign 0.80 yalign 0.35 anchor (0.5, 0.5)

    p "Руи!"

    show rui s droch1:
        "rui s droch2" with Dissolve(.1)

    r "Тебе нравится, [player_name]?"

    p '''Ахх... {w=0.3}Я.. {w=0.3}Мх..

    ...

    (Он слишком сильно водит пальцами... Кажется, я уже водопад...)

    Руи...

    '''

    menu:

        "...":

            p "М..."

            r "Ну же, [player_name], не молчи."

            $ molchun += 1

            menu:

                "Я не знаю, что говорить...":

                    p "А что говорить-то, ну, э.. ху..."

                    show rui s droch2:
                        "rui s droch1" with Dissolve(.1)

                    r "Хм?.. {w=0.5}Хорошо, постарайся просто расслабиться и получать удовольствие~"

                "Мне очень нравится":

                    p "Мне очень нравится, Руи, продолжай..."

                    show rui s droch2:
                        "rui s droch1" with Dissolve(.1)

                    r "Хе-хе, я очень рад~"

                    $ rui_ebi += 1

                "Давай перейдём уже к более интересной части":

                    p "Давай перейдём уже к более интересной части~"

                    show rui s droch2:
                        "rui s droch1" with Dissolve(.1)

                    r "М? Ты уверена?"

                    p "Да..."

                    r "Я конечно очень ценю твоё рвение, но знаешь, нужно и прелюдиями уметь наслаждаться."

                    $ rui_ebi += 2

                "Давай на этом закончим?..":

                    p "Давай уже закончим, Руи..."

                    show rui s droch2:
                        "rui s droch1" with Dissolve(.1)

                    r "Ха?.. {w=0.5}Не бойся, милая, всё будет хорошо, тебе точно понравится."

                    p "Но я..{w=0.3}{nw}"

                    r "Чш!"

                    $ rui_ne_ebi += 1

                "Прекрати!":

                    p "Прекрати сейчас же, Руи!"

                    show rui s droch2:
                        "rui s droch1" with Dissolve(.1)

                    r "Чшш... не кричи ты так."

                    p "Руи, я серьёзн-{w=0.2}{nw}"

                    p "Ах! {w=0.3}Чёрт, ты..."

                    $ rui_ne_ebi += 2

        "Мне очень нравится":

                p "Мне очень нравится, Руи, продолжай..."

                show rui s droch2:
                    "rui s droch1" with Dissolve(.1)

                r "Хе-хе, я очень рад~"

                $ rui_ebi += 2

        "Давай перейдём уже к более интересной части":

            p "Давай перейдём уже к более интересной части~"

            show rui s droch2:
                "rui s droch1" with Dissolve(.1)

            r "М? Ты уверена?"

            p "Да..."

            r "Я конечно очень ценю твоё рвение, но знаешь, нужно и прелюдиями уметь наслаждаться."

            $ rui_ebi += 3

        "Давай на этом закончим?..":

            p "Давай уже закончим, Руи..."

            show rui s droch2:
                "rui s droch1" with Dissolve(.1)

            r"Ха?.. {w=0.5}Не бойся, милая, всё будет хорошо, тебе точно понравится."

            p "Но я.."

            r "Чш!"

            $ rui_ne_ebi += 2

        "Прекрати!":

            p "Прекрати сейчас же, Руи!"

            show rui s droch2:
                "rui s droch1" with Dissolve(.1)

            r "Чшш... не кричи ты так."

            p "Руи, я серьёзн-{w=0.2}{nw}"

            p "Ах! {w=0.3}Чёрт, ты..."

            $ rui_ne_ebi += 3

    p "..."

    p "Мх.. {w=0.1}Руи... {w=0.5}Ах, Руи... {w=0.3}Руи..."

    hide sex with Dissolve(0.3)
    pause 0.2
    show rui s droch1:
        "rui s znormal" with Dissolve(.1)

    p "..."

    p "Что ты..."

    play sound undress
    scene bg ruisex2 
    show rui s hop1
    with Fade(0.3, 2.0, 0.3)
    
    p "..."

    p ''' Э?{w=0.5}{nw}

    Э?...{w=1.5}{nw}

    Ээээээ?! 
    
    '''

    p "Ох..."

    menu:

        "...":

            p "..."

            r "Всё в порядке? Я продолжаю?"

            p "Да, давай..."

            $ molchun += 1

        "Продолжай":

            p "Чёрт, Руи не останавливайся, я тебя прошу!"

            p "Ты ведь собираешься войти, да? Давай быстрее..."

            r "Хе-хе~"

            $ rui_ebi += 1

        "[[Пнуть]":

            show rui s hop1:
                "rui s hop2" with Dissolve(.1)
            
            r "Не дёргайся ты так, всё ж хорошо~"

            p "(Чёрт... Я не могу ногой пошевелить, он слишком сильный)"

            p "Руи, пожалуйста, прекрати..."

            show rui s hop2:
                "rui s hop1" with Dissolve(1.)

            r "..."

            p "Эй, фиолетовая залупа, не игнорируй меня!"

            $ rui_ne_ebi += 2

    show rui s hop1:
        "rui s droch3" with Dissolve(.1)
    
    r "М?"

    p "!!!"

    r "Не тут... {w=1}А если..."

    p "..."

    p "М.. Ах!"

    r "Ага!"

    show rui s droch3:
        "rui s droch4" with Dissolve(.1)

    r "Я нашёл твою точку G..."

    p "Я..."

    show rui s droch4:
        "rui s 1234" with Dissolve(.1)

    p "..."

    r "Ты готова?"

    play sound zip
    show rui s 1234:
        "rui s 1dick" with Dissolve(.1)

    pause 1.0

    p "Ох..."

    menu:

        "...":

            r "Ничего не скажешь?"

            p "..."

            r "Ладно, привыкай, я постепенно начну действовать."

            $ molchun += 1

        "Вставляй побыстрее Руи-младшего":

            p "Вставляй уже Руи-младшего побыстрее!"

            r "Ха-ха, как скажешь."

            $ rui_ebi += 2

        "Руи, прекрати, это уже не смешно!":

            p "Руи хватит, я не шучу!"

            r "Чш... Ты ведь не в серьёз? Я уверен, тебе понравится."

            p "Нет, Руи, я не хочу! Не сейчас."

            r "..."

            p "Ты собираешься сделать это против моей воли? Знаешь, вообще-то это-{w=0.2}{nw}"

            play sound udar
            with hpunch

            $ rui_pain_add('42')

            r "Чшшш, всё в порядке."

            $ rui_ne_ebi += 1

    scene bg ruisex
    show rui s droch1
    with Dissolve(0.3)

    r "Так.. Эту позу сегодня ты уже видела..."

    p "..."

    play sound gandom

    "Вы слышите, как Руи шуршит упаковкой от презерватива."

    r "Что ж, приступим?~"

    p "..."

    "Вы чувствуете, как Руи начал тереться головкой своего члена об вашу промежность."

    menu:

        "Вставляй уже побыстрее, Руи!":

            p "Руи! Вставляй побыстрее, я больше уже не могу терпеть"

            r "Чшш, не спеши ты так, всё же, доминирую тут я."

            $ rui_ebi += 1

        "...":

            p "Мх..."

            r "..."

            r "Я вставляю."

            $ molchun += 1

        "Пожалуйста, Руи, остановись...":

            p "Руи, прошу тебя остановись..."

            r "..."

            p "Не игнорируй меня... {w=0.5}Ну пожалуйста!"

            r "Я вставляю."

            p "Руи! Остановись, еблан!"

            r "..."

            $ rui_ne_ebi += 1

            if rui_ne_ebi < 5:
                $ get_ach('smir')

            menu:

                "Смириться":

                    p "Почему ты так поступаешь..."

                    $ rui_ne_ebi += 1

                "Сопротивляться" if rui_ne_ebi >= 5:

                    jump rui_iznos

    p "М.. Ах.."

    "Вы чувствуете, как член Руи медленно входит в вас, его движения очень осторожны."

    "Вставив наполовину парень остановился, давая вам привыкнуть к ощущению его пениса внутри"

    p "Ах.. мх..."

    "Вы чувствуете как сердце начинает бешено колотиться."

    show rui s droch1:
        "rui s end1" with Dissolve(.1)

    r "Тебе нравится, [player_name]?"

    p "М..."

    "Наконец, Руи вставил член полностью и начал медленно двигаться. {p=1.0}Ваше тело начинает гореть, наполняясь приятными ощущениями внутри."

    if rui_ebi > molchun and rui_ebi > rui_ne_ebi:

        p "Руи... Ах, Руи... Сильнее, пожалуйста!"

        "Дальше все воспоминания смешались, но никогда никуда не уйдут из вашей головы..."

        scene end rui ebi with Dissolve(.3)

        "Вы помните невероятный оргазм, множества поз, безумное лицо Руи, которое тогда казалось вам особенно привлекательным."

        "Вы помните, как страстно извивались под ним, как просили быть грубее, как Руи вечно повторял насколько сильно любит вас и каждый сантиметр вашего тела."

        "Это было незабываемое утро, которые вы повторите с ним ещё не раз."

        "Если вам надоест секс, Руи найдёт способ вновь перенести вас на седьмое небо и испытать оргазм как в первый раз."

        $ rui_horny_add('1')

        "Этот парень безумный. И вы навечно влюблены в него."

        window hide

        pause 0.5

        call ends_rui("ebi") from _call_ends_rui_3

        pause 5.0


    elif rui_ne_ebi > rui_ebi and rui_ne_ebi >= molchun:

        $ rui_pain_add('43')

        p "Я тебя ненавижу, Руи..."

        "Вы действительно не хотели заниматься сексом с Руи, но вы не могли ему противостоять. {w=0.5}Нет, не могли, только ни зная на что он способен."

        "Вы тихонько хныкали, пока Руи делал своё дело"

        "Лицо парня выражало чистое безумие... {w=1}Вы хотели бы забыть это..."

        scene end rui ne_ebi with fade

        $ rui_horny_add('2')

        "Вы навечно обречены быть в отношениях с Руи, вы навечно обречены заниматься с ним сексом."

        window hide

        pause 0.5

        call ends_rui("ne_ebi") from _call_ends_rui_4

        pause 5.0

    else:

        p "..."

        "Вы молчали остаток секса, в то время как Руи тихонько стонал. Его лицо полыхало красным, на нём читалось безумие и блаженство."

        "В конечном итоге, вы можете сказать, что вам понравилось. {w=1}Этот парень действительно всегда сможет найти способ удовлетворить девушку."

        "Вы ничего не говорили ему, не подсказывали в каком направлении стоит двигаться. {w=1}Но он сам нашёл все нужные точки на вашем теле и смог доставить вам удовольствие."

        "Когда Руи попросит вас повторить, вы будете ломаться, но в итоге согласитесь и останетесь довольны."

        $ rui_horny_add('3')

        "Со временем ваша похотливая сторона возьмёт над вами верх и вы сами начнёте просить парня отрахать вас во все щели, так что б соседи во всём доме просто ахуели."

        window hide

        pause 0.5

        call ends_rui("molchun_ebka") from _call_ends_rui_5

        pause 5.0


    return

# сопративление, износилование (КОНЦОВКА)
label rui_iznos:

    p "Руи, прекрати, сейчас же!"

    play sound udar

    r s sad "А..."

    p "..."

    r "Ты меня ударила?"

    p "Я.."

    play sound udar 
    with hpunch

    play sound udar2 
    with vpunch

    play sound udar 
    with hpunch

    $ rui_pain_add('11')

    p "A!"

    show rui s sad:
        "rui s zcrazy" with Dissolve(.1)

    r "Ты совсем спятила?! {w=0.5}Не смей мне перечить!"

    p "Но, Руи, я.."

    play sound udar 
    with hpunch

    play sound udar2 
    with vpunch

    play sound udar 
    with hpunch

    $ rui_pain_add('12')

    p "Мне больно, Руи..."

    r s end2 "Заткнись и не мешай мне..."

    p "A!"

    p "Руи, блять, перестань, я не хочу!"

    r "Заткнись!"

    play sound udar 
    with hpunch

    $ rui_pain_add('13')

    "Дальше было всё как в тумане..."

    scene end rui iznos with Dissolve(.1)

    "Вы помните, что очень сильно плакали и умоляли Руи остановиться, в ответ на это Руи или игнорил или бил вас."

    "В тот день вы просто возненавидели его и свою судьбу, которая связала вас с ним."

    $ rui_horny_add('4')

    "Что же вам делать дальше... Любые попытки принять меры он всегда останавливал... Есть ли надежда?"

    window hide

    pause 0.5

    call ends_rui("iznos") from _call_ends_rui_6

    pause 5.0

    return