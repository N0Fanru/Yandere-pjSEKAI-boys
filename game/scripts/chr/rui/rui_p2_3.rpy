define need_kaito = 100

label rui_return: # этот еблан  вернулся

    # руи: 180 -50 (сер:65) рассудок: 1000 0 кайто: 160 50

    hide screen r_bedroom
    hide screen r_room
    hide screen r_studio
    hide screen r_kitchen
    hide screen r_toilet
    hide screen rui_timer
    hide screen rui_home_scheme
    hide screen card_button
    with Dissolve(.2)
    stop music
    play sound door

    if locate == 'bed':

        scene bg rui bedroom roof
        with Dissolve(.3)

        "Вы слышите звук замка, свидетельствующий о том, что Руи вернулся."

    if locate == "bedroom":

        p "!!!"

        play audio undress
        scene black with Dissolve(.2)

        "Услышав звук открывающейся двери, вы быстро легки в кровать."

        scene bg rui bedroom roof
        with Dissolve(.3)

        $ locate = 'bed'


    if locate == 'bed':

        "Из коридора слышны разговоры Руи с... Нене?.. Но вы не можете разобрать о чём именно они говорят."

        p "..."

        if score >= 6:
            jump kaito_win

        "Через пару минут всё утихает и по шагам слышно, как Нене уходит."

        if score != 0:

            "Неужели она не заметила?.. Неужели у вас не вышло?.."

        play sound steps

        pause 3.3

        stop sound

        if rui_state > 40:
            jump good_new_end
        else:
            jump rui_suid

    p "!!!"

    p "Вот же чёрт..."

    play music stress fadein 1.0 volume 0.5

    "Ого, вы не успели вернуться в спальню, а Руи уже пришёл, кажется, вам пиздец!"

    show nene uh zorder 2:
        xalign -0.8
        ease 0.8 xalign 0.5

    ne "[player_name], так это прав-{w=0.2}{nw}"

    play sound udar2

    show rui lom zorder 1:
        xalign 1.8
        easein_back 0.3 xalign 0.6

    show nene uh:
        pause 0.1
        easeout_back 0.2 ypos 1000

    r "ТИХО!{w=0.2}{nw}"

    show rui lom:
        ease 0.3 zoom 1.5 yalign 0.2

    r "..."

    stop music
    play sound udar2
    scene black

    $ rui_pain_add("47")

    jump basement

    return

# счёт не набран, Руи пришёл и happy
label good_new_end:

    play music rui_home fadein 2.0 volume 0.6 

    show bg rui bedroom roof:
        "bg rui moning2" with Dissolve(.5)

    r "Я вернулся, [player_name]~{w}\nИ купил тебе кое-что вкусное."

    show bg rui moning2:
        "bg rui bedroom roof" with Dissolve(.3)
        pause 2.5
        "bg rui feeds" with Dissolve(.3)

    "Руи достаёт из пакета стаканчик мороженого с ложечкой, и, зачерпнув немного, протягивает ложку с мороженым вам."

    r "Поешь, [player_name]~"

    "Его голос прозвучал как-то зловеще... Хотя возможно вам просто показалось, но испытывать судьбу лишний раз вы не стали и съели то, что вам предлагали."

    show bg rui feeds:
        "bg rui feeds none" with Dissolve(.1)

    "На удивление, мороженое оказалось очень вкусным! Вам захотелось ещё..."

    r "Вкусно? Будешь ещё?"

    "Вы энергично киваете головой."

    show bg rui feeds none:
        "bg rui feeds" with Dissolve(.1)

    "Руи набирает ещё мороженого и протягивает вам. "

    show bg rui feeds:
        "bg rui feeds none" with Dissolve(.1)

    extend "Вы вновь съедаете."

    $ mind(100, "+")

    p "Как же это вкусно! Хочу ещё!"

    show bg rui feeds none:
        "bg rui feeds" with Dissolve(.1)

    r "Фу-фу~"

    show bg rui feeds:
        "bg rui feeds none" with Dissolve(.1)

    if mind_value < 900:
        $ mind(900)
    
    p "БОЖЕСТВЕННЫЙ ВКУС!{w}\nГде ты купил такое мо-{w=0.2}{nw}"

    $ mind(1000)

    p "Охх... Я как-то не хорошо себя чувствую..."

    show bg rui feeds none:
        "bg rui moning3" with Dissolve(.2)

    r "Всё хорошо?"

    stop music fadeout 5.0

    p "В голове будто туман..."

    r "..."

    p "Руи... Я... я люблю тебя..."

    show bg rui moning3:
        "bg rui moning2" with Dissolve(.1)

    r "Я тоже люблю тебя, [player_name]~"

    p "Руи... "

    show bg rui moning2:
        "bg rui tuch" with Dissolve(.15)

    extend "давай займёмся сексом..."

    show bg rui tuch:
        "bg rui tuch2" with Dissolve(.1)

    r "Ты уверена?"

    p "Да..."

    show bg rui tuch2:
        "bg rui tuch" with Dissolve(.1)

    r "Хорошо, я тебя поня-{w=0.2}{nw}"

    p "Не раздевайся, давай быстрее..."

    show bg rui tuch:
        "bg rui bedroom roof" with Dissolve(.2)

    r "Дай я хотя бы плащ сниму..."

    p "..."

    play music sexmusic fadein 2.0 volume 0.2

    show bg rui bedroom roof:
        "bg rui nome s1" with Dissolve(.3)

    "Руи снимает себя плащ и взбирается на вас."

    "Ваше тело будто горит от желания... Что же на ваш нашло?"

    p "Быстрее, быстрее, начинай, Руи..."

    play sound undress

    "Руи осторожно снимает с вас одежду, растягивает свою ширинку и выполняет остальные дейстивия перед началом."

    p "Прошу, Руи, не томи, давай без прелюдий, моё тело уже готово, начинай быстрее..."

    r "Хорошо, [player_name]..."

    show bg rui nome s1:
        "bg rui nome s2" with Dissolve(.1)

    "С этими словами он резко входит в вас, из-за чего из вашего рта вырывается громкий стон."

    p "Мх..."

    r "Всё хорошо?"

    p "Да, продолжай..."

    "Руи начинает двигаться, ваше тело реагирует слишком сильно, слишком..."

    show bg rui nome s2:
        "bg rui nome s3" with Dissolve(.1)

    "Вам почти хочется плакать от переизбытка ощущений... Почему всё ощущается так ярко?.."

    "Неужели это из-за мороженного?.. Нет, это не важно, не важно."

    "Вы внимательно смотрите в лицо Руи..."

    p "Я тебя люблю."

    r "Я тоже тебя люблю, [player_name]~"

    "Такое странное чувство... Будто вы влюбились в Руи снова... Будто вы снова признались друг другу в своих чувствах."

    "У вас на глазах начинают появляться слёзы. Вы чувствуете себя так... счастливо."

    p "Я хочу остаться с тобой навсегда, Руи..."

    r "Я тоже, [player_name], я тоже..."

    p "Ах..."

    r "Я скоро кончу."

    show bg rui nome s3:
        "bg rui nome s4" with Dissolve(.1)

    "Последние несколько толчков и Руи кончает в презерватив, после чего рухается на кровать рядом с вами."

    $ rui_horny_add("21")

    stop music fadeout 2.0

    window hide

    scene end rui happy m with Fade(0.3, 0.8, 0.3)

    play music low fadein 2.0 volume 2.5

    pause

    window show

    r "Ты как, [player_name]?"

    p "Я?.. Я хорошо... Я отлично..."

    p "Руи, я..."

    r "М? Ты?"

    p "Давай навсегда будем вместе? Я поняла насколько сильно люблю тебя, Руи"

    show black:
        alpha 0.0
        linear 3.0 alpha 1.0

    r "Конечно, [player_name], конечно..."

    show black:
        alpha 1.0

    "С того дня вы и Руи всегда были вместе... И, кажется, вы действительно были счастливы."

    window hide

    pause 0.5

    call ends_rui("happy") from _call_ends_rui_23

    pause 5.0

    return

# счёт не набран, Руи пришёл и not happy
label rui_suid:

    play music rui_home fadein 2.0 volume 0.6

    show bg rui bedroom roof:
        "bg rui moning3" with Dissolve(.5)

    r ".{w=0.3}.{w=0.3}."

    p "(Почему он выглядит таким грустным?..)"

    r "[player_name]..."

    p "???"

    r "Нам нужно расстаться."

    p "Что?"

    r "Ты меня не любишь..."

    p "..."

    r "Я не могу так больше, прости, [player_name]."

    show bg rui moning3:
        "bg rui suid" with Dissolve(.2)

    r "Прости..."

    p "Руи, сто-{w=0.2}{nw}"

    play sound shot fadeout 0.5
    stop music
    scene black
    hide screen mind_bar_screen

    p "..."

    window hide

    play music doomed fadein 3.0 volume 0.6

    scene end rui suid with Dissolve(2.0)

    pause

    $ config.choice_empty_window = None

    menu:

        "Взять пистолет":

            $ config.choice_empty_window = extend

            stop music fadeout 0.5
            scene black with Dissolve(0.5)

            pause 0.5
            play sound shot

            pause 5.0

            call ends_rui("suid") from _call_ends_rui_24

            pause 5.0

            return

        "Уйти":

            $ config.choice_empty_window = extend
            stop music fadeout 1.5

            window show

            p "..."

            scene black with Dissolve(.5)

            "Вы оставляете Руи так и просто уходите..."

            jump the_end

    return 

# у гг получилось
label kaito_win:

    play sound knock1 volume 1.0

    p "!!!"

    "Вы слышите глухой удар, что это может быть?.."

    scene bg rui bedroom moning with fade

    "Вы садитесь на кровать, прислушиваясь к звукам."

    show nene uh:
        parallel:
            xalign -0.5
            ease 0.6 xalign 0.5
        parallel:
            alpha 0.0
            ease 0.3 alpha 1.0

    pause 1.0

    show nene uh:
        xalign 0.5 alpha 1.0

    play music ruistart fadein 1.5 volume 0.4

    ne "О боже..."

    show nene sad at sd

    ne "Кайто действительно говорил правду и тебя похотил Руи..."

    p "..."

    show nene uh at sd

    ne "Пойдём, [player_name], это всё закончится здесь и сейчас. Я уже вызвала полицию, всё будет хорошо."

    hide screen mind_bar_screen
    scene bg street3
    show nene sad:
        xalign 0.2
    with fade

    ne "..."

    show nene uh at sd

    ne "О! Кайто хочет тебе что-то сказать..."

    show kaito happy:
        xalign 0.8 alpha 0.0 matrixcolor TintMatrix("#449effff")
        ease 0.3 alpha 0.7

    if need_kaito >= 50:
        k "Привет, [player_name]~"

        k "Я очень рад, что мой план сработал..."

        show kaito tuch at sd

        k "И знаешь, мне кажется, что ты заслуживаешь небольшую награду~"

        p "Что?{w=0.4}{nw}"

        jump kaito_secret
        
    else:
        k "Привет, [player_name]..."

        p "..."

        show kaito think at sd

        k "Ну, я рад, что мой план сработал..."

        k "Теперь ты можешь начать новую жизнь и наконец-то всё будет хорошо..."

        p "Да..."

        stop music fadeout 1.0
        scene black with Dissolve(.5)

        p "Верно... теперь всё будет хорошо..."

        jump the_end

    return

# концовка с названием концовка
label the_end:

    window hide

    play music harmony fadein 3.0

    scene end rui the_end with Dissolve(.5)

    window show

    p "Наконец-то это всё кончено..."

    "Больше никакого Руи, никакой ядерки, наконец-то вы будите жить нормальной жизнью..."

    "Просто наконец-то..."

    window hide

    pause 5.0

    call ends_rui("the_end") from _call_ends_rui_25

    pause 5.0

    return

# подвал ура
label basement:

    $ mind(200, "-")

    window hide
    play sound2 wake
    pause 6.1
    window show

    p "Мх... Голова..."

    scene bg basement
    show blank at blink_open

    play music nn1 fadein 1.0 volume 0.1

    p "Как же больно..."

    p "Подождите... Почему я в подвале из гача лайф?!"

    p "О нет нет нет нет... дела плохи..."

    r "[player_name]..."

    p "{cps=4}...{/cps}"

    "Ну а дальше происходили такие страшные вещи, что даже для этой игры это слишком..."

    "..."

    window hide

    pause 5.0

    call ends_rui("podval") from _call_ends_rui_26

    pause 5.0

    return

    return