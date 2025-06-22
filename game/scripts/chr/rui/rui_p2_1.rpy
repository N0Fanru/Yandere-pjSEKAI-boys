# Руи похищает гг (+-)
label rui_home_poh:

    $ rui_state = 80
    $ kaito_state = 100
    play sound2 wake
    stop music fadeout 1.0
    window hide
    pause 6.1

    window show

    p "..."

    p "А?.."

    scene bg rui living room 
    show blank at blink_no_open_more

    "Вы несколько раз моргаете, пытаясь сообразить где находитесь и что произошло."

    p "Мх... голова... пиздец..." 

    noc "[player_name]?"

    play music doomed fadein 5.0 volume 0.6

    "Вы слышите знакомый голос... {w=1}Это был Руи. По ощущениям ваша голова лежит у него на коленях."

    r "Ох, [player_name], ты проснулась~"

    r "Не волнуйся, всё в порядке, я не причиню тебя вреда... {w=0.5}Я просто... {w=0.2}хочу показать тебе, что я действительно тебя люблю."

    if rui_psyho:
        r "Даже если ты считаешь меня психом или типо того, я смогу доказать тебе обратное."

    r "Нашей любви ничто не помешает, [player_name]."

    "Вы хотели что-то сказать, но вместо этого смогли лишь издать несколько звуков."

    r "Ох, тебе сейчас тяжело говорить, не утруждай себя. {w=0.5}Я не хотел, чтобы ты испытывала сильный страх, поэтому вколол тебе кое-что."

    r "Давай я тебе сейчас принесу воды, это поможет тебе проснуться."

    show blank at blink4 zorder 10

    "Руи осторожно приподнимает вашу голову, заставляя вас принять сидячее положение, встаёт и уходит из комнаты."

    stop music fadeout 5.0

    "Ваш разум сейчас затуманен, мышление заторможено, но вы пытаетесь хоть немного оценить весь пиздец, в котором оказались."

    "Судя по всему, вы находись дома у Руи. К счастью (или к сожалению?), не в его подвале."

    show blank at blink5

    "Вы делаете глубокий вдох, пытаясь прийти в чувства."

    play music sad_nervis fadein 4.0 volume 0.25

    show blank at blink_open

    "Вы начинаете постепенно осознавать всю ситуацию целиком... {w=0.5}Руи действительно вырубил и похитил вас!"

    $ mind_value = 600
    $ old_mind_value = 600
    $ persistent.showmindebart = 'blink'

    "Похоже, подобное положение слишком сильно влияет на ваш {b}рассудок{/b}. "

    show screen mind_bar_screen
    
    extend "Следите за своим ментальным состоянием по {b}индикатору{/b} в левом верхнем углу."

    $ persistent.showmindebart = 'none'

    pause 0.05

    $ mind(150)

    "Из-за {b}низких значений{/b} рассудка у вас может ухудшиться восприятие мира, а также повыситься вспыльчивость и эмоциональность."

    $ mind(900)

    "Однако из-за {b}слишком высоких значений{/b} вы начнёте чувствовать себя слишком комфортно и ваша бдительность и внимательность сильно упадут."

    $ mind(600)

    "Низкие и слишком высокие значения рассудка напрямую влияют на то, как вы можете повести себя в той или иной ситуации, иногда полностью лишая вас выбора."

    "Старайтесь держаться чуть выше середины. Безопасной зоной является значения {b}от 450 до 750{/b}. {w=1.0}Чем дальше вы находитесь от безопасной зоны, тем сильнее эффект."

    $ mind(1000)

    "Если вы добрались до {b}высокого экстремального значения{/b} (1000), ваш рассудок больше не измениться."

    $ mind(0)

    "На {b}низком экстремальном значении{/b} (0) вы полностью потеряете себя как личность и кто знает, что произойдёт дальше..."

    $ mind(600)

    # ачивка рассказчик

    "Рассудок меняется в зависимости от того, что происходит вокруг вас. {w=0.5}В то время как на вещи происходящее вокруг влияет ваш выбор в игре..."

    $ s4_add('7')

    $ mind_can_lose = True

    stop music fadeout 3.0

    r "[player_name]..."

    play music doomed fadein 5.0 volume 0.6

    show rui nc cup zorder 2 with Dissolve(.2)
    "Руи вернулся со стаканом в руке, вы смотрите на него всё ещё пустым взглядом."

    show rui nc cup sad at sd 

    r "Ох, неужели я переборщил с дозировкой... Это нехорошо..."

    show rui nc cup1 at sd

    r "Попей воды, это поможет препарату быстрее выйти из твоего организма."

    "Руи подносит стакан с водой к вашим губам, без лишних размышлений вы начинаете жадно пить воду."

    window hide

    play sound drink volume 1.8

    pause 2.3

    show rui nc cup at sd 

    window show

    r "Вот так, скоро тебе станет легче, не переживай."

    show rui nc hello at sd

    "Руи ставит пустой стакан на стол и смотрит на вас."

    r "Как ты себя чувствуешь сейчас? Знаешь, ты спала гораздо дольше, чем я рассчитывал..."

    menu:

        "[[Промолчать]":

            p "..."

            show rui nc shock at sd

            r "[player_name]..."

            show rui nc sad at sd

            r "Ладно, я понимаю, тебе должно быть тяжело сказать что-либо..."

            r "В любом случае, {nw}"

        "Мне лучше":

            $ rui_state += 5

            p "Мне уже лучше..."

            r "Я рад это слышать... {w=0.5}Не волнуйся, всё будет в порядке, я обещаю."

            r "[player_name], {nw}"

        "Как я могу быть в порядке?":

            $ rui_state -= 10

            p "Как я могу быть в порядке, Руи?"

            show rui nc sad at sd

            r "..."

            $ mind(150, "-")

            p "Ты чёртов психопат, раз решил меня похитить! {w=0.3}{nw}" with hpunch
            extend "Я ненавижу тебя!" with hpunch

            show rui nc shock at sd

            r "[player_name]! Успокойся!"

            show rui nc hello say at sd

            r "Я не собираюсь причинять тебе вред. Я лишь хочу показать тебе насколько счастливой ты можешь быть со мной..."

            show rui nc hello at sd

            p "Какого хуя, Руи... почему... Просто почему..."

            show rui nc sad at sd

            "Вы начинаете тихо хныкать, понимая в насколько безвыходной ситуации вы оказались."

            "Вот что вы можете сделать против на голову больного ублюдка сейчас?"

            r "[player_name]..."

            show black zorder 10:
                alpha 0.0
                linear 0.3 alpha 1.0

            "Руи обнимает вас, поглаживая по спине и пытаясь утешить."

            show black zorder 10:
                alpha 1.0

            menu:

                "[[Позволить обнимать дальше]":

                    $ mind(50, "+")

                    r "Всё хорошо, [player_name]. Я понимаю насколько это стресс для тебя, но..."

                    r "Но... {w=0.5}Но это для твоего же блага{w=0.3}, просто..{w=0.2} поверь мне..."

                    $ rui_state += 12

                    "Вы начинаете постепенно успокаиваться и Руи отпускает вас."

                    show black:
                        linear 0.3 alpha 0.0

                    r "Вот так лучше..."

                    hide black

                    show rui nc hello at sd

                    r "Знаешь, {nw}"

                "[[Отолкнуть]":

                    $ rui_state -= 10

                    show black:
                        linear 0.3 alpha 0.0

                    show rui nc shock at sd

                    "Вы пинаете Руи, желая, чтобы он держался как можно дальше от вас."

                    p "Не прикасайся ко мне! Как ты вообще можешь вести себя, будто ты не сделал ничего плохого... {w=0.3}{nw}"
                    extend "Мне мерзко от тебя!" with vpunch

                    show rui nc sad at sd

                    r "[player_name]..."

                    "Вы вытеряете свои слёзы и сурово смотрите на Руи."

                    p "Что тебе сейчас надо?"

                    r "... {nw}"

    # руи: 85 60 рассудок: 600 450

    extend "ты действительно слишком долго спала. {w=0.3}Для восстановления тебе нужно поесть."

    "Вы смотрите на Руи, желая что-то сказать, но не успеваете, так как он берёт вас на руки и тащит на кухню."

    stop music fadeout 1.0

    window hide

    scene black with Dissolve(.3)

    play sound steps

    pause 2.2

    stop sound

    scene rkitchen1 with Dissolve(.3)

    play music kitchen volume 0.7 fadein 3.0

    pause 0.5

    if persistent.low == 2:
        scene rkitchen2-1 with Dissolve(.3)
    else:
        scene rkitchen2 with Dissolve(.3)
    
    window show

    "Руи сажает вас, а сам устраивается по другую сторону стола, внимательно смотря на вас."

    r "Твой организм сильно истощён..."

    if persistent.low == 2:
        show rkitchen2-1:
            "rkitchen3-1" with Dissolve(.2)
    else:
        show rkitchen2:
            "rkitchen3" with Dissolve(.2)

    extend " Поэтому, открой рот, я тебя покормлю."

    menu:

        "[[Открыть рот]":

            $ rui_state += 5

            $ mind(100, "+")

            "Вы открываете рот, позволяя Руи накормить вас. Карри на вкус удивительно вкусный."

            if persistent.low == 2:
                show rkitchen3-1:
                    "rkitchen7-1" with Dissolve(.1)
            else:
                show rkitchen3:
                    "rkitchen7" with Dissolve(.1)

            r "Какая хорошая девочка~"

            "Руи заботливо кормит вас, опустошая всю тарелку."

        "[[Не открывать]":

            $ rui_state -= 5

            "Ага, конечно, размечтался, вы его хорошо знаете... вот откроете рот сейчас, а вместо ложки у вас во рту окажется его хуй и будете вместо карри есть сперму с сахаром."

            if persistent.low == 2:
                show rkitchen3-1:
                    "rkitchen4-1" with Dissolve(.1)
            else:
                show rkitchen3:
                    "rkitchen4" with Dissolve(.1)

            r "[player_name], открой рот."

            p "..."

            r "Я в любом случае тебя накормлю, но если ты сама не откроешь рот, то мне придётся сделать это более мерзким способ, который тебе не понравится."

            r "Даю тебе последний шанс."

            menu:

                "[[Открыть рот]":

                    $ rui_state += 2

                    if persistent.low == 2:
                        show rkitchen4-1:
                            "rkitchen3-1" with Dissolve(.1)
                    else:
                        show rkitchen4:
                            "rkitchen3" with Dissolve(.1)

                    "Вы неохотно открываете рот, к удивлению, во рту у вас не оказался хуй, а оказалась ложка с карри."

                    if persistent.low == 2:
                        show rkitchen3-1:
                            "rkitchen7-1" with Dissolve(.1)
                    else:
                        show rkitchen3:
                            "rkitchen7" with Dissolve(.1)

                    r "Вот, другое дело, [player_name]."

                    "Руи скармливает вам всю тарелку."

                "[[Не открывать]":

                    stop music

                    "Вы по-прежнему не открываете свой рот."

                    if persistent.low == 2:
                        show rkitchen4-1:
                            "rkitchen5" with Dissolve(.1)
                    else:
                        show rkitchen4:
                            "rkitchen5" with Dissolve(.1)

                    "Руи вздыхает и начинает набирать в свой рот карри... Он не глотает его..."

                    if persistent.low == 2:
                        show rkitchen5:
                            "rkitchen6-1" with Dissolve(.1)
                    else:
                        show rkitchen5:
                            "rkitchen6" with Dissolve(.1)

                    "Набрав полный рот карри, он серьёзно смотрит на вас. {w=1}Вам не нравится этот взгляд..."

                    show blank at blink_close

                    play music stress fadein 6.0

                    "Неожиданно он наклоняется к вам, силой открывает руками вам рот и прижимает свои губы к вашим, проталкивая карри языком из вам в рот."

                    "Вы чувствуете отвратительную текстуру слегка пережёванной еды, обмоченной чужой слюной, и шершавого языка Руи, который то и дело соприкасается с вашим языком."

                    $ rui_pain_add("44")
                    
                    "Это так мерзко! Вас начинает тошнить от этого вкуса и чавкающего звука."

                    $ mind(200, "-")

                    "Боже, за что вам это... {w=1}Вы пытались сопротивляться и не глотали еду, но в конечном итоге её стало слишком много и вы сдались, глотая порцию, которая была у Руи во рту."

                    show blank at blink_open_more

                    "Вы открываете свои слегка намокшие глаза и смотрите на Руи."

                    if persistent.low == 2:
                        show rkitchen6-1:
                            "rkitchen8-1" with Dissolve(.1)
                    else:
                        show rkitchen6:
                            "rkitchen8" with Dissolve(.1)

                    r "Ну, теперь ты откроешь рот самостоятельно?"

                    menu:

                        "Да":

                            stop music

                            p "Да, прости..."

                            play music kitchen fadein 2.0

                            "Руи молча скармливает вам остатки карри из тарелки."

                        "Нет":

                            p "Убейся своей ядеркой, я не буду есть твою еду!"

                            if persistent.low == 2:
                                show rkitchen8-1:
                                    "rkitchen9-1" with Dissolve(.1)
                            else:
                                show rkitchen8:
                                    "rkitchen9" with Dissolve(.1) 

                            r "Чёрта с два, я заставлю тебя ещё пожалеть об этом!"

                            "Руи снова набирает полный рот карри, но в этот раз тщательно жуёт его, но так же не глотает."

                            show blank at blink_close zorder 3

                            "Он вновь притягивает вас к себе и выталкивает еду из своего рта в ваш."

                            $ mind(150)

                            "В этот раз текстура ещё более отвратительная: пережёванные куски мяса, смешанные с бульоном от карри и слюной Руи."

                            "Не давая вам и секунды передыха, он снова отстраняется, быстро наполняет свой рот, пережёвывает и снова прижимает свой рот к вашему, проталкивая еду."

                            "Он делает это снова {w=0.3}и снова... {w=0.3}и снова... {w=0.3}и снова..."

                            "Вы плачете, пытаясь хоть как-то оттолкнуться от Руи и понимая, что еды становится во рту слишком много и вы не успеваете глотать..."

                            $ mind(30)

                            "Эта мерзкая смесь лезет наружу из вашего рта, вы задыхаетесь, стараясь дышать, но карри заполняет ваши ноздри."

                            show rkitchen zorder 2

                            "Блять, какого чёрта! Это уже слишком для вас!"

                            show blank at blink_open_more zorder 3

                            "Руи отходит от вас, позволяя консистенции из еды и слюны капать с вашего лица на стол и пол."

                            stop music fadeout 2.0

                            "Вы смотрите на это с отвращением и плачем... {w=0.5}Как же вы всё это ненавидите, почему только..."

                            $ mind(0)

                            pause

    show rkitchen with Dissolve(.2)

    # руи: 90 55 рассудок: 700 250

    "После этого он встаёт из-за стола, кладя тарелку и ложку в раковину, и,{nw}"

    if rui_state >= 80:
        extend " нежно взяв вас за руку, {nw}"
    else:
        extend " схватив вас за руку, {nw}"

    extend "повёл вас обратно в зал."

    stop music fadeout 0.7

    window hide

    scene black with Dissolve(.3)

    play sound steps

    pause 2.2

    stop sound

    scene bg rui living room 
    show rui nc hello
    with Dissolve(.3)

    pause 0.3

    window show

    "Руи сажает вас на диван и смотрит на вас добрым взглядом."

    play music rui_home fadein 3.0 volume 0.7

    r "[player_name], ты ведь понимаешь, что теперь твоя жизнь полностью изменится? {w=0.3}Тебе нужно немного времени, но вскоре ты полюбишь свою новую жизнь."

    r "Теперь тебе больше не нужно делать все бытовые вещи. {w=0.2}Уборка, {w=0.2}готовка, {w=0.2}учёба, {w=0.2}работа, {w=0.2}закупки... {w=1}Я всё буду делать за тебя."

    show rui nc crazy2 at sd

    r "Ты можешь целыми днями сидеть за компьютером или заниматься только тем, что тебе нравится. Тебе даже на улицу нет смысла выходить!~"

    show rui nc crazy1 at sd

    $ config.menu_include_disabled = True

    r "Разве это не жизнь мечты, [player_name]?"

    menu:

        "Ты больной...":

            $ mind(50, "-")

            show rui nc sad at sd

            p "Пиздец ты конченый, кому вообще понравится эта идея? Тебе точно нужно психологическая помощь. Отпусти ме-{w=0.2}{nw}"

            show rui nc happy at sd

            play sound udar
            with vpunch
            $ rui_state -= 5

            $ rui_pain_add("45")

            r "Чшш... Не бунтуй, [player_name]. {w=0.5}Я понимаю, что по началу может быть сложно, но вскоре ты свыкнешься."

        "Прикольнинько" if mind_value > 400:

            $ rui_state += 5

            p "Класс, супер, прикольно."

            show rui nc blush at sd

            r "[player_name]... {w=0.2}Я люблю тебя... {w=0.4}Очень сильно..."

        "...":

            p "..."

            show rui nc sad at sd

            "Руи тяжело вздыхает и смотрит на вас грустным взглядом."

    # руи: 95 50 рассудок: 700 200

    hide rui with Dissolve(.2)

    stop music fadeout 3.0

    "Он садится рядом с вами и начинает чикать каналы на телевизоре."

    if not persistent.tv_rui:
        $ _dismiss_pause = False

    window hide

    hide screen quick_menu
    hide screen mind_bar_screen
    $ quick_menu = False
    with Dissolve(.3)

    pause 0.4

    show screen block_scr(persistent.tv_rui, 15)
    $ renpy.movie_cutscene ('videos/tv rui1.webm')

    if persistent.low == 0:
        play music tv_ads volume 0.5
        scene tv rui3mv
    else:
        scene tv rui2

    $ quick_menu = True
    show screen quick_menu
    show screen mind_bar_screen
    with Dissolve(.3)

    window show

    r "Ах, по телевизору совсем ничего интересного нет...{w=0.3}{nw}"

    if persistent.low != 0:
        r "А?{w=0.3}{nw}"
        window hide
        hide screen quick_menu
        hide screen mind_bar_screen
        $ quick_menu = False
        with Dissolve(.3)
        play music tv_ads volume 0.5
        show screen block_scr(persistent.tv_rui, 19)
        $ renpy.movie_cutscene ('videos/tv rui3.webm', stop_music=False)
        scene tv rui4
        $ quick_menu = True
        show screen quick_menu
        show screen mind_bar_screen
        with Dissolve(.3)
        window show

    if persistent.low == 0:
        r "О, я помню эту рекламу.{w=0.3}{nw}"
        window hide
        pause 14.0
        window show
    else:
        r "О, я помню эту рекламу."

    $ _dismiss_pause = True
    if persistent.tv_rui:
        scene tv rui4
    $ persistent.tv_rui = True

    r "Хмм... [player_name], ты не хочешь сыграть в какую-нибудь игру?{w=0.2} Ммм... {w=0.3}О! У меня есть идея, сейчас приду, никуда не уходи."

    p "Будто у меня есть выбор..."

    "Руи уходит из комнаты, вы смотрите на экран телевизора."

    p "..."

    "..."

    "Погодите, а картинка на экране разве не должна меняться?"

    stop music

    ".{w=0.3}.{w=0.3}."

    play music none volume 1.0 fadein 3.0

    p "Почему пропал звук..."

    play sound k_sad_um volume 0.01

    ks2 "{glitch=10}{sc}{=norm_style}Держись...{/sc}{/glitch}{w=0.2}{nw}"

    extend "{glitch=10}{sc}{=norm_style} Пожалуйста, держись...{/sc}{/glitch}{w=0.5}{nw}"

    extend "{glitch=10}{sc}{=norm_style} Я могу помочь тебе...{/sc}{/glitch}"

    $ mind(50, "-")

    p "Какого чёрта?.."

    p "Это... {w=0.3}Я не слышу голоса, но... {w=0.2}Я его чувствую..."

    ks2 "{glitch=10}{sc}{=norm_style}Ты{/sc}{/glitch}{w=0.2}{nw}"
    extend "{glitch=10}{sc}{=norm_style} мне{/sc}{/glitch}{w=0.2}{nw}"
    extend "{glitch=10}{sc}{=norm_style} доверяешь{/sc}{/glitch}{w=0.2}{nw}"
    extend "{glitch=10}{sc}{=norm_style}?{/sc}{/glitch}"

    menu:

        "[[Промолчать]":

            p "Бред какой-то..."

            $ mind(100, "-")

            p "Мне кажется, я просто схожу с ума, ха-ха..."

        "Да":

            $ kaito_state += 10

            p "Да?.."

            ks2 "{glitch=10}{sc}{=norm_style}Я{/sc}{/glitch}{w=0.2}{nw}"
            extend "{glitch=10}{sc}{=norm_style} рад...{/sc}{/glitch}{w=0.4}{nw}"
            extend "\n{glitch=10}{sc}{=norm_style}Спасибо,{/sc}{/glitch}{w=0.2}{nw}"
            extend "{glitch=10}{sc}{=norm_style} [player_name].{/sc}{/glitch}"

        "Нет":

            $ kaito_state -= 5

            p "Как я могу доверять хуй пойми кому... {w=0.2}или чему..."

            ks2 "{glitch=10}{sc}{=norm_style}Пожалуйста,{/sc}{/glitch}{w=0.2}{nw}"
            extend "{glitch=10}{sc}{=norm_style} доверься.{/sc}{/glitch}"

            $ mind(50, "-")

            p "Пиздец, нахуй, сука, блять, какого хуя, блять, залупа, ну и пизда..."

    # руи: 95 50 рассудок: 700 100 кайто: 110 95

    scene tv ruiglitch

    play sound [ "<silence .1>", "audio/switch.ogg" ]
    stop music

    pause 0.3

    call kaito_list_lable("tv") from _call_kaito_list_lable_11

    p "!!!"

    r "[player_name]... {w=0.5}{nw}" 

    play music rui_home fadein 3.0 volume 0.6

    show rui nc hello:
        xalign -0.5
        ease 1.3 xalign 0.5
    
    extend "прости за ожидание, я давно не играл в карты и забыл где они лежат."

    show rui nc hello:
        xalign 0.5

    p "Карты?.."

    show rui nc happy at sd

    r "Угу, я предлагаю сыграть в дурака, что думаешь?"

    menu:

        "Ты это про себя?":

            $ rui_state -= 10

            show rui nc shock at sd

            p "Эм... {w=0.5}Дурак? Ты это про себя?"

            show rui nc srs at sd

            r "..."

            if rui_state <= 70:

                "Руи тяжело вздыхает, смотря на вас серьёзным взглядом."

            else:

                r "[player_name]... Дурак – это русская карточная игра."

            r "Так ты хочешь сыграть или нет?"

            menu:
            
                "Да":

                    p "Ладно, хорошо."

                "Нет":

                    $ rui_state -= 5

                    p "Нет, иди нахуй."

                    show rui nc sad at sd

                    r "Как скажешь, моё дело предложить..."

                    r "Тогда просто будем смотреть странную передачу по телевизору..."

                    p "..."

                    jump tv_cont

                "Мне всё равно":

                    p "Мне всё равно..."

        "Давай" if mind_value > 450:

            $ rui_state += 10

            p "Хорошо, давай."

        "Нет" if mind_value > 250:

            p "Нет{w=0.1}.{w=0.1}.{w=0.1}."

            show rui nc sad at sd

            r "Хорошо, тогда просто посмотрим телевизор..."

            p "..."

            jump tv_cont

        "Мне всё равно" if mind_value > 100:

            p "Делай что хочешь..."

    # руи: 105 35 рассудок: 700 100 кайто: 110 95

    show rui nc blush at sd

    r "Отлично! Ты знаешь правила?"

    menu:

        "Да":

            p "Да, я не дура."

            r "Хорошо, тогда начнём игру!"

        "Нет":

            p "Хз, не играла..."

            show rui nc hello at sd

            r "Окей, сейчас я попробую тебе объяснить..."

            call durak_ruls from _call_durak_ruls

    show rui nc happy at sd

    r "Так, кто раздаёт карты?"

    menu:

        "Ты":

            $ player_takes_cards_ = False

            stop music fadeout 1.0

            p "Давай ты..."

        "Я":

            $ player_takes_cards_ = True

            stop music fadeout 1.0

            p "Я!"


    # миллион переменных
    hide screen mind_bar_screen
    window hide
    call durak_game from _call_durak_game
    scene black
    pause 0.3
    scene bg rui living room
    show screen mind_bar_screen

    play music rui_home fadein 1.0 volume 0.6

    $ rui_state += 30

    if who_win_ == 0:
        show rui nc crazy1 
        with Dissolve(.2)
        $ mind(100, "-")
        r "Фуфу, я выиграл~"
    elif who_win_ == 2:
        show rui nc shock
        with Dissolve(.2)
        $ mind(300, "+")
        r "Ухты, ты выиграла..."
    else:
        show rui nc hello
        with Dissolve(.2)
        if mind_value > 750:
            $ mind(100, "-")
        elif mind_value < 450:
            $ mind(100, "+")
        r "Надо же у нас ничья!"

    show rui nc blush at sd

    r "В любом случае, спасибо за игру, [player_name]."

    r "А теперь давай просто расслабимся и посмотрим телевизор..."

    jump tv_cont

    return

# руи: 135 0 рассудок: 1000 50 кайто: 110 95



# смотрят телевизор дальше
label tv_cont:

    stop music fadeout 1.0

    show black:
        alpha 0.0
        linear 0.5 alpha 1.0

    window hide

    play music doomed fadein 2.0 volume 0.6

    pause 1.0

    scene black

    scene tv_changes
    show eye-open-true
    with Dissolve(1.5)

    pause

    window show

    p '...'

    window hide

    $ mind(50, "-")

    show eye-open-true at blink7
    show tv_changes:
        yanchor 0.5 xanchor 0.5 yalign 0.5 xalign 0.5
        pause 0.4
        ease 0.5 zoom 1.5 rotate -3 yalign 0.57

    pause 1.5

    window show

    p "Мх..."

    "Ваша голова кажется такой тяжёлой... {w=0.5}А глаза вот-вот закроются..."

    "Но хорошая ли идея сейчас спать?.."

    $ renpy.stop_skipping()

    "Может стоит {b}{i}поднажать{/i}{/b} и не засыпать?"

    window hide

    $ renpy.notify('Жмите, чтобы не заснуть!')

    $ sleep_clik = 50

    show screen cliker with Dissolve(.2)

    pause
    
    return

label no_sleep_on_tv:

    hide screen cliker with Dissolve(.5)

    show tv_changes:
        easein_expo 0.15 yalign 0.5 xalign 0.5 rotate 0 zoom 1.0

    p '(Нет! Нельзя так просто терять бдительность!)'

    p 'Кто знает, что Руи может сделать...'

    r '[player_name]...'

    p "!!!"

    r "Ты спишь?"

    menu:

        "Нет":

            p "Нет..."

            r "Выглядишь сонной... {w=0.5}Пойдём уже ложиться спать."

            p "А-{w=0.2}{nw}"

            "Вы не успеваете что-либо сказать, как Руи берёт вас за руку и ведёт в свою спальню."

            jump sleep_rui_home

        "[[Притвориться спящей]":

            $ rui_state -= 5

            show blank at blink_close

            p "..."

            play sound undress

            "Вы чувствуете как руи осторожно берёт вас на руки "

            stop music fadeout 0.3

            play sound steps

            extend "и несёт вас куда-то."

            p "..."

            play sound bed volume 2.0

            "Он вроде как положил вас на кровать... {w=0.5}И лёг рядом с вами."

            play music rui_home fadein 1.0 volume 0.7

            r "Я знаю, что ты не спишь, но сейчас тебе лучше поспать."

            p "..."

            jump sleep_rui_home.sleep

    return

label sleep_on_tv:

    $ mind(200, "+")

    stop music fadeout 5.0

    scene black
    hide screen cliker

    jump kaito_dream

# они пошли спать
label sleep_rui_home:

    window hide

    stop music fadeout 0.3

    scene black with Dissolve(.3)
    play sound steps 

    pause 3.5

    play music rui_home fadein 1.0 volume 0.7

    scene bg rui bedroom with Dissolve(.3)

    window show

    p ".{w=0.3}.{w=0.3}."

    "Подойдя к кровати вы осознаёте насколько действительно устали..."

    "Ваше тело само лезет в тёплую кровать, желая побыстрее окунуться в сон и забыть о сегодняшнем дне."

    show bg rui bedroom:
        ease 0.3 zoom 1.5

    play sound undress

    scene black with Dissolve(.3)

    "Да... так лучше..."

    play sound undress

    "Вы чувствуете как Руи ложится рядом с вами... {w=0.4}Но к счастью он вас не трогает."

    label .sleep:

        scene bg rui bedroom roof
        show blank at blink_open

        r "Спокойной ночи, [player_name]."

        menu:

            "Спокойной ночи":

                $ rui_state += 15

                p "Спокойной ночи.{w=0.3}.{w=0.3}.{w=0.5} Руи."

            "...":

                $ rui_state -= 10

                p "..."

                "Руи тяжело вздыхает и поворачивается на бок."

        r "Я люблю тебя, [player_name]. {w=0.5}Я правда люблю тебя..."

        "Вы хотите спать и сон бы точно пошёл вам на пользу, хоть вы и не уверены в обстоятельствах."

        menu:

            "Заснуть":

                $ mind(50, "+")

                stop music fadeout 5.0

                show blank at blink_close

                "Вы решаете, что лучше будет набраться сил перед завтрашним днём, и закрываете глаза, погружаясь в глубокий сон."

                jump kaito_dream

            "Не спать":

                "Вы решаете, что спать сейчас опасная затея и вам нужно продержаться до утра..."

                play music none volume 5.0

                $ mind(50, "-")

                p "..."

                $ mind(50, "-")

                p "..."

                "Тишина кажется слишком громкой... {w=0.5}Может всё-таки стоит поспать?"

                menu:

                    "Поспать" if mind_value > 100:

                        stop music
                        show blank at blink_close

                        "Так всё же будет лучше для вас..."

                        jump kaito_dream

                    "НЕ СПАТЬ":

                        $ mind(150)

                        p "НЕТ, Я НЕ МОГУ ПОКА СПАТЬ"

                        p "..."

                        $ mind(50, "-")

                        p "..."

                        $ mind(50, "-")

                        p "Или всё же..."

                        menu:

                            "Поспать" if False:
                                pass
                            "НЕ СПАТЬ":

                                p "..."

                                p "Боже.."

                                $ mind(0)

    return

# руи: 150 -25 рассудок: 1000 0 кайто: 110 95