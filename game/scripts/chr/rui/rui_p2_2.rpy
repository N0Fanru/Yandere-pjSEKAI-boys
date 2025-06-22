# руи: 150 -25 рассудок: 1000 0 кайто: 110 95

# гг снится сон с Кайто
label kaito_dream:

    window hide

    pause 0.5

    scene black

    play music [k_eman, "<silence 1.5>"] loop volume 0.1

    pause

    window auto

    p "Что это за звук?.."

    p "..."

    scene bg dream1:
        zoom 1.5 yanchor 0.5 xanchor 0.5 yalign 0.5 xalign 0.5
    show blank at blink_open_more

    pause 2.0

    p "Ай.. {w=0.7}Как ярко..."

    show bg dream1:
        ease 0.5 xalign 0.0

    p "Где я?.. {w=0.7}{nw}"

    show bg dream1:
        ease 1.0 xalign 1.0

    extend "Это сон?"

    p "Судя по всему так..."

    stop music
    play sound k_um

    p "!!!"

    show d 1:
        xalign -0.5
        ease 0.5 xalign 0.5
    show bg dream1:
        ease 0.5 xalign 0.0

    p "Кто тут?!"

    p "..."

    p "Как бы я не пыталась всмотреться, я не могу разобрать его лицо..."

    nq "{glitch=10}{sc}{=norm_style}[player_name]...{/sc}{/glitch}"

    p "А?"

    nq "{glitch=10}{sc}{=norm_style}Ты {/sc}{/glitch}{w=0.2}{nw}"
    extend "{glitch=10}{sc}{=norm_style}должна {/sc}{/glitch}{w=0.2}{nw}"
    extend "{glitch=10}{sc}{=norm_style}довериться {/sc}{/glitch}{w=0.2}{nw}"
    extend "{glitch=10}{sc}{=norm_style}мне.{/sc}{/glitch}"

    if mind_value - 50 > 0:
        $ mind(50, "-")

    p "Уфф..."

    nq "{glitch=10}{sc}{=norm_style}Он {/sc}{/glitch}{w=0.2}{nw}"
    extend "{glitch=10}{sc}{=norm_style}сейчас {/sc}{/glitch}{w=0.2}{nw}"
    extend "{glitch=10}{sc}{=norm_style}спит.{/sc}{/glitch}"

    nq "{glitch=10}{sc}{=norm_style}Тебе {/sc}{/glitch}{w=0.2}{nw}"
    extend "{glitch=10}{sc}{=norm_style}нужно {/sc}{/glitch}{w=0.2}{nw}"
    extend "{glitch=10}{sc}{=norm_style}проснуться {/sc}{/glitch}{w=0.2}{nw}"
    extend "{glitch=10}{sc}{=norm_style}и {/sc}{/glitch}{w=0.2}{nw}"
    extend "{glitch=10}{sc}{=norm_style}взять {/sc}{/glitch}{w=0.2}{nw}"
    extend "{glitch=10}{sc}{=norm_style}его {/sc}{/glitch}{w=0.2}{nw}"
    extend "{glitch=10}{sc}{=norm_style}телефон.{/sc}{/glitch}"

    p "Что... Но это-{w=0.3}{nw}"

    play sound k_ja

    nq "{glitch=10}{sc}{=norm_style}Тебе {/sc}{/glitch}{w=0.2}{nw}"
    extend "{glitch=10}{sc}{=norm_style}нужно {/sc}{/glitch}{w=0.2}{nw}"
    extend "{glitch=10}{sc}{=norm_style}включить {/sc}{/glitch}{w=0.2}{nw}"
    extend "{glitch=10}{sc}{=norm_style}песню.{/sc}{/glitch}"

    p "Песню... Какую ещё нахуй песню?"

    nq "{glitch=10}{sc}{=norm_style}Ты {/sc}{/glitch}{w=0.2}{nw}"
    extend "{glitch=10}{sc}{=norm_style}поймёшь. {/sc}{/glitch}"
    extend "{glitch=10}{sc}{=norm_style}Доверься {/sc}{/glitch}{w=0.2}{nw}"
    extend "{glitch=10}{sc}{=norm_style}мне.{/sc}{/glitch}"

    p ".{w=0.5}.{w=0.5}."

    menu:

        "Хорошо" if mind_value < 900:

            $ kaito_state += 20

            p "Хорошо... {w=0.5}Наверное..."

            call kaito_list_lable("dream") from _call_kaito_list_lable_12

            play sound k_mm

            show d 3

            nq "{glitch=10}{sc}{=norm_style}Спасибо.{/sc}{/glitch}"

            window hide

            show blank at blink_close zorder 5
            pause 0.5

        "Иди нахуй":

            $ kaito_state -= 15

            p "НЕТ ИДИ НАХУЙ"

            p "Это ж верная смерть... {w=0.7}Тем более я понятие не имею кто ты..."

            p "Вдруг ты просто моя шиза или типа того..."

            play sound k_um

            show d 2

            nq "{glitch=10}{sc}{=norm_style}...{/sc}{/glitch}"

            p "..."

            window hide

            show d 2:
                ease 0.05 zoom 10.0 yalign 0.2

            pause 0.04

            scene black

    pause

    scene bg rui bedroom roof
    show blank at blink_open_more

    pause 2.0

    window show

    p "Умф..."

    p "Включить песню на телефоне Руи... {w=0.5}Стоит ли это делать на самом деле?.."

    menu:

        "Сделать это!":

            p "Чёрт, ладно, была не была..."

        "Не, спать":

            $ mind(150, "+")

            $ kaito_state -= 20

            p "Не, ну нахуй, я лучше посплю..."

            show blank at blink_close

            "Вы закрываете глаза и вновь погружаетесь в сон, на этот раз вы проспите до утра."

            scene black
            window hide

            jump good_moning

            # руи: 150 -25 рассудок: 1000 0 кайто: 130 60

    
    play sound undress
    window hide
    scene black with Dissolve(.3)

    pause 0.5

    play sound steps

    pause 3.3

    play music night fadein 0.5 volume 0.7
    scene bg rui phone with Dissolve(.3)
    
    window show

    "Вы осторожно слазите с кровати и подходите к тумбочке Руи."

    p "(Самое главное действовать осторожно...)"

    window hide

    pause

    $ _dismiss_pause = False

    show bg rui phone take with Dissolve(.2)

    pause 0.3

    show bg rui phone un with Dissolve(.4)

    pause 0.3

    show phone off:
        xalign 0.5 zoom 0.5 yalign -3.0
        easein_back 1.0 yalign -0.3

    pause 1.4

    $ can_sekai = False

    show screen phone with Dissolve(.1)
    hide phone off

    window show

    p "(Он говорил про эту песню?..)"

    window hide

    $ can_sekai = True

    pause

    return


# гг попадает в секай
label wond_sekai:

    $ kaito_state += 10

    stop music

    play sound "audio/ui_sfx/choice.flac"

    scene expression Solid("#fff")
    hide screen phone
    hide screen enter_sekai
    with test

    pause 2.0

    play music sekai fadein 3.0 volume 0.6

    scene bg sekai with Dissolve(5.0)

    $ _dismiss_pause = True

    window auto

    p "Ох..."

    p "Где я?.."

    window hide

    show bg sekai:
        ease 0.5 zoom 1.8 xalign 0.7 yalign 0.8
        pause 0.3
        ease 0.5 xalign 1.0 yalign 0.3 zoom 1.8
        pause 0.2
        ease 0.5 xalign 0.1 yalign 0.7 zoom 1.5
        pause 0.2
        ease 0.3 zoom 1.0 xalign 0.5 yalign 1.0

    pause 2.8

    window auto

    p ".{w=0.5}.{w=0.5}."

    p "Я либо окончательно сошла с ума, либо... {w=0.5}Либо я не знаю что! Этому же просто нет объяснения..."

    if mind_value - 100 > 0:
        $ mind(100, "-")
    elif mind_value - 50 > 0:
        $ mind(50, "-")

    p "Ах..."

    noc "Хммм... Кто-то пришёл в такое позднее время?~"

    p "!!!"

    show miku smile:
        alpha 0.0 xalign 0.5
        linear 0.2 alpha 1.0

    noc "Что-то случи-{w=0.3}{nw}"

    show miku shock at sd:
        alpha 1.0

    noc ".{w=0.5}.{w=0.5}."

    p "..."

    p "Это... {w=0.3}МИКУ?!"

    show miku sad at sd

    m "Вот дела..."

    p "Значит я точно сошла с ума, раз уж уже Мику перед собой вижу, хаха..."

    show miku shock at sd

    m "Ва! Успокойся, успокойся... {w=0.3}Всё хорошо, ты в порядке."

    show miku smile at sd

    m "Ты находишься в Секае - место, созданное из чувств Цукасы!"

    p "Цукасы?"

    show miku think at sd

    m "Но, честно говоря, ты не должна тут находиться... {w=0.3}Как ты сюда попала?"

    show miku shock at sd

    noc "Кто-то пришёл?"

    show miku shock:
        pause 0.2
        ease 0.3 xalign -0.1

    show kaito_wxs happy:
        xalign 2.3
        ease 0.5 xalign 1.1

    noc "Мику-{w=0.5}{nw}"

    show kaito_wxs shock at sd:
        xalign 1.1
    show miku shock0:
        xalign -0.1

    noc "!!!"

    p ".{w=0.5}.{w=0.5}.{w=0.5}Кайто?.."

    show kaito_wxs think at sd

    $ k = Character(_('     Кайто'), color="#3f7df9", image='kaito', callback=[name_callback, textsound_callback], cb_name='kaito')

    k "Так значит всё же так..."

    p "???"

    show kaito_wxs happy at sd

    k "Ну, добро пожаловать в {nw}"

    show miku smile0 at sd
    
    extend "Wonderland Секай!"

    p "Спасибо..."

    show kaito_wxs srs0 at sd
    show miku think0 at sd

    m "Но всё же, как ты-{w=0.2}{nw}"

    show kaito_wxs happy0 at sd

    k "Пойдём я тебе всё тут покажу!"

    show miku shock0 at sd

    m "Э, Кайто!"

    k "Пойдём, пойдём..."

    stop music fadeout 3.0

    show black:
        alpha 0.0
        linear 0.2 alpha 1.0

    "Кайто быстро хватает вас за руку и отводит дальше от Мику."

    play music iakes fadein 1.0 volume 0.4

    scene bg sekai2
    show kaito_wxs srs
    with Dissolve(1.0)

    p "..."

    p "(Я чувствую себя как-то неуютно...)"

    p "(Может, я снова заснула?..)"

    p "(Если так присмотреться, то Кайто чем-то похож на тот силуэт из сна...)"

    p ".{w=0.5}.{w=0.5}."

    p "(Нет, всё-таки различия точно есть.)"

    k "[player_name]..."

    p "!!!"

    p "Откуда ты знаешь моё имя?.."

    show kaito_wxs think at sd

    k "Так значит, это всё же ты..."

    p "Ну... да..."

    p "..."

    show kaito_wxs normal at sd

    k "Скажи, ты ведь оказалась тут, потому что тебя попросил кто-то из сна?"

    p "Да! Так ты это был ты?!"

    k "Нет... "

    show kaito_wxs think at sd

    extend "Точнее, не совсем я..."

    p "А?"

    k "Это была другая версия меня."

    p "Другая версия тебя?"

    k "Угу..."

    show kaito_wxs normal at sd

    k "Скажи, получается это правда то, что он говорил?"

    k "Тебя действительно похитил Руи?"

    p "..."

    # руи: 150 -25 рассудок: 1000 0 кайто: 140 80

    menu:

        "Да" if mind_value < 1000:

            $ kaito_state += 10

            "Вы осторожно киваете головой."

            p "Да, это так..."

            show kaito_wxs sad at sd

            k "Понятно..."

            k "Не ожидал я от него такого... {w=0.5}Мне жаль, что тебе приходиться проходить через это..."

            p "..."

            if mind_value < 600:
                $ mind(100, "+")
                p "Да..."
            elif mind_value > 600:
                $ mind(100, "-")
                p "Уфф..."

            show kaito_wxs normal at sd

            k "[player_name], мы поможем тебе. Мы обязательно тебя спасём."

            p '"Мы"?'

            k "Я и моя другая версия. В случае необходимости мы и других привлечём, но всё сделаем очень осторожно."

            p "Спасибо..."

        "Нет":

            $ kaito_state -= 10

            p "Нет."

            k ".{w=0.5}.{w=0.5}."

            show kaito_wxs srs at sd

            k "[player_name]... Может, ты не осознаёшь всей серьёзности данной ситуации или, может, ты не доверяешь мне, но..."

            k "Но тебе правда нужна помощь и мы её можем тебе дать."

            p "..."

            show kaito_wxs normal at sd

            k "Пожалуйста, доверься мне и позволь помочь..."

    # руи: 150 -25 рассудок: 1000 0 кайто: 150 70

    k "Нам нужно встретиться с другой моей версией, у него должен быть план."

    k "Я перемещу нас в его Секай."

    stop music
    play sound "audio/ui_sfx/choice.flac"
    play music none volume 3.0
    scene expression Solid("#fff") with test

    pause 2.0

    scene bg kaito
    show kaito_wxs srs1
    with Dissolve(5.0)

    p "..."

    p "Тут так тихо..."

    show kaito_wxs normal1 at sd

    kw "Он должен быть где-то тут..."

    kw "КАЙТОООО!" with hpunch

    show kaito_wxs normal1:
        pause 0.2
        ease 0.3 xalign 0.0

    show kaito hello0:
        xalign 2.3 yalign 1.0
        ease 0.5 xalign 1.0

    k "Я тут!"

    show kaito_wxs normal1:
        xalign 0.0
    show kaito hello0:
        xalign 1.0

    show kaito smile0 at sd

    k "Вы всё-таки пришли, я так рад..."
        
    p "Ты!"

    show d 1:
        xalign 0.83 alpha 0.0
        ease 0.2 alpha 1.0

    p "Точно, это ты был в моём сне..."

    show kaito srs0 at sd
    hide d 1

    k "Да, это так. Спасибо, что сделала так, как я просил, [player_name]."

    show kaito smile0 at sd

    k "Тебе тоже спасибо, Вакай."

    show kaito_wxs happy1 at sd

    kw "Конечно, да и я сам хочу помочь."

    show kaito_wxs think1 at sd

    kw "Честно говоря, я тебе не поверил, когда ты рассказал, что Руи сделал..."

    show kaito_wxs normal1 at sd

    kw "Так, у тебя есть план?"

    show kaito think0 at sd

    k "Есть несколько идей... Скажи, у WxS ведь завтра репетиция?"

    kw "Да, всё так... Но пойдёт ли туда Руи..."

    k 'Он пойдёт. Он сейчас наоборот будет пытаться вести себя наиболее "нормально".'

    show kaito srs0 at sd

    k "Скажи, кто из WxS самый надёжный?"

    show kaito_wxs think1 at sd

    kw "Надёжный?.. Сложный вопрос... Ну... наверное, Нене."

    show kaito sad0 at sd

    k "Нене, говоришь... {w}Как думаешь, она сможет под каким-нибудь предлогом после репетиции пойти к Руи домой?"

    show kaito_wxs normal1 at sd

    kw "Я думаю да. Они с Руи дружат ещё с детства."

    show kaito think0 at sd

    k "Хорошо, тогда тебе нужно будет поговорить с Нене. Нужно чтобы она сделала это завтра."

    kw "Хорошо, я тебя понял."

    show kaito srs0 at sd

    k "Теперь ты, [player_name]."

    k "Тебе нужно будет пробраться в мастерскую Руи и включить его компьютер, чтобы мы могли поддерживать связь."

    k "Тебе придётся оставить всякие знаки, на которые Руи не сможет обратить внимание, но Нене заметит." 
    
    k "Я тебе дам подробную инструкцию, что нужно сделать, когда ты включишь компьютер. Сейчас я пока не уверен."

    show kaito think0 at sd

    k "Ещё я боюсь, что Руи может тебя просто запереть в комнате..."

    show kaito_wxs srs1 at sd

    kw "В спальне у Руи достаточно хлипкий замок, насколько я знаю. {w}Один удар по ручке чем-то тяжёлым - и замка нет."

    show kaito happy0 at sd

    k "Отлично! Тогда завтра с утра, когда Руи уйдёт на репетицию, тебе нужно выломать замок, найти мастерскую Руи и включить компьютер."

    k "Затем я тебе скажу, что нужно делать дальше. Думаю, Руи не уйдёт надолго, к тебя будет от силы 2 часа."

    k "Ты поняла, [player_name]?"

    menu:

        "Да, я поняла" if mind_value < 900:

            $ kaito_state += 10

            p "Да, я поняла..."

            k "Отлично. "

            show kaito tuch0 at sd
            
            extend "Всё будет хорошо, [player_name]. У тебя всё получится"

            if mind_value < 600:
                $ mind(200, "+")
                p "Да..."

            "Кайто нежно и осторожно гладит вас по голове, будто желая успокоить и придать сил."

            show kaito happy0 at sd

            p "Спасибо."

            show kaito_wxs happy1 at sd

            kw "Что ж, тогда удачи. Тебе лучше выспаться перед завтрашним днём. Мы тебя обязательно спасём, [player_name]."

            k "Угу."

        "Я не буду это делать":

            p "Я не буду это делать."

            show kaito_wxs shock1 at sd
            show kaito shock0 at sd

            k "Что?"

            kw "Но почему, [player_name]?"

            menu:

                "Мне и так хорошо":

                    $ kaito_state -= 20

                    p "Мне и так хорошо... Кто вам вообще сказал, что мне нужна помощь?"

                    show kaito_wxs sad1 at sd

                    kw "..."

                    show kaito angry0 at sd

                    k "[player_name], ты действительно так считаешь?.."

                    p "..."

                    k "Останешься с ним - поставишь крест на своём будущем. Неужели ты действительно этого хочешь?"

                "Я вам не доверяю":

                    $ mind(50, "-")

                    $ kaito_state -= 15

                    p "Я вам не доверяю... Вы не пойми кто, затащили меня не пойми куда."

                    show kaito_wxs sad1 at sd

                    kw "[player_name], послушай, у всех, кто попадал в Секай была похожая реакция, но мы правда хотим тебе помочь."

                    kw "Подумай, всё будет лучше, чем остаться с Руи..."

                    p "..."

                    show kaito angry0 at sd

                    k "[player_name], доверься нам... {w=0.5}Хотя бы в этот раз."                    

                "Вы - это моя шиза":

                    $ mind(100, "-")

                    $ kaito_state -= 5

                    p "Вы все лишь моя шиза! Неужели вы правда думали, что я поверю, что встретилась лично с Вокалоидами?"

                    p "Бред же! Очевидно, что я просто схожу с ума."

                    show kaito_wxs sad1 at sd

                    kw "[player_name]..."

                    show kaito tuch0 at sd

                    "Кайто осторожно протягивает руку и касается вашего плеча."

                    k "Я могу тебя прикоснуться, уверена ли ты то, что это галлюцинация?"

                    "Он осторожно хлопает вас по плечу, давай почувствовать тяжесть своей руки."

                    k "Если вдруг завтра ты сможешь сломать замок и включить компьютер в мастерской Руи, разве это не будет подтверждением того, что всё это не галлюцинация?"

                    show kaito think0 at sd

                    k "А если у тебя не получится, то ведь ничего не случится, ты ничего не потеряешь..."

                    show kaito angry0 at sd

                "...":

                    $ kaito_state -= 10

                    p "..."

                    show kaito_wxs sad1 at sd

                    kw "[player_name]... Слушай, какая бы не была причина мы действительно хотим тебе помочь..."

                    show kaito think0 at sd

                    k "Это так, [player_name]. Если ты попытаешься принять, помощь, то ты ведь ничего не потеряешь, так?"

                    show kaito angry0 at sd

            k "Хорошо подумай над этим. Мы сделаем то, что сказали. Принять помощь или нет - твой выбор, конечно, но я надеюсь, что ты выберишь верный вариант."

            kw "..."

            k "Спокойной ночи, [player_name]."

    # руи: 150 -25 рассудок: 1000 0 кайто: 160 50

    call kaito_list_lable("sekai") from _call_kaito_list_lable_13

    window hide
    
    stop music
    play sound "audio/ui_sfx/choice.flac"
    scene expression Solid("#fff") with test

    pause 2.0
    play music night fadein 5.0 volume 0.7

    scene bg rui phone un
    with Dissolve(5.0)

    window show

    p "Уфф... {w=0.3}И что это по итогу было..."

    p "Нужно положить телефон на место и вернуться в кровать."

    window hide

    pause 0.5
    show bg rui phone take with Dissolve(.2)
    pause 0.5
    show bg rui phone with Dissolve(.2)

    pause

    play sound steps
    scene black with Dissolve(.3)

    pause 3.0

    play sound undress
    pause 0.8
    window show

    "Ложась в кровать вы моментально засыпаете и проспите до утра."

    stop music fadeout 1.0
    window hide

    jump good_moning

# утрооо
label good_moning:

    if mind_value < 600:
        $ mind(100, "+")

    pause
    window auto
    
    r "[player_name]..."

    r "[player_name]~"

    play music rui_home fadein 1.0 volume 0.7

    scene bg rui moning1
    show blank at blink_open_more

    p "Мх..."

    r "Доброе утро, [player_name]~\nКак спалось?"

    menu:

        "Хорошо" if mind_value > 300:

            $ rui_state += 10

            p "Доброе утро... Хорошо..."

            show bg rui moning1:
                "bg rui moning2" with Dissolve(.2)

            r "Я рад."

        "Ужасно" if mind_value < 850:

            $ rui_state -= 10

            p "Ужасно... Как я ещё могла спать после того, что ты сделал?"

            show bg rui moning1:
                "bg rui moning3" with Dissolve(.2)

            r "..."

        "..." if 50 < mind_value < 1000:

            $ rui_state -= 5

            p "..."

            show bg rui moning1:
                "bg rui moning3" with Dissolve(.2)

            r "[player_name]..."

    # руи: 160 -35 рассудок: 1000 0 кайто: 160 50

    r "Мне нужно сходить на репетицию с WxS. Это займёт всего часа 2, не больше... Я приготовил завтрак и оставил его на столе в этой комнате."

    if rui_state > 120:

        r "Я доверяю тебя, [player_name]. Веди себя хорошо, пока меня не будет..."

        p "Хорошо..."

        show bg rui bedroom roof with Dissolve(.2)

        "Руи выходит из комнаты, не закрывая дверь, вы прислушиваетесь к звукам, ожидая, когда он уйдёт из дома."

        $ door = True

    else:

        r "Я закрою тебя в этой комнате на это время, [player_name]."

        r "Прости, но я не могу пока тебе доверять..."

        p "..."

        play sound [steps, door]

        show bg rui bedroom roof with Dissolve(.2)

        "Руи выходит из комнаты и закрывает дверь, вы прислушиваетесь к звукам, ожидая, когда он уйдёт из дома."

        stop sound

        $ door = False

    stop music fadeout 5.0

    p "Он ушёл..."

    $ rui_time = 120
    $ locate = "bed"
    $ score = 0

    show screen rui_timer

    p "У меня есть два часа... Думаю, мне нужно внимательно отнестись к этому времени..."

    "За временем вы можете следить по таймеру рядом с индикатором рассудка."

    play music doomed fadein 1.0 volume 0.6

    label .wake:

        p "..."

        menu:

            "Вставать":

                $ locate = "bedroom"

                p "Нужно уже просыпаться и обдумывать план действий..."

            "Полежать ещё немного":

                p "Лучше полежу ещё немного..."

                window hide

                hide screen rui_timer
                show black
                with Dissolve(.5)

                $ mind(100, "+")

                pause 1.5

                $ rui_time -= 30
                if rui_time <= 0:
                    jump rui_return

                hide black 
                show screen rui_timer
                with Dissolve(.5)

                jump good_moning.wake

    window hide

    play sound undress
    scene black with Dissolve(.2)

    pause 2.0

    $ vafli = True

    scene bg rui bedroom moning
    show m2
    show m3
    show m4
    show vaf2
    with Dissolve(.2)

    pause

    window show

    p "На столе лежат вафли... Стоит ли поесть или лучше не тратить на это время?"

    menu:

        "Есть":

            $ vafli = False
            $ rui_state += 5

            p "Ладно, поесть всяко будет лучше..."

            hide screen rui_timer
            show black
            with Dissolve(.2)

            hide vaf2

            play sound eat volume 2.0

            $ mind(100, "+")

            "Вы стараетесь позавтракать как можно быстрее."

            $ rui_time -= 15
            if rui_time <= 0:
                jump rui_return

            hide black 
            show vaf1
            show screen rui_timer
            with Dissolve(.2)

            "Да, так лучше..."

        "Не есть":

            $ rui_state -= 5

            p "Не, лучше не буду есть, это займёт слишком много времени."

    # руи: 165 -40 рассудок: 1000 0 кайто: 160 50

    p "Кайто просил, чтобы я пробралась в мастерскую Руи и включила там компьютер... Стоит ли это делать или лучше остаться в комнате и дождаться Руи?.."

    menu:

        "Пойти в мастерскую" if mind_value < 1000:

            p "Была не была, это всяко лучше, чем сидеть сложа руки..."

        "Остаться в комнате":

            p "Мм..."

            p "Я лучше тут останусь... Зачем лишний раз так рисковать?.."

            window hide

            if not door:
                $ rui_state += 15

            scene black
            hide screen rui_timer
            with Dissolve(.3)
            $ locate = "bed"
            play sound undress

            window show

            "Вы ложитесь обратно в кровать и дожидаетесь прихода Руи..."

            jump rui_return

    $ talk_kaito = False
    $ done = False
    $ locates = ['studio', 'room', 'bedroom', 'toilet', 'kitchen']

    if door:
        "Дверь открыта, так что вы без проблем вышли из комнаты."
        with Dissolve(.3)
    else:

        "Хмм.. он закрыл дверь, нужно бы придумать как её можно открыть от сюда..."

        window hide

        hide m2
        hide m3
        hide m4
        hide vaf2
        show screen rui_moning

        $ renpy.pause(hard=True)

        label .vaf:
            "Это точно будет бесполезно тут..."
            $ renpy.pause(hard=True)
        label .m4:
            show bomb:
                yalign 3.0 xalign 0.5
                easein 0.6 yalign 1.0
            pause 0.4
            window show
            "Это просто какие-то чертяжи Руи, они не имеют значения..."
            show bomb:
                ease 0.3 alpha 0.0
            window hide
            pause 0.3
            hide bomb
            $ renpy.pause(hard=True)
        label .m3:
            "Вы берёте вазу с цветами в руки."
            p "Хм..."
            play sound glass volume 1.3
            "Вы кидаете её, целясь в ручку."
            "Очевидно, нихуя не получилось и вы просто разбили вазу..."
            window hide
            $ renpy.pause(hard=True)
        label .m2:

            $ rui_state -= 10

            "Вы берёте книгу в руки и начинаете ебашить ей по ручке двери."

            play sound knock3

            "..."

            play sound knock3

            "..."
            
            "Ебать нахуй, оно реально открытолось!"

    "Сейчас вам нужно направиться в мастерскую Руи..."

    window hide

    $ tasks = {'studio': [False],
        'room': [False, False, False],
        'bedroom': [False],
        'toilet': [False, False],
        'kitchen': [False, False, False]}

    $ can_card = True

    show screen card_button
    show screen rui_home_scheme
    hide screen rui_moning
    with Dissolve(.8)

    pause

    # руи: 180 -50 (сер:65) рассудок: 1000 0 кайто: 160 50

    return

label rui_studio:

    if rui_time <= 0:
        jump rui_return

    $ can_card = False
    $ locate = 'studio'
    stop music fadeout 3.0
    scene black
    hide screen r_bedroom
    hide screen r_room
    hide screen r_studio
    hide screen r_kitchen
    hide screen r_toilet
    hide screen rui_home_scheme
    with Dissolve(.3)

    window hide

    play sound steps

    pause 3.0

    play music iakes fadein 1.0

    scene bg rui room with Dissolve(.3)

    if not talk_kaito:

        $ rui_state -= 1

        p "Вот я и здесь..."

        "Вы решительно подходите к компьютеру и включаете его."

        show kaito happy:
            xalign 0.5 alpha 0.0 matrixcolor TintMatrix("#449effff")
            ease 0.3 alpha 0.7

        p "!!!"

        p "Ой, испугал меня..."

        show kaito smile at sd

        k "Я рад, что ты пришла, [player_name]~"

        show kaito srs at sd

        k "Но ближе к делу, нельзя просто так терять время."

        k "Первое что тебе нужно запомнить: тебе нужно вернуться в спальну до того как Руи вернёся домой. Поняла?"

        p "Угу..."

        show kaito think at sd

        k "Твоя задача крайне проста: пройтись по всем комнатам в доме и оставить там следы своего существования."

        k "Это может быть всё что угодно: скрытая надпись, помятый насок в стопке идеально сложенной одежды..."

        k "Всё, что может заметить человек, если будет всматриваться, но не такое заметное, чтобы сразу бросалось в глаза."

        show kaito srs at sd

        k "Вакай уже поговорил с Нене, она придёт, но крайне сомневается в том, можно ли нам верить..."

        k "Поэтому наша задача убедить её в том, что это правда, чтобы она могла действовать резко и чётко."

        k "Это понятно, [player_name]?"

        p "Да.. Ага, вроде..."

        show kaito think at sd

        k "Ах..."

        k "Ещё раз: тебе нужно оставить за собой следы, но успеть вернуться до того, как придёт Руи."

        k "Можешь вернуться ко мне сюда по окончанию, а можешь и не возвращаться, я самсмогу выключить компьютер."

        show kaito tuch at sd

        k "Удачи, [player_name], я в тебя верю~"

        call kaito_list_lable("pc") from _call_kaito_list_lable_14

        show kaito tuch:
            ease 0.3 alpha 0.0

        p "..."

        $ talk_kaito = True

        window hide

    show screen r_studio

    $ can_card = True

    $ renpy.pause(hard=True)

    label .kaito_tell:

        $ can_card = False

        show kaito srs:
            xalign 0.5 alpha 0.0 matrixcolor TintMatrix("#449effff")
            ease 0.3 alpha 0.7

        k "Да? Тебе нужна какая-то помощь, [player_name]?"

        menu:

            "Да":

                "Вы киваете головой."

                $ n = sum(value is False for task_list in tasks.values() for value in task_list)

                $ name = {'studio': 'мастеркой',
                        'room': "зале",
                        'bedroom': "спальне",
                        'toilet': "ванной комнате",
                        'kitchen': "кухне"}

                $ x = ", ".join([v for key, v in name.items() if key in [key for key, values in tasks.items() if not all(values)]])

                show kaito think at sd

                if n != 0:

                    k "Хмм... постарайся оставить ещё [n] следов."

                    k "Посмотри ещё в [x]."

                else:

                    k "Хмм... Я думаю уже достаточно, возвращайся в спальню, пока Руи не вернулся..."

            "Нет":

                "Вы мотаете головой."

                k "Хорошо, если что, обращайся."

        show kaito tuch at sd

        k "Удачи, [player_name]~"
        
        show kaito tuch:
            ease 0.2 alpha 0.0

        $ can_card = True

        $ renpy.pause(hard=True)

    label .shema:

        menu:

            "Оставить записку в чертяжах?"

            "Да":

                $ tasks['studio'][0] = True
                $ score += 1
                $ rui_state -= 1

                "Вы пишите записку о помощи и прицепляете её к остальным чертяжам Руи"

            "Нет":

                pass

        $ can_card = True

        $ renpy.pause(hard=True)

    return


label rui_room:

    if rui_time <= 0:
        jump rui_return

    $ can_card = False
    $ locate = 'room'
    stop music fadeout 3.0
    scene black
    hide screen r_bedroom
    hide screen r_room
    hide screen r_studio
    hide screen r_kitchen
    hide screen r_toilet
    hide screen rui_home_scheme
    with Dissolve(.3)

    window hide

    play sound steps

    pause 3.0

    play music rui_home fadein 1.0

    scene bg rui living room with Dissolve(.3)

    show screen r_room

    $ can_card = True

    $ renpy.pause(hard=True)

    label .book:

        menu:

            "Изменить порядок книг?"

            "Да":

                $ tasks['room'][0] = True
                $ score += 1
                $ rui_state -= 1

                "Вы перемещаете книги так, что первые буквы состовляют слово SOS."

            "Нет":
                pass

        $ can_card = True

        $ renpy.pause(hard=True)

    label .vaza:

        menu:

            "Написать на сбоку на вазе послание?"

            "Да":

                $ tasks['room'][1] = True
                $ score += 1
                $ rui_state -= 1

                "Вы выскрёбываете ногтем послание SOS сбоку на вазе."

            "Нет":
                pass

        $ can_card = True

        $ renpy.pause(hard=True)

    label .lampa:

        menu:

            "Перерезать провода лампе?"

            "Да":

                $ tasks['room'][2] = True
                $ score += 1
                $ rui_state -= 3

                "Вы перерезали провода лампе."

            "Нет":
                pass

        $ can_card = True

        $ renpy.pause(hard=True)

    return

label rui_bedroom:

    if rui_time <= 0:
        jump rui_return

    $ can_card = False
    $ locate = 'bedroom'
    stop music fadeout 3.0
    scene black
    hide screen r_bedroom
    hide screen r_room
    hide screen r_studio
    hide screen r_kitchen
    hide screen r_toilet
    hide screen rui_home_scheme
    with Dissolve(.3)

    window hide

    play sound steps

    pause 3.0

    play music ruistart fadein 1.0

    scene bg rui bedroom moning with Dissolve(.3)

    menu:

        "Лечь в кровать и дождаться возвращения Руи?"

        "Да":
            $ locate = 'bed'

            jump rui_return

        "Нет":
            pass

    show screen r_bedroom

    $ can_card = True

    $ renpy.pause(hard=True)

    label .sh:

        menu:

            "Кинуть футболку рядом с дверью с другой стороны?"

            "Да":

                $ tasks['bedroom'][0] = True
                $ score += 1
                $ rui_state -= 5

                "Вы берёте, сминаете и кидаете футболку Руи с другой стороны двери."

            "Нет":
                pass

        $ can_card = True

        $ renpy.pause(hard=True)

    return

label rui_kitchen:

    if rui_time <= 0:
        jump rui_return

    $ can_card = False
    $ locate = 'kitchen'
    stop music fadeout 3.0
    scene black
    hide screen r_bedroom
    hide screen r_room
    hide screen r_studio
    hide screen r_kitchen
    hide screen r_toilet
    hide screen rui_home_scheme
    with Dissolve(.3)

    window hide

    play sound steps

    pause 3.0

    play music kitchen fadein 1.0

    scene rkitchen with Dissolve(.3)

    show screen r_kitchen

    $ can_card = True

    $ renpy.pause(hard=True)

    label .food:

        menu:

            "Рассыпать еду?"

            "Да":

                $ tasks['kitchen'][0] = True
                $ score += 1
                $ rui_state -= 10

                "Вы рассыпаете хдопья и специи по полу."

            "Нет":
                pass

        $ can_card = True

        $ renpy.pause(hard=True)

    label .wt:

        menu:

            "Перелить воду в мультиварку?"

            "Да":

                $ tasks['kitchen'][1] = True
                $ score += 1
                $ rui_state -= 1

                "Вы переливаете воду в мультиварку... Это явно самое странное, что вы делали"

            "Нет":
                pass

        $ can_card = True

        $ renpy.pause(hard=True)

    label .kn:

        menu:

            "Воткнуть нож в доску?"

            "Да":

                $ tasks['kitchen'][2] = True
                $ score += 1
                $ rui_state -= 2

                "Вы втыкаете нож в доску."

            "Нет":
                pass

        $ can_card = True

        $ renpy.pause(hard=True)

    return

label rui_toilet:

    if rui_time <= 0:
        jump rui_return

    $ can_card = False
    $ locate = 'toilet'
    stop music fadeout 3.0
    scene black
    hide screen r_bedroom
    hide screen r_room
    hide screen r_studio
    hide screen r_kitchen
    hide screen r_toilet
    hide screen rui_home_scheme
    with Dissolve(.3)

    window hide

    play sound steps

    pause 3.0

    play music doomed fadein 1.0

    scene bg bathroom with Dissolve(.3)

    show screen r_toilet

    $ can_card = True

    $ renpy.pause(hard=True)

    label .pl:

        menu:

            "Помять полотенце?"

            "Да":

                $ tasks['toilet'][0] = True
                $ score += 1
                $ rui_state -= 1

                "Вы помняли полотенце, теперь они весят безобразно."

            "Нет":
                pass

        $ can_card = True

        $ renpy.pause(hard=True)

    label .ml:

        menu:

            "Написать мылом послание?"

            "Да":

                $ tasks['toilet'][1] = True
                $ score += 1
                $ rui_state -= 2

                "Вы пишите мылом послание о помощи."

            "Нет":
                pass

        $ can_card = True

        $ renpy.pause(hard=True)

    return