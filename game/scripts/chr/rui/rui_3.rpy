# игрок остался в пижаме
label pizhama:

    play sound knock2
    queue sound knock2

    p "Если это орифлейм, то я пожалуюсь на них Руи."

    window hide

    scene black with dissolve

    pause 1.5

    scene bg corridor with dissolve

    pause 0.5

    stop music fadeout 1.5

    if persistent.kaito_int > 0 and not persistent.showkaito_rui:

        show tsukasa hard with Dissolve(.3)

        voice k_aa
        show tsukasa likekaito1

        call kaito_list_lable("show") from _call_kaito_list_lable_3

        $ persistent.showkaito_rui = True
    
    else:

        show tsukasa hard with Dissolve(.3):
            xalign 0.5

    window show

    pause 0.5

    p "..."

    play music tsu fadein 1.5

    p "Э? {w=1}Цукаса?"

    show tsukasa hard say at sd

    ts "Ты сейчас одна дома? {w=1}Мне нужно с тобой поговорить."

    p "Странно видеть тебя с таким серьёзным лицом... {w=0.5}Что-то случилось?"

    show tsukasa hard at sd

    ts "..."

    ts "Это насчёт Руи."

    p "Э?"

    p "А что с ним не так?.."

    ts "Не притворяйся, ты ведь сама всё понимаешь..."

    ts "Я могу пройти?"

    menu:

        "Тебе лучше уйти":

            jump tsu_goaway

        "Зачем? Говори здесь":

            jump tsu_say_now

        "Да, проходи":

            $ za_tsu += 4

            p "Да, конечно, проходи."

            jump tsu_welcom

    return

# гг просит уйти цукасу
label tsu_goaway:

    p "Цукаса, тебе лучше уйти..."

    show tsukasa shock at sd

    ts "А? [player_name]? У тебя всё хорошо..."

    p "Уйди. {w=0.5}Просто уйди..."

    show tsukasa srs at sd
    
    ts "..."

    ts "Ты боишься Руи?"

    p "..."

    p "Это неважно, тебе нужно уйти. Сейчас же!"

    show tsukasa hard at sd

    ts "[player_name]! Ваши отношения с Руи не нормальны. Ты не должна потакать ему, ты не должна бояться его."

    p "Заткнись!"

    show tsukasa shock at sd

    ts "..."

    p "У нас с Руи всё хорошо! Он меня любит больше всего мира... И я тоже его люблю..."

    p "Не лезь не в своё дело!" with hpunch

    show tsukasa hard say at sd

    ts "Вот оно что..."

    show tsukasa hard at sd

    ts "Но действительно ли ты уверена в своих чувствах?"

    p "Уйди... Уйди... Я хочу видеть только Руи, только его."

    ts "[player_name]..."

    show tsukasa hard zorder 1

    show rui lom zorder 0:
        xalign 0.3 alpha 0.0
        linear 0.1 alpha 1.0

    p "Цукаса!"

    play sound udar2
    with hpunch

    stop music

    window hide

    scene black with fade

    pause 1.0

    window show

    $ rui_pain_add('14')

    r "[player_name]!"

    r "Ты в порядке, [player_name]?"

    window hide

    scene bg cor1
    show rui cor1
    with dissolve

    window show

    r "Прости, я тебя слегка задел..."

    p '"Слегка задел"...'

    p "Что с Цукасой?!"

    scene bg ts die with fade

    play music dillema fadein 0.5

    p "Цукаса!"

    show rui sad:
        xalign 0.3 alpha 0.0
        linear 0.3 alpha 1.0

    r "..."

    show rui sad:
        alpha 1.0

    r "Он ведь к тебе лез? Я слышал твои крики..."

    p "Он мёртв?! Руи, ты его убил?"

    r "Наверное."

    p "Руи, ты убийца?! Как... аа... что будет теперь..."

    r "[player_name]! Успокойся!"

    show rui hello at sd

    r "Всё уже позади, он больше не сможет причинить тебе вред..."

    p "Вред? О чём ты... {w=0.5}Ты своего друга убил!"

    show rui angry at sd

    r "Да поебать мне!"

    show rui crazy2 at sd

    r "[player_name], я сделал это только ради тебя! Если б не я, кто знал бы какие ужасные вещи он мог вытворить с тобой."

    r "Я понимаю, ты сейчас можешь быть напугана, но со временем страх уйдёт и ты осознаешь, что это было просто необходимо."

    show rui hello at sd

    r "Всё будет хорошо, [player_name], я всё улажу."

    r "Ты можешь жить у меня, если теперь твой дом ассоциируется со смеретью..."

    p "Руи..."

    menu:

        "Ты можешь вытворить со мной вещи и пострашнее":

            p "Ты можешь вытворить со мной вещи и пострашнее..."

            show rui sad at sd

            p "Как я могу тебе доверять, после того как ты убил своего друга?"

            p "Жить с тобой в одном доме - это как мина в неизвестном месте. Каждое моё действие - рискованный ход."

            p "Если ты без колебаний смог убить того, кого знал несколько лет, то и меня без проблем прибить сможешь..."

            r "[player_name]..."

            r "Я никогда не причиню тебе вред!"

            show rui blush at sd

            r "Я люблю тебя больше мира, [player_name]! Ты для меня всё и если понадобится, то я готов даже умереть ради тебя!"

            p "..."

            menu:

                "Тогда убейся":

                    jump ubeysa

                "...":

                    p "..."

                    show rui sad at sd

                    r "[player_name]..."

                    r "Ты теперь боишься меня, [player_name]?"

                    p "Я..."

                    p "М..."

                    show rui shock at sd

                    r "[player_name], ответь мне!"

                    menu:

                        "Оставь меня в покое!":

                            p "Руи, отстань от меня! Не трогай меня! Ты, итак, уже достаточно сделал..."

                            show rui sad at sd

                            r "..."

                            r "Ничего ведь страшного не произошло... Мы можем продолжить встречаться так же, как и раньше... Разве нет?"

                            p "По-твоему убийство Цукасы - ничего страшного? Руи... {w=1}Я разочарована в тебе, Руи..."

                            show rui shock at sd

                            r "А?!"

                            r "..."

                            show rui panic1 at sd

                            r "Ясно..."

                            r "[player_name]... Ты ведь знаешь как сильно я тебя люблю..."

                            show bg ts die2 with Dissolve(0.3)

                            p "..."

                            show rui panic1:
                                linear 0.15 xalign 0.5 yalign 0.53 zoom 1.2

                            pause 0.1

                            show rui home poh with Dissolve(0.07):
                                zoom 1.0

                            r "{sc=6}{=norm_style}Я не могу позволить тебе просто так уйти от меня!{/sc}{w=0.2}{nw}"

                            window show

                            p "Руи!{w=0.2}{nw}"

                            play sound udar2
                            with hpunch

                            $ rui_pain_add('15')

                            stop music

                            scene black
                            with Dissolve(.3)

                            $ rui_psyho = True

                            jump rui_home_poh

                        "Мне страшно...":

                            p "Мне страшно... {w=1}Что теперь будет?..."

                            show rui hello say at sd

                            r "Я понимаю, это большой шок для тебя, но я рядом. Мы справимся с этим вместе."

                            show rui hello at sd

                            p "..."

                            r "Тебе нужно сделать сейчас выбор... Ты переедешь ко мне или нет?"

                            menu:

                                "Да...":

                                    p "Да... Так будет лучше для меня... {w=1}Я так думаю..."

                                    r "Отлично! Тогда иди пока в машину, я разберусь с трупом. Не оставлять же его просто так."

                                    p "Да..."

                                    jump go_rui_home

                                "Я лучше останусь у себя дома...":

                                    p "Я лучше останусь у себя дома..."

                                    show rui sad at sd

                                    r "Хорошо... Я понимаю."

                                    r "Иди пока что в свою комнату, я разберусь с Цукасой..."

                                    p "..."

                                    jump tsu_die

                                "Я не могу встречаться с убийцей":

                                    p "Я не могу так больше, Руи..."

                                    p "Ты убил Цукасу! Ты убил своего друга! Я не могу встречаться с убийцей... {w=1}Между нами всё кончено!"

                                    show rui shock at sd

                                    r "..."

                                    show rui panic1 at sd

                                    r "Ясно... {w=1}Да, я... {w=2}понимаю тебя..."

                                    r "Но, [player_name]... {w=2}Ты ведь знаешь как сильно я тебя люблю... {w=2}Ты ведь знаешь..."

                                    show bg ts die2 with Dissolve(0.3)

                                    r "Я не могу позволить, чтобы всё так закончилось...{w=0.5}{nw}"

                                    show rui panic1:
                                        linear 0.1 xalign 0.5 yalign 0.53 zoom 1.2

                                    pause 0.05

                                    show rui home poh with Dissolve(0.05):
                                        zoom 1.0

                                    r "{sc=6}{=norm_style}Я не могу позволить тебе просто так уйти от меня!{/sc}{w=0.2}{nw}"

                                    window show

                                    $ rui_pain_add('16')

                                    p "Руи!{w=0.2}{nw}"

                                    play sound udar2
                                    with hpunch

                                    stop music

                                    scene black with Dissolve(.3)

                                    $ rui_psyho = True

                                    jump rui_home_poh

                "Я верю тебе":

                    p "Ладно, Руи, я поверю тебе..."

                    show rui hello at sd

                    r "Отлично! Так что ты выберешь? Останешься у себя или переедешь ко мне?"

                    menu:

                        "Я останусь у себя":

                            p "Я думаю, мне лучше всё же остаться у себя..."

                            r "Хорошо, я понимаю..."

                            r "Иди пока что в свою комнату, я разберусь тут..."

                            jump tsu_die

                        "Я перееду к тебе":

                            p "Думаю, мне лучше переехать к тебе..."

                            show rui blush at sd

                            r "Хорошо... {w=1}Я рад, что мы думаем одинаково."

                            show rui hello at sd

                            r "Иди пока что в машину. Я разберусь с трупом Цукасы... Не стоит его бросать так здесь.."

                            p "Да... {w=0.5}Хорошо..."

                            jump go_rui_home

        "Я не хочу уходить из своего дома...":

            p "Но я не хочу уходить из своего дома..."

            r "Я понимаю... {w=1}Ты можешь остаться тут, я позабочусь о всех деталях."

            p "Руи..."

            show rui sad at sd

            r "Не бойся, всё будет хорошо, я обо всём позабочусь..."

            show rui hello at sd

            r "Иди пока что в свою комнату."

            p "..."

            jump tsu_die

        "Хорошо, я перееду к тебе":

            p "Хорошо... Я перееду к тебе... {w=1}Думаю, так будет лучше для меня..."

            r "Я рад, что ты так думаешь. Не бойся, я всё улажу, всё будет хорошо.."

            p "Ладно..."

            jump go_rui_home

    return

# гг сказала руи убиться <3 (КОНЦОВКА)
label ubeysa:

    p "Тогда убейся. {w=1}Докажи, что ты реально готов на всё ради меня"

    show rui shock at sd

    r "[player_name]... {w=0.5}Ты это сейчас серьёзно?"

    p "Да."

    r "Но это не имеет какого-либо смысла, нет причины по которой мне сейчас стоит умереть..."

    menu:

        p "..."

        "Это была шутка":

            $ haha_add('2')

            p "Ахахахахахаххахахахахахах, Руи, это была шутка!"

            r "..."

            show rui happy at sd

            r "Пиздец, [player_name], что за хуйня? Ты меня жесть как напугала."

            p "Ахахах."

            show rui hello at sd

            r "Хе-хе, ну хоть шутить не разучилась. Юмор - это хорошо, это полезно."

            p "Чт..."

            r "В любом случае, что ты думаешь насчёт того, что я сказал?"

            p "Хм.."

            menu:

                "Я буду жить у тебя":

                    p "Думаю, мне будет лучше пожить у тебя..."

                    show rui hello say at sd

                    r "Хорошо. {p=1}Можешь пока что некоторое время посидеть у себя в комнате? {w=2}Мне стоит разобраться с трупом сейчас."

                    p "Хорошо..."

                    jump go_rui_home

                "Я останусь у себя дома":

                    p "Я лучше останусь у себя дома..."

                    r "Я понимаю."

                    r "Иди пока что в свою комнату, я разберусь с трупом."

                    p "Хорошо.."

                    $ joke_tsu_die = True

                    jump tsu_die

        "Я серьёзно":

            p "Руи, я говорю на полном серьёзе."

    show rui sad at sd

    p "Ты разве не хочешь, чтобы я была счастлива?.. {w=0.5}А ведь это сделает меня очень счастливой..."

    p "Заставь меня сиять, Руи!"

    show rui panic1 at sd

    r "Хорошо, [player_name]..."

    show rui panic1:
        linear 0.1 xalign 0.5 yalign 0.53 zoom 1.2

    pause 0.05

    show rui ubeysa1 at none with Dissolve(0.05):
        yalign 1.0 xalign 0.5 zoom 1.0

    r "{sc}{=norm_style}Но только ты пойдёшь вместе со мной!{/sc}" with hpunch

    p "Руи! У тебя биполярка или что? Ты ведь говорил, что не причинишь мне вред!"

    r "В отношениях всегда должны быть счастливы обе стороны."

    r "Ты хочешь, чтобы я умер. Я хочу, чтобы мы навсегда были вместе.. до самой смерти...."

    show rui ubeysa2 at sd

    r "Если мы умрём вместе, то эти два желания будут исполнены, разве нет?"

    p "Ну ахуеть логика..."

    p "Стой! Руи!"

    scene black with fade

    pause 0.5

    $ rui_pain_add('17')

    "После Руи нажал на красную кнопку..."

    "Это был пульт от его карманной ядерной бомбы."

    "Очевидно, вы сдохли вместе с ним."

    window hide

    pause 0.5

    call ends_rui("ubeysa") from _call_ends_rui_7

    pause 2.0

    return

# гг остаётся дома, отношения те же, но Цукаса сдох (КОНЦОВКА)
label tsu_die:

    stop music fadeout 1.0
    play music low

    scene bg room with Fade(0.3, 0.5, 0.3)

    window show

    "Прошло около часа..."

    "В начале вы слышали как Руи убирает труп, но в последние 15 минут не было слышно никаких звуков..."

    p "..."

    show rui sad at right:
        alpha 0.0
        linear 0.3 alpha 1.0

    show rui sad at right:
        alpha 1.0

    r "[player_name]..."

    show rui hello:
        linear 0.3 xalign 0.5 zoom 1.1

    r "Ты в порядке?"

    p "Я..."

    $ config.menu_include_disabled = False

    menu:

        "Да":

            p "Да... Наверное..."

            show rui happy at sd

            r "Рад это слышать."

            r "Я купил тебе мороженого, чтобы тебе стало легче. {p=1}Насчёт трупа можешь не переживать: я подстроил всё под несчастный случай."

            p "Хорошо..."

        "Не знаю...":

            p "Я не знаю..."

            show rui sad at sd

            r "Я понимаю, это может быть тяжело..."

            show rui hello say at sd

            r "Я купил тебе мороженого, чтобы тебе стало легче. {p=1}Насчёт трупа можешь не переживать: я подстроил всё под несчастный случай."

            show rui hello at sd

            p "..."

            r "Всё будет хорошо, я обещаю..."

        "Нет" if not joke_tsu_die:

            p "Как я могу быть в порядке после этого?.."

            show rui sad at sd

            r "[player_name]..."

            p "Ты убил его... Ты действительно убил его..."

            r "Я..."

            menu:

                "Ты монстр!":

                    p "Ты монстр, Руи!"

                    show rui shock at sd

                    p "Неужели тебя вообще не мучает совесть, чмо ты ёбаное!"

                    r "..."

                    p "Я ненавижу тебя!"

                    show rui angry at sd

                    r "Ясно..."

                    r "Значит я тебе мороженое покупаю, а ты тут истерику устраиваешь."

                    p "Какое мороженое? Ты Цукасу убил!"

                    r "И чо?"

                    p "Ну типо соси... {w=0.5}точнее иди нахуй, я тебя боюсь."

                    r "..."

                    r "Я не хотел этого делать..."

                    p "..."

                    show rui angry:
                        linear 0.2 yalign 0.4 zoom 1.4

                    pause 0.08

                    show rui lom with Dissolve(0.08)

                    window show

                    $ rui_pain_add('18')

                    p "Руи, стой!{nw}"

                    play sound udar2
                    with hpunch

                    stop music

                    scene black with Dissolve(.3)

                    $ config.menu_include_disabled = True

                    $ rui_psyho = True

                    jump rui_home_poh

                "Мне страшно":

                    p "Мне страшно... {w=1}Мне так страшно, Руи..."

                    r "Ох..."

                    show rui hello at sd

                    r "Не бойся, [player_name]... Всё будет хорошо, нас не найдут. Я всё подстроил под несчастный случай."

                    p "..."

                    r "Я купил тебе мороженого, чтобы тебе стало полегче."

                    p "Спасибо..?"

                    r "Всё будет хорошо..."

                "...":

                    p "..."

                    r "Ох..."

                    r "Я понимаю тебя, но всё будет хорошо, я обещаю..."

                    r "Я подстроил смерть Цукасы под несчастный случай, мы в безопасности."

                    p "..."

                    show rui hello at sd

                    r "Я купил тебе мороженого, чтобы тебе стало легче. Пойдём."

                    p "Да..."

    scene black with dissolve

    $ config.menu_include_disabled = True

    "После этого ваши отношения с Руи никак не изменились, будто бы ничего и не произошло..."

    "Но Цукаса умер... {w=1}Веченая память(завтра забудем)"

    window hide

    pause 0.5

    call ends_rui("tsu_die") from _call_ends_rui_8

    pause 2.0

    return

# гг говорит цукасе сказать на месте
label tsu_say_now:

    p "Зачем? Говори здесь."

    show tsukasa srs at sd

    ts "Это может быть небезопасно... Да и диалог не на пару минут..."

    p 'Что значит "Небезопасно"?..'

    show tsukasa hard say at sd

    ts "Меня напрягают ваши с Руи отношения... Меня напрягает то, что с ним стало и то, как он к тебе относится..."

    show tsukasa hard at sd

    p "Что ты имеешь в виду?"

    ts "Он слишком помешан на тебе. Он стал слишком ревнивым... и... Я видел в его рюкзаке кучу твоих фотографий, сделанных явно исподтишка. {w=1}Я думаю, он сталкерит за тобой."

    p "М..."

    ts "[player_name]... Я думаю, ему стоит обратиться к специалисту, пока ещё не поздно. Мы можем обсудить с тобой это?"

    menu:

        "Да, проходи":

            $ za_tsu += 2

            p "Да... Проходи..."

            $ tsu_lit_know = True

            jump tsu_welcom

        "Ты лазил в его рюкзаке?":

            $ za_rui += 1

            p "Погоди... Ты лазил в его рюкзаке?"

            show tsukasa shock at sd

            ts "Нет, что ты!"

            show tsukasa srs at sd

            ts "Ну... Точнее я мельком видел те фотографии и заглянул ему в рюкзак, чтобы подтвердить свою теорию..."

            p "Теорию?"

            show tsukasa hard say at sd

            ts "Мы с Руи дружим несколько лет... И я действительно переживаю за него.. {w=1}И за тебя тоже."

            show tsukasa hard at sd

            ts "..."

            menu:

                "У тебя просто паранойя":

                    $ za_rui += 2

                    p "Цукаса, у тебя просто паранойя. Наши отношения с Руи очень комфортные.{sc=2}{i}{color=#000000} Он просто не может быть сталкером.{/color}{/i}{/sc}"

                    show tsukasa srs at sd

                    ts "[player_name]... Ты действительно так думаешь?"

                    p "Да."

                    show tsukasa hard at sd

                    ts "..."

                    jump rui_back

                "Возможно, ты прав...":

                    $ za_tsu += 1

                    p "Хм... Возможно, ты в чём-то прав.."

                    ts "Спасибо за понимание, [player_name]..."

                    ts "Я..{w=0.2}{nw}"

                    jump rui_back
                
        "Мне кажется, ты преувеличиваешь":

            $ za_rui += 2

            p "Ты преувеличиваешь, Цукаса."

            show tsukasa shock at sd

            ts "[player_name]! Я серьёзно переживаю, как и за тебя, так и за него."

            p "У нас в отношениях с Руи всё хорошо, мы действительно любим друг друга!"

            show tsukasa hard say at sd

            ts hard say "Послушай... Раньше Руи был просто чудаковатый... Но сейчас он безумен. Неужели ты этого не замечаешь?"

            show tsukasa hard at sd

            p "..."

            ts "Я видел как он...{w=0.2}{nw}"

            jump rui_back


    return


# приходит руи
label rui_back:

    stop music fadeout 1.0

    show tsukasa hard zorder 1

    show rui angry zorder 0:
        xalign 0.8 yalign 1.0 alpha 0.0
        linear 0.2 alpha 1.0

    play music dark fadein 1.0

    r "Что у вас тут происходит?"

    show rui angry:
        alpha 1.0

    show tsukasa scream:
        linear 0.1 xalign 0.0

    ts "{cps=50}Ваааааааааа!{/cps}"

    show tsukasa srs0:
        yalign 1.0
        xalign 0.0

    show rui angry0

    r "Ну и?"

    p "Руи..."

    show rui sad0 at sd

    r "[player_name]... {w=1}Ты в порядке? Он не приставал к тебе?"

    p "Я..."

    menu:

        "Всё в порядке":

            $ za_tsu += 1

            p "Всё в порядке, Руи, не переживай."

            r "Хорошо..."

        "Он назвал тебя психом":

            $ za_rui += 1

            p "Он назвал тебя психом, Руи!"

            show tsukasa shock0 at sd

            ts "ЧТО? [PN]!"

            show rui angry0 at sd

            r "Вот значит как..."

            r "Что ты скажешь на это, Цукаса?"

            show tsukasa pain0 at sd

            ts "Руи... Я не это имел в виду.."

            show tsukasa srs0 at sd

            ts "Я лишь сказал, что волнуюсь за твоё состояние. Скажи, разве ты сам не замечаешь, как сильно ты изменился? Теперь ты стал ещё страннее обычного"

            r "Интересно, и в чём же проявляется моя странность?"

            ts "Ты стал более вспыльчив, одержим [pn_tp], реже стал видеться с нашей группой. Да даже сейчас..."

            show tsukasa hard0 at sd

            ts "Вот скажи, какого чёрта ты в 6 утра ходишь в этом своём костюме? {p=1}И тебе удобно в эти бархатных тягах?"

            r "Чт..."

            show rui panic0 at sd

            r 'Какого чёрта, тебя это вообще ебёт? {w=1}А что это ты сам как "вивид" оделся? Для тебя они лучше, чем наша команда?'

            show tsukasa shock0 at sd

            ts "Что ты несёшь, эта одежда просто удобная... И вообще..."

            show tsukasa ehe0 at sd

            ts "Неужели ты настолько поражён великим Тенмой Цукасей, что и его уже начал ревновать? Хе-хе!"

            play sound udar
            show tsukasa shock0 at sd

            ts "Ай!"

            show rui angry0 at sd zorder 2

            r "Хватит вести себя как придурок!"

            show tsukasa pain0 at sd

            ts "..."

            r "Уходи отсюда. Всё равно ничего толкового ты не скажешь."

            show tsukasa srs0 at sd

            ts "Хорошо... {p=1}*шепчет* [player_name], пожалуйста, будь осторожней..."

            r "..."

            show tsukasa srs0 zorder 0:
                easein 0.3 xalign 0.5

            pause 0.3

            hide tsukasa with Dissolve(.3)

            show rui sad at sd

            r "[player_name]... Пойдём пройдём на кухню, нам стоит поговорить."

            p "..."

            $ rui_know_tsu = True

            jump rui_posle_tsu

        "Он лез ко мне":

            $ za_rui += 2

            p "Он лез ко мне..."

            show tsukasa shock0 at sd

            ts "ЧТО?!"

            show tsukasa srs0 at sd

            show rui angry0 at sd

            r "М?"

            show tsukasa shock0 at sd

            ts "П-подожди... [player_name]... Что ты такое говоришь?!"

            menu:

                "Это шутка":

                    $ haha_add('3')

                    p "Хи-хи, да шучу я.."

                    show rui angry0

                    show tsukasa srs0 at sd

                    ts "..."

                    r "..."

                    ts "У тебя ужасное чувство юмора, [player_name]..."

                    p "Хи-хи, да ладно вам."

                    show rui hello0 at sd

                    r "Ахах..."

                "Я серьёзно":

                    p "Я серьёзно."

                    show tsukasa scream0 at sd

                    ts "{cps=0}АААААААААААААААААААААААААААААААААААААААААААААА?!?!??!?!!?!!?!{nw}{/cps}"

                    show tsukasa scream0:
                        linear 0.1 xalign 0.7
                        linear 0.03 xalign 0.6
                        pause 0.2
                        linear 0.1 xalign 0.0
                        linear 0.03 xalign 0.2
                        pause 0.2
                        linear 0.1 xalign 0.7
                        linear 0.03 xalign 0.6
                        pause 0.2
                        linear 0.1 xalign 0.0
                        linear 0.03 xalign 0.2

                    ts "{cps=0}АААААААААААААААААААААААААААААААААААААААААААААА?!?!??!?!!?!!?!{/cps}"

                    ts "Что ты имеешь в виду????????? Я всего лишь хотел поговорить с тобой..."

                    $ lie_add('2')

                    r "Да неужели?"

                    show tsukasa shock0 at sd

                    ts "Р-руи..."

                    jump tsu_pain
    
    show rui angry0 at sd zorder 1

    r "В любом случае, Цукаса, что ты здесь делаешь?"

    show tsukasa hard0 at sd

    ts "Просто пришёл поговорить с [pn_tp], мы ведь друзья."

    r "В 6 часов утра?.."

    ts "Да?.."

    show rui panic0 at sd

    r "НЕ ДЕРЖИ МЕНЯ ЗА ИДИОТА!!"

    show tsukasa shock0 at sd

    ts "Ва!"

    show tsukasa srs0 at sd zorder 0

    show rui angry0 at sd

    r "[player_name]... Лучше бы оказалось, что ты не виновата в этой ситуации и что тебе нечего от меня скрывать..."

    p "Руи, я..."

    if za_tsu > za_rui:

        show tsukasa hard0 at sd

        ts "Она ни в чём не виновата, Руи, успокойся!"

        r "Хорошо, я поверю. Но тогда вопросы к тебе. Какого чёрта, ты припёрся к {sc=1}{i}{=norm_style}моей девушке{/i}{/sc} в 6 утра?"

        show tsukasa srs0 at sd

        ts "Я..."

        r "Язык проглотил?"

    ts "..."

    menu:

        "Он сказал, что волнуется о тебе":
            
            $ za_rui += 1

            p "Он лишь сказал, что заметил странности в твоём поведении."

            show tsukasa shock0 at sd

            ts "[player_name]!"

            p "Он волнуется за тебя, за меня и за наши с тобой отношения."

            r "Вот оно что..."

            show rui panic0 at sd

            r "Цукаса... Скажи, а зачем ты суёшь нос не в своё дело..."

            show tsukasa pain0 at sd

            ts "..."

            r "Разве наши отношения с [pn_tp] выглядят нездорово? Что в них не так?"

            ts "Руи... Мне кажется ты слишком помешан на ней..."

            r "Ха?"

            show rui angry0 at sd

            r "Что ты имеешь в виду? Помешан? О, может ты видел те фотографии... Хм, это в порядке вещей знать о своём партнёре как можно больше, разве нет?"

            show tsukasa srs0 at sd

            ts "..."

            r "Уходи... Цукаса, уходи... {w=1}Не пытайся разрушить наши с [pn_tp] отношения!"

            show tsukasa srs0 zorder 0:
                easein 0.3 xalign 0.5

            pause 0.3

            hide tsukasa with Dissolve(.3)

            $ chestno = True

            $ renpy.notify('Руи запомнит вашу честность!')

            r "Ох..."

            show rui hello at sd

            r "Спасибо за честность, [player_name]."

            r "В любом случае, пошли на кухню, я хотел бы с тобой поговорить."

            $ rui_know_tsu = True

            jump rui_posle_tsu

        "Он пригласил меня участвовать в шоу":

            p "Он пригласил меня поучаствовать в шоу."

            r "..."

            play sound udar2
            with hpunch

            show tsukasa shock0

            $ rui_pain_add('19')

            p "Ай!"

            ts "Руи!"

            r "Ты это сейчас серьёзно?!"

            r "ТЫ ДЕЙСТВИТЕЛЬНО ДУМАЕШЬ, ЧТО Я ПОВЕРЮ В ЭТУ ЧУШЬ?"

            show rui panic0 at sd

            r "Как минимум, НИКТО в 6 утра не приходит домой к другому человеку, чтобы просто позвать его поучаствовать в шоу."

            r "Да и тем более... {w}Это {sc=2}{i}{=norm_style}я{/i}{/sc} занимаюсь постановкой! Это {sc=2}{i}{=norm_style}я{/i}{/sc} распределяю роли! Если б что-то изменилось в плане, то {sc=2}{i}{=norm_style}я{/i}{/sc} бы первый об этом узнал!"

            p "..."

            show rui angry0 at sd

            r "Теперь ты понимаешь насколько глупа была твоя ложь, [player_name]?"

            p "Руи, я..."

            show rui sad0 at sd

            r "Скажи, [player_name], что мне теперь о тебе думать? Как мне теперь тебе доверять?"

            r "И ты, Цукаса..."

            show tsukasa srs0 at sd

            ts "..."

            show rui angry0 at sd

            r 'Я ухожу из "Wonderlands x Showtime". Навсегда.'

            show tsukasa shock0 at sd

            ts "Ч-что?! Руи, подожди!"

            r "Это окончательное решение. С этого момента меня ничто с тобой больше не связывает... Так же как и с Нене, Эму и кем-либо ещё."

            r "Теперь для меня в этом мире существуют только я сам и [player_name]."

            show tsukasa scream0 at sd

            ts "Руи! Ты спятил! Ты ведь..."

            show tsukasa srs0 at sd

            r "Заткнись! Она сможет вернуть моё доверие к ней, мы будем счастливы вместе, {sc=1}{i}{=norm_style}навечно!{/i}{/sc}"

            p "Руи..."

            show rui angry:
                linear 0.15 xalign 0.5 zoom 1.3 yalign -0.05

            pause 0.1

            show tsukasa shock0 at sd

            show rui ubeysa1 with Dissolve(.1):
                zoom 1.0 yalign 0.0 xalign 0.5

            r "Пойдём, [player_name]..."

            p "Р-руи..."

            r "Пойдём скорее"

            p "..."

            window hide

            stop music fadeout 1.0
            play music low fadein 1.0 volume 2.3
            scene bg street3
            show rui go to u
            with Fade(0.5, 0.3, 0.5)

            window show

            p "Руи..."

            r "Чш... С этого момента мы будем счастливы."

            p "..."

            menu:

                "Куда ты меня ведёшь?":

                    p "Куда ты меня ведёшь, Руи?.."

                    r "К себе домой. Теперь мы вечность будем счастливы вместе. Вечность..."

                "Что ты собираешься сделать со мной?":

                    p "Что ты собираешься сделать со мной?.."

                    r "Хе-хе, не переживай, я просто спасаю тебя от всех от проблем!"

                    r "У меня дома никто тебя не тронет... И мы вечность будем счастливы вместе!"

                "...":

                    p "..."

            show rui go to u:
                "rui go to u h" with Dissolve(.1)

            r "[player_name], я так счастлив, ты не представляешь!"

            r "Наконец-то у нас всё будет хорошо, наконец-то! Никто, никто нам больше не помешает."

            r "Ох, [player_name], я так тебя люблю. Я так тебя люблю, [player_name]!"

            jump go_rui_home

        "Он хотел приготовить тебе подарок":

            $ za_tsu += 1

            p "Руи, он лишь хотел приготовить тебе подарок и пришёл ко мне, чтобы попросить помощи."

            show rui shock0 at sd

            r "Что... {w=1}В 6 утра?"

            p "Ну знаешь, ты почти всегда рядом со мной. Очень сложно обсудить сюрприз."

            show tsukasa hard0 at sd

            ts "[player_name]..."

            show rui panic0 at sd

            $ lie_add('3')

            r "Что ж... Это имеет смысл."

            show rui hello0 at sd

            r "Хорошо, вы закончили свои обсуждения?"

            menu:

                "Да":

                    p "Да, мы уже закончили."

                "Нет":

                    p "Нет, ещё..."

                    show tsukasa shock0 at sd

                    ts "Закончили! Мы закончили! Мне уже пора!"

            r "Хорошо... {p}Цукаса, в следующий раз просто предупреди меня, что ты хочешь обсудить c [pn_tp] сюрприз для меня."

            show tsukasa hard0 at sd

            ts "Хорошо..."

            r "..."

            show tsukasa hard0 zorder 0:
                easein 0.3 xalign 0.5

            pause 0.3

            hide tsukasa with Dissolve(.3)

            r "Что ж, а теперь я хочу кое-что тебе рассказать, пошли на кухню."

            jump rui_posle_tsu

    return

# Руи избивает Цукасу (концовка)
label tsu_pain:

    play sound udar2

    show tsukasa scream0 at sd

    ts "Ай! Что ты творишь!"

    r "А ты?"

    play sound udar

    show tsukasa pain0 at sd

    ts "ПРЕКРАТИ МЕНЯ БИТЬ!"

    r "Иначе что?"

    show rui angry zorder 2:
        linear 0.1 xalign 0.4

    pause 0.05
    hide tsukasa
    show rui beat tsu:
        xalign 0.2
    with Dissolve(0.2)

    pause 0.15

    play sound udar
    queue sound udar2

    ts "[player_name]! Сделай что-нибудь!"

    menu:

        "[[Вмешаться]":

            jump rui_stop_beat_tsu

        "[[Не вмешиваться]":

            p "..."

            play sound udar
            queue sound udar2
            queue sound udar
            queue sound udar2

            pause 0.1

            ts "[PN]!!!"

            play sound udar2
            queue sound udar

            ts "ПОЖАЛУЙСТА, [PN], ОСТАНОВИ ЕГО!! Я ТЕБЯ УМОЛЯЮ!!!!!!"

            play sound udar
            queue sound udar2

            p "..."

            menu:

                "[[Вмешаться]":

                    jump rui_stop_beat_tsu

                "[[Не вмешиваться]":

                    p "..."

                    play sound udar2
                    queue sound udar

                    ts "[PN]! [PN]! [PN]!"

                    "Вы продолжали смотреть на то, как Руи избивает Цукасу, не вмешиваясь..."

                    show rui sad with dissolve:
                        xalign 0.4

                    if not persistent.tsu_pain_beat:
                        $ get_ach ('tsu_pain')
                        $ persistent.tsu_pain_beat = True

                    "Спустя пару минут Цукаса смог вырваться и убежал прочь."

                    r "[player_name]... {w=1}Ты в порядке?"

                    p "Да..."

                    show rui hello say at sd

                    r "Всё будет хорошо теперь, Цукаса тебя не тронет больше."

                    show rui hello at sd

                    p "Да... {w=0.5}Спасибо."

                    r "Ты пережила достаточно сильный шок... Может, ты хочешь переехать ко мне на время?"

                    menu:

                        "Да":

                            p "Да... Я думаю, это неплохая идея..."

                            show rui happy at sd

                            r "Отлично! Тогда пойдём."

                            jump go_rui_home

                        "Нет":

                            p "Не стоит... Мне лучше остаться у себя дома."

                            show rui sad at sd

                            r "М... Ничего, я понимаю."

                            show rui hello at sd

                            r "В любом случае, я рад, что с тобой сейчас всё хорошо!"

                            p "..."

                            window hide 

                            pause 0.5

                            call ends_rui("tsu_pain") from _call_ends_rui_9

                            pause 2.0

    return

# гг простит Руи перестать пиздеть Цукасу
label rui_stop_beat_tsu:

    p "Руи! Прекрати!"

    play sound udar2
    queue sound udar

    r "..."

    p "Руи! Пожалуйста!"

    show rui shock:
        xalign 0.5
    show tsukasa cry pain:
        xalign 0.15
    with Dissolve(.2)

    r "..."

    p "Цукаса..."

    ts "..."

    hide tsukasa with Dissolve(.2)

    pause 0.2

    show rui sad at sd

    r "..."

    r "[player_name]... Ты в порядке? Цукаса не сильно тебя тронул?"

    menu:

        "Я в порядке":

            p "Всё в порядке, Руи..."

            show rui hello at sd

            r "Хах... Я рад. {p=1}Прости, если я перегнул палку с этим."

            r "Окей, давай пройдём на кухню, я хотел рассказать тебе кое-что."

            p "Ага."

            $ tsu_hurt_you = True

            jump rui_posle_tsu

        "[[Притвориться, что Цукаса причинил вред]":

            p "Руи! Ты не представляешь, как он угрожал мне!"

            $ lie_add('4')

            r "[player_name]! Ты... о боже..."

            show rui angry at sd

            r "Я обязательно разберусь с ним, [player_name]..."

            p "Мне так плохо, Руи..."

            show rui sad at sd

            r "Я понимаю... Всё будет хорошо... Я защищу тебя."

            show rui hello at sd

            r "Давай, ты переедешь ко мне домой? Так будет безопасней для тебя."

            menu:

                "Да":

                    p "Да... Так будет безопасней для меня..."

                    r "Хорошо! Тогда пойдём."

                    jump go_rui_home

                "Нет":

                    p "Нет... Не стоит..."

                    r "Ох... Хорошо."

                    r "Может, мне тогда стоит что-нибудь сделать для тебя?"

                    jump rui_dog

    return

# Руи готов сделать всё ради гг (КОНЦОВКА)
label rui_dog:
    
    show rui crazy2 at sd

    $ config.menu_include_disabled = True

    r "Скажи только слово и я сделаю для тебя абсолютно всё!"

    menu:

        "Стань моей собакой":

            jump .true_rui_dog

        "Скинь ядерку на дом Цукасы" if not rnt10:

            if rui_not_tsu:

                $ rnt10 = True

                p "Скинь ядерку на дом Цукасы"

                show rui shock at sd

                r "Э? Но зачем тебе это? Это, конечно, хороший способ испытать ядерку, да и Цукаса меня в последнее время слишком бесит, но всё же..."

                if yaderka_huh:

                    show rui angry at sd

                    r "Погоди, ты так хочешь доказать, что между тобой и Цукасой ничего не было?.. Что ж.."

                    show rui panic1 at sd

                    r "Ты ведь действительно понимаешь, что я могу это сделать..."

                    p "Да..."

                else:

                    show rui sad at sd

                    r "[player_name]... Я не буду этого делать. Игра в правду или действие не должна вредить другим людям."

                    show rui hello at sd

                    r "Давай я сделаю для тебя что-нибудь другое?"

                    menu:

                        "Стань моей собачкой":

                            jump .true_rui_dog

                        "Задонать мне в секае" if not donate:

                            $ donate = True

                            $ renpy.notify('SEGA хуесосы')

                            p "Задонать мне в секае..."

                            $ get_ach('sekai')

                            show rui shock at sd

                            r "Ох... Я мог бы сделать гораздо больше для тебя, но если это твое желание..."

                            show rui hello at sd

                            if igra_deivstvie:
                                if 'donate' not in persistent.pravda_or_deistvie:
                                    $ nn_list = persistent.pravda_or_deistvie
                                    $ nn_list.append('donate')
                                    $ persistent.pravda_or_deistvie = nn_list
                                    $ get_ach('play_as')

                            r "Я задоначу тебе сегодня вечером, это всё же не так быстро."

                            show rui blush at sd

                            r "Ну а пока, моя очередь загадывать~"

                            jump rui_more.igra_dev

            elif igra_deivstvie:
                
                p "Скинь ядерку на дом Цукасы"

                show rui shock at sd

                r "Э? Странные у тебя желания.."

                show rui crazy at sd

                r "В любом случае, это отличная идея.. Я смогу испытать своё изобретение на деле!"

            else:

                p "Скинь ядерку на дом Цукасы"

                show rui shock at sd

                r "Э? Откуда ты узнала, что я недавно создал карманную ядерную бомбу?"

                show rui crazy at sd

                r "В любом случае, это отличная идея....... Заодно и испытаю её как следует..."

            show rui crazy2 at sd

            r "Ехехе........ {p=1}Пойдём же быстрее, [player_name]!"

        "Задонать мне в секае" if not donate:

            $ donate = True

            $ renpy.notify('SEGA хуесосы')

            p "Задонать мне в секае..."

            $ get_ach('sekai')

            show rui shock at sd

            r "Ох... Я мог бы сделать гораздо больше для тебя, но если ты действительно этого хочешь..."

            show rui hello at sd

            if igra_deivstvie:
                if 'donate' not in persistent.pravda_or_deistvie:
                    $ nn_list = persistent.pravda_or_deistvie
                    $ nn_list.append('donate')
                    $ persistent.pravda_or_deistvie = nn_list
                    $ get_ach('play_as')

            r "Я задоначу тебе чуть позже, когда Цукаса переведёт мне мою долю с прошлого шоу."

            if igra_deivstvie:

                r "Что ж, теперь моя очередь.."

                jump rui_more.igra_dev

            r "Может, пока ты хочешь чего-нибудь ещё?"

            menu:

                "Стань моей собакой":

                    jump .true_rui_dog

                "Скинь ядерку на дом Цукасы":

                    if igra_deivstvie:
                
                        p "Скинь ядерку на дом Цукасы"

                        show rui shock at sd

                        r "Э? Странные у тебя желания..."

                        show rui crazy at sd

                        r "В любом случае, это отличная идея.. Я смогу испытать своё изобретение на деле и деньги быстрее получу!"

                    else:

                        p "Скинь ядерку на дом Цукасы"

                        show rui shock at sd

                        r "Э? Откуда ты узнала, что я недавно создал корманую ядерную бомбу?"

                        show rui crazy at sd

                        r "В любом случае, это отличная идея... {p=1}Так я и ему отомщу, и деньги быстрее получу."

                    show rui crazy2 at sd

                    r "Ехехе........ {p=1}Пойдём же быстрее, [player_name]!"

    window hide

    stop music fadeout 1.5
    play music nn1 fadein 1.5

    scene bg street2 with fade

    show rui hello:
        xalign 0.5 alpha 0.0
        ease 0.3 alpha 1.0

    $ home = False

    window show

    show rui hello:
        alpha 1.0

    r "Поверить не могу, что мы собираемся это сделать..."

    show rui blush at sd

    r "Я так волнуюсь, [player_name]!"

    show rui sad at sd

    r "А! Кстати... Мы уже почти пришли, спрошу пока не поздно."

    r "Хочешь ли ты видеть то, как я запускаю ядерку?"

    r "Мы не будем подходить к самому дому Цукасы. В моей ядерной бомбе есть простое автоуправление. Она сама долетит до его дома."

    r "Но всё же запуск ядерки может быть достаточно пугающим. Ты точно хочешь это видеть?"

    menu:

        "Да, хочу":

            p "Да, я хочу увидеть как ты запускаешь ядерную бомбу на дом Цукасы!"

            show rui hello at sd

            r "Что ж... Тогда пойдём!"

            stop music fadeout 1.0

            scene bg street
            show rui crazy:
                xalign 0.5
            with fade
            play music nn2 fadein 1.5

            r "Так..."

            r "Для запуска всё готово... Мне начинать?"

            p "Да..."

            show rui tsu yaderka1 at sd

            r "Что ж, тогда вперёд..."

            r "3...{w=0.4}{nw}"

            r "2...{w=0.4}{nw}"

            r "1...{w=0.4}{nw}"

            play sound boom volume 0.3

            show rui tsu yaderka2 at none, Shake(None, 9.0, dist=5)
            with None

            if igra_deivstvie:
                if 'yaderka' not in persistent.pravda_or_deistvie:
                    $ nn_list = persistent.pravda_or_deistvie
                    $ nn_list.append('yaderka')
                    $ persistent.pravda_or_deistvie = nn_list
                    $ get_ach('play_as')

            r "ХАХАХАХАХХАХАХАХАХАХАХА{w=0.3}{nw}"

            p "...{w=1}{nw}"

            r "ХАХАХАХАХХАХАХААХАХАХХАХАХАХАХАХАХХАХА{w=1}{nw}"

            r "МЫ СДЕЛАЛИ ЭТО!{w=0.5}{nw}"

            r "ТЫ ВЕДЬ ТОЖЕ СЛЫШАЛА ЭТОТ ВЗРЫВ?{w=0.5}{nw}"

            p "Бож... что за конченый..."

            show rui crazy2:
                xalign 0.5

            r "{sc=1}{i}{=norm_style}[player_name]... Ох, [player_name]... [player_name]... Моя [player_name]...{/i}{/sc}"

            r "{i}[player_name]... Я так счастлив, что мы это сделали. Ты хочешь посмотреть на то как сейчас выглядит дом Цукасы?{/i}"

            $ config.menu_include_disabled = False       

            menu:

                "Да":

                    p "Да, я хочу это увидеть!"

                    r "Ехехе... Я так рад! Пошли скорее!"

                    label .tsu_bum:

                        stop music fadeout 1.0
                        scene bg tsu home bum
                        show rui happy:
                            xalign 0.5
                        with Fade(0.5, 0.3, 0.5)
                        play music dillema fadein 1.0

                        r "Ты видишь это, [player_name]... Ну разве это не прекрасно?!"

                        p "Да..."

                        show rui crazy2 at sd

                        r "{i}Интересно, был ли Цукаса у себя дома во время взрыва...{/i}"

                        show rui hello at sd

                        "Руи пялится с довольным ебалом на то, что стало с домом Цукасы."

                        r "..."

                        r "Ах.. Думаю, мы достаточно насмотрелись, нам стоит уходить, пока у нас не возникли проблемы, хе-хе..."

                        p "Ты прав."

                        show rui hello:
                            alpha 1.0
                            linear 0.3 alpha 0.0

                        p "..."

                        r "Ты идёшь?"

                        p "А? Да!"

                        scene bg corridor
                        show rui happy:
                            xalign 0.5
                        with Fade(0.5, 0.3, 0.5)

                        $ home = True

                        r "Что ж... Я надеюсь, ты довольна тем, что я {sc=1}{i}{=norm_style}сделал для тебя.{/i}{/sc}"

                        r "Чего ты хочешь ещё?"

                        $ config.menu_include_disabled = False

                        jump .ww

                "Нет...":

                    p "Нет, спасибо..."

                    show rui hello at sd

                    r "Ну ладно... В любом случае, чего сейчас хочет моя дорога?"

                    r "Чего ты хочешь ещё?"

                    label .ww:

                        menu:

                            "Ты же уже выполнил своё действие..." if igra_deivstvie and not dev_vp:

                                p "Руи, но ты же уже выполнил действие.."

                                $ dev_vp = True

                                show rui crazy2 at sd

                                r "Это уже не важно, [player_name]! Я хочу сделать для тебя ещё больше!"

                                show rui hello at sd

                                r "Ну же, чего ты хочешь ещё?"

                                jump .ww

                            "Этого достаточно":

                                jump dostatochno

                            "Стань моей собакой":

                                jump .true_rui_dog

                            "Задонать мне в секае" if not donate:

                                $ donate = True

                                $ renpy.notify('SEGA хуесосы')

                                p "Задонать мне в секае..."

                                $ get_ach('sekai')

                                show rui shock at sd

                                r "Ох... И всего-то..."

                                show rui hello at sd

                                if igra_deivstvie:
                                    if 'donate' not in persistent.pravda_or_deistvie:
                                        $ nn_list = persistent.pravda_or_deistvie
                                        $ nn_list.append('donate')
                                        $ persistent.pravda_or_deistvie = nn_list
                                        $ get_ach('play_as')

                                r "Хорошо, я задоначу тебе в секае, если ты этого хочешь, но чуть позже."

                                r "Чего ты хочешь ещё?"

                                $ config.menu_include_disabled = False

                                jump .ww

                            "Иди нахуй, конченый":

                                p "Иди нахуй, неадекват конченый..."

                                show rui sad at sd

                                r "Чего... [player_name]..."

                                p "Что слышал, чмошник."

                                stop music fadeout 0.5

                                show rui angry at sd

                                r "У тебя мозги из-за взырыва лопнулись или что?"

                                r "Ты только что послала человека, который взорвал дом своего лучшего друга!"

                                p "..."

                                r "Какая ты глупая..."

                                show rui home poh

                                r "{sc=2}{i}{=norm_style}ТЫ ИДИОТКА!{/i}{/sc}" with hpunch

                                window show

                                $ rui_pain_add('20')

                                p "Ааа! Откуда ты вообще достал этот лом???? Из своей жо-{w=0.3}{nw}"

                                play sound udar2
                                with vpunch

                                stop music

                                scene black with Dissolve(.3)

                                $ rui_psyho = True

                                jump rui_home_poh

        "Нет...":

            p "Нет, наверное, всё же не стоит..."

            show rui hello at sd

            r "Хорошо, я понимаю! Тогда жди здесь, я вернусь как только закончу."

            p "Ладно..."

            hide rui with Dissolve(.3)

            pause 0.5

            p "..."

            "Вы ждёте Руи минут 10. Кажется, вы слышали тихий взрыв."

            p "..."

            show rui crazy at center, Shake(None, 10.0, dist=5)
            with Dissolve(.3)

            if igra_deivstvie:
                if 'yaderka' not in persistent.pravda_or_deistvie:
                    $ nn_list = persistent.pravda_or_deistvie
                    $ nn_list.append('yaderka')
                    $ persistent.pravda_or_deistvie = nn_list
                    $ get_ach('play_as', tm=0.3)

            r "Я сделал это! Я скинул ядерку на дом Цукасы! {p=0.1}Меня аж всего трясёт от волнения!"

            show rui crazy2:
                xalign 0.5

            r "Ты хочешь увидеть, что сейчас стало с домом Цукасы, [player_name]???"

            menu:

                "Нет":

                    p "Нет.... не стоит..."

                    show rui shock at sd

                    r "Ох.. Прости, всё же ты и на запуск ядерки не хотела смотреть."

                    show rui hello at sd

                    r "Давай я сделаю для тебя что-нибудь ещё?"

                    r "Чего ты хочешь ещё?"

                    $ config.menu_include_disabled = False

                    jump .ww

                "Да":

                    p "Да... Звучит интересно."

                    show rui hello at sd

                    r "Ха.. Я рад, пошли скорее!"

                    jump .tsu_bum

    label .true_rui_dog:

        window auto

        p "Стань моей собачкой, Руи!"

        window show

        stop music fadeout 1.0

        show rui shock at sd

        r "Что... {w=1}Ты это сейчас серьёзно?.."

        p "Да.."

        show rui blush at sd

        r "Ну если ты так говоришь..."

        if not home:

            r "Но для начало нужно дойти до твоего дома~"

            window hide

            scene bg corridor with Fade(0.5, 0.3, 0.5)

            show rui blush with Dissolve(.3):
                xalign 0.5

            window show

            r "Что ж, теперь можем и начать..."

        play music sexmusic fadein 1.0 volume 0.4
        
        r "Что ты хочешь, чтобы я сделал для начала?"

        p "Хм... Надень ушки~ {p=0.3}У меня, вроде, где-то должны валяться."

        r "Хорошо~"

        scene black with Dissolve(.3)

        "Вы направились в свою комнату в поисках ушей. Через пару минут вы нашли их и дали Руи."

        scene bg room
        show rui dog1:
            xalign 0.5
        with Dissolve(.3)

        r "Ну как, [player_name], тебе нравится?~"

        p "Ох, ебать, достойно, но ты больше на кота похож."

        show rui dog2 at sd

        r "Ня, ня, Руи-да-ня~"

        p "Ладно, что-то в этом есть..."

        r "Ну так, с чего начнём?"

        menu:

            "Встань на колени":

                $ var1 = 1

                p "Встань на колени."

                show rui dog3 at sd

                r dog3 "Ха-ха, [player_name], мне нравится твой ход мыслей~"

                scene bg roomflo
                show rui dog8
                with Dissolve(.3)

                "Руи садится перед вами на колени."

            "Помой посуду":

                stop music fadeout 1.5

                p "Помой посуду."

                show rui dog4 at sd

                r "А? Ты это сейчас серьёзно?"

                p "Да."

                show rui dog5 at sd

                r "Хорошо, [player_name], я помою посуду."

                play music kitchen fadein 1.5

                scene bg kitchen with Fade(0.3, 0.8, 0.3)

                "Вы решили совместить приятное с полезным, грех упускать такую возможность, когда у тебя есть мальчик на побегушках."

                show rui dog2:
                    xalign -0.8
                    ease 1.5 xalign 0.5

                "Руи достаточно быстро управился с посудой."

                show rui dog2:
                    xalign 0.5

                r "Итак, что ты прикажешь делать дальше, моя госпожа?"

                p "Отлично. Итак, теперь на колени и... "

                menu:

                    "Помой полы":

                        $ var1 = 2

                        extend "помой полы."

                        show rui dog6 at sd

                        r "Да что же это такое... Ну ладно."

                        scene black with Dissolve(.3)

                        "Руи берёт тряпку и швабру из ванны и начинает мыть полы во всём вашем доме, он сразу же протирает мебель на случай, если вы потом попросите его об этом."

                        "Вы довольно наблюдаете за ним."

                        scene bg corridor
                        show rui dog6:
                            xalign 0.5
                        with Dissolve(.3)

                        r "Итак, я закончил с этим."

                        p "Отлино, теперь приготовь ужин."

                        show rui dog7 at sd

                        r "[player_name]! Зачем ты так поступаешь со мной? Я же твой ручной поросёночек..."

                        if igra_deivstvie:

                            r "Я, итак, уже достаточно сделал. Давай или ты просишь выполнить меня более интересные задания, или теперь я загадываю."
                            
                        else:

                            r "Ты же знаешь, что я рассчитывал совсем на другое, когда соглашался на это..."

                            r "Я, конечно, всегда рад тебе помочь, но заканчивай уже с этим."

                        menu:

                            "[[Ударить за непослушание]":

                                play sound udar

                                stop music

                                show rui dog4 at sd

                                p "Эй! Не забывай, кто здесь твоя госпожа!"

                                $ persistent.showkaito_rui = False

                                call kaito_list_lable("dog") from _call_kaito_list_lable_4

                                show bg corglitch

                                show kaito shglitch:
                                    alpha 0.3 xalign 0.0
                                    pause 0.08
                                    alpha 0.0 xalign 1.0
                                    pause 0.08
                                    alpha 0.3
                                    pause 0.1
                                    alpha 0.0

                                voice k_ahaha
                                ks "{glitch=10}{sc}{=norm_style}Собаки не разговаривают!{/sc}{/glitch}{w=0.2}{nw}"

                                show bg corridor

                                show rui dog7 at sd

                                r "Да что б тебя... ты что-то совсем зазналась."

                                $ rui_pain_add('21')

                                play sound udar2
                                with vpunch

                                r "Ты совсем не ценишь то, что я для тебя делаю!" 

                                p "Руи, погоди, я же..{w=0.3}{nw}"

                                play sound udar
                                with hpunch

                                $ rui_pain_add('22')

                                scene black with Dissolve(.3)

                                jump rui_home_poh

                            "Хорошо, прости":

                                $ get_ach('dog_wow')

                                p "Хорошо, прости меня, Руи..."

                                show rui dog5 at sd

                                r "Другое дело... {w=0.5}Ну, что интересного ты мне теперь загадаешь?"

                                stop music fadeout 1.0

                                p "Встань на четвереньки и иди за мной как собачка.."

                                show rui dog2 at sd

                                r "Мррр~ А это мне уже нравится."

                                play music sexmusic fadein 1.5 volume 0.4

                                scene bg roomflo
                                show rui dog8
                                with Fade(0.3, 0.6, 0.3)

                                "Руи ползёт на четвереньках за вами в вашу комнату."

                    "Иди за мной как собачка":

                        $ var1 = 1

                        extend "иди за мной как собачка~"

                        stop music fadeout 1.0

                        show rui dog3 at sd

                        r "Ха-ха, как скажешь, [player_name]~"

                        play music sexmusic fadein 1.5 volume 0.4

                        scene bg roomflo
                        show rui dog8
                        with Fade(0.3, 0.6, 0.3)

                        "Руи ползёт на четвереньках за вами в вашу комнату."

        r "Я жду твоих команд, [player_name]~"

        p "Капец у тебя плащ как второй ковёр... {w=0.3}Ладно, неважно."

        menu:

            "Поцелуй мои ноги":

                p "Поцелуй мои ноги."

                r "Как скажешь, госпожа~"

                scene rui dog10 with Dissolve(.3)

                "Руи приближает к вам ближе и целует вашу ногу."

                scene end rui rui_dog with Dissolve(.1)

            "Погавкай для меня":

                p "Погавкай для меня~"

                r "..."

                show rui dog8:
                    "rui dog9" with Dissolve(.1)

                r "Гав-гав!~"

                show rui dog9:
                    "rui dog8" with Dissolve(.1)

                p "Ха-ха, забавно..."

                scene end rui rui_dog with Dissolve(.3)

                "Руи приближается к вам ближе и берёт вашу ногу себе в руку."

        r "Чего ещё пожелаете, госпожа?~"

        show end rui rui_dog:
            "rui dog11" with Dissolve(.1)

        r "Ау.. {w=0.3}Ха-ха, это было неожиданно."

        show rui dog11:
            "rui dog12" with Dissolve(.1)

        r "Что ж, позволь мне побыть непослушным пёсиком~"

        show rui dog12:
            "rui dog13" with Dissolve(.1)

        p "Руи... "

        $ x = 0

        menu:

            "[[Наслаждаться]":

                $ var2 = 1

                show rui dog13:
                    "rui dog14" with Dissolve(.2)

                "Руи наклоняется ближе к вашей киске, отодвигает ваши трусики в сторону и высунув язык начинает водить им вверх-вниз вдоль вашего междуножного пирожного."

                p "Ах... О боже..."

                show rui dog14:
                    "bg black" with Dissolve(.3)

                "Вы закрываете глаза, полностью погружаясь в бурю эмоций."

                "Руи действительно хорош в этом, он очень умело обращается своим языком. Ваша [player_name]-мини уже полностью мокрая."

                "Прошло несколько минут чистой эйфории и вы доходите до пика, испытывая глубокий экстаз."

                scene end rui rui_dog with Dissolve(.3)

                "Вы открываете глаза и смотрите на Руи, тяжело дыша."

                r "Это было достаточно хорошо?"

                p "Да, Руи... Я была на седьмом небе."

                r "Хе-хе, я рад, что тебе понравилось~"

                p "Не зазнавайся только.."

                r "Конечно, конечно~"

            "[[Сопротивляться]":

                $ var2 = 2

                show rui dog13:
                    "rui dog15" with Dissolve(.1)
                    pause 0.1
                    "rui dog16" with Dissolve(.05)
                    pause 0.1
                    "rui dog17" with Dissolve(.05)
                    pause 0.3
                    "rui dog18" with Dissolve(.1)

                "Вы со всей дури пинаете Руи в лицо."

                r "Ай-яй, [player_name], это больно..."

                p "А нехуй делать то, чего я не приказываю, понял?"

                show rui dog18:
                    "rui dog19" with Dissolve(.15)

                r "А ты, оказывается, очень строгая, когда доминируешь~"

                p "Захлопнись и делай то, что я говорю!"

                r "У-у-у.. Ладно-ладно~"

        r "Что мне теперь сделать, госпожа?"

        p "Снимай штаны и тащи страпо-{w=0.3}{nw}"

        if igra_deivstvie:
            if 'dog' not in persistent.pravda_or_deistvie:
                $ nn_list = persistent.pravda_or_deistvie
                $ nn_list.append('dog')
                $ persistent.pravda_or_deistvie = nn_list
                $ get_ach('play_as')

        "После этого ваша фантазия стала настолько безумна, что на всеобщий обзор это лучше не показывать..."

        "Руи слушался каждой вашей команды. Кажется, он неплохо вжился в роль подчинения."

        if var2 == 1:
            if var1 == 1:
                $ rui_horny_add('5')
            else:
                $ rui_horny_add('6')
        else:
            if var1 == 1:
                $ rui_horny_add('7')
            else:
                $ rui_horny_add('8')  

        "Что бы вы не сказали ему, он это выполнит... {p}Неважно насколько извращённая это будет идея, {sc=1}{i}{=norm_style}он всё сделает ради вас...{/i}{/sc}"

        window hide

        call ends_rui("rui_dog") from _call_ends_rui_10

        pause 5.0

        return

# руи взрывает дом цукасы, гг говорит, что этого достаточно (КОНЦОВКА)
label dostatochno:

    p "Этого достаточно..."

    show rui shock at sd

    r "Ха?.. Ты так думаешь..."

    show rui hello at sd

    r "В любом случае, я рад, что смог угодить тебе. Ты всегда можешь просить меня о чём-либо. Насколько бы безумной просьба не была... Я сделаю это!"

    p "..."

    show rui blush at sd

    r "И теперь никто и никогда не сможет помешать нашей любви! В ином случае его будет ждать та же учесть, что и Цукасу!"

    stop music fadeout 1.0

    scene bg tsu home bum with Fade(0.5, 0.3, 0.5)

    "Позже выяснялось, что во время взрыва в доме Цукасы была вся его семья..."

    "Каким-то чудом полиция так и не смогла раскрыть это дело. Похоже, Руи просто гений."

    "После этого ваши отношения с Руи стали только сильнее. {p=2}И вы не до конца уверены в том, из-за любви ли это, или из-за страха..."

    window hide

    call ends_rui("tsu_bum") from _call_ends_rui_11

    pause 5.0

    return


# гг пускает Цукасу домой
label tsu_welcom:

    stop music fadeout 1.0

    window hide

    scene bg kitchen talk
    show kitchen talk zorder 10
    show tsukasa srs:
        xalign 0.4
    with Fade(0.5, 0.5, 0.5)

    play music kitchen fadein 1.0 volume 0.8

    window show

    if tsu_lit_know:

        p "Так... Что там с Руи?.."

        show tsukasa hard say at sd

        ts "Как я уже и сказал, он стал слишком ревнивым и помешенным на тебе..."

        ts "Я помню, как мы с тобой и Эму как-то задержались до поздна, через пару дней на твоих руках были синяки..."

        show tsukasa hard at sd

        ts "Он ведь тебя бьёт, когда ты делаешь то, что ему не нравится, так?.."

        p "Я..."

        show tsukasa pain at sd

        ts "..."

        ts "Насчёт тех фотографий... На них ты находишься на улице, в школе, в своей квартире... Но все они сделаны скрытно: из-под угла, через окно..."

        ts "Чёрт, у него даже есть фотографии, на которых ты переодеваешься!"

        p "Ох.."
    
    else:

        p "Так... Что ты хотел мне рассказать про Руи?"

        ts "[player_name].. Руи ведь иногда бьёт тебя?"

        p "..."

        show tsukasa hard say at sd

        ts "Я понимаю, что возможно лезу не в своё дело, но я волнуюсь за вас двоих."

        ts "Руи слишком помешан на тебе. Он ревнует тебя к каждому кусту. Я помню, как мы с тобой и Эму как-то задержались до поздна, через пару дней на твоих руках были синяки..."

        ts "На днях, во время репетиции шоу, я заметил в портфеле Руи твои фотографии. Когда он отошёл, я взглянул на них поближе..."

        show tsukasa pain at sd

        ts "..."

        ts "[player_name]... Все те фотографии сделаны исподтишка. На них ты находишься на улице, в школе, в своей квартире... {w}Чёрт, у него даже есть фотографии, на которых ты переодеваешься!"

        p "Ох..."

    show tsukasa srs at sd
    
    ts "Сам он стал более отстранённым..."

    menu:

        "[[Слушать дальше]":

            ts "Раньше он тоже чудным был, но он всегда очень любил своих друзей и свои шоу... Он был очень добрым человеком."

            show tsukasa hard say at sd

            ts "Всё начало меняться, когда ему исполнилось 18 и он съехал от родителей..."

            ts "Он полностью отдался своим изобретениям, почти не выходил из дому, он даже умудрялся пропускать шоу!"

            show tsukasa pain at sd

            ts "Мы очень сильно волновались за него... Но потом он познакомился с тобой."

            show tsukasa hard at sd

            ts "Его состояние улучшилось, он снова стал таким, каким был ранее. С тобой он был особенно мил."

            ts "Потом вы начали встречаться и всё казалось было хорошо..."

            show tsukasa pain at sd

            ts "Но сейчас ему снова становится хуже... Он буквально стал помешан на тебе..."

            show tsukasa srs at sd

            ts "[player_name].. Он любит тебя нездоровой любовью... Ты ведь это понимаешь?"

            p "Цукаса.. я.."
            
            menu:

                "Я понимаю это":

                    $ za_tsu += 1

                    p "Да... Я понимаю это ты прав. Мне было страшно поднимать эту тему..."

                    show tsukasa hard at sd

                    ts "Рад, что ты осознаёшь проблему..."

                    ts "Я считаю, ему стоит обратиться к психотерапевту. Пару терапий должны пойти ему на пользу."

                    p "Да... Думаю, ты прав."

                    ts "[player_name], будь осторожней с ним и попытайся как-нибудь подтолкнуть его на поход к врачу."

                    p "Да, хорошо."

                "Ты преувеличиваешь":

                    $ za_rui += 2

                    p "Я думаю, что ты преувеличиваешь."

                    show tsukasa pain at sd

                    ts "[player_name]..."

                    p "Да, Руи странноват, но именно это и делает его таким привлекательным!"

                    ts "..."

                    ts "Наверное, нет смысла тебя переубеждать..."

                    ts "[player_name], просто... Просто будь осторожней с ним. И попытайся как-нибудь подтолкнуть его к тому, чтобы он посетил психотерапевта."

                    p "Ладно, наверное..."

            ts "Ладно, мне лучше уйти, пока Руи не пришёл."

            p "Ты прав."

            window hide

            scene bg corridor
            show tsukasa hard
            with Fade(0.3, 0.5, 0.3)

            window show

            ts "Будь осторожней, [player_name]... Я.."

            $ tsu_say_gg = True

            jump rui_back

        "[[Уломать на секс]":

            jump domog_tsu

    return

# гг домагается до Цукасы (КОНЦОВКА)
label domog_tsu:

    p "Цукаса, я..."

    show tsukasa shock at sd

    ts "[player_name]... С тобой всё хорошо?.."

    menu:

        "[[Надавить на жалость]":

            p "Цукаса... Знаешь, Руи может быть так жесток ко мне..."

            label .zhalost:

                show tsukasa srs at sd

                ts "[player_name]... Ты можешь высказать мне всё насчёт Руи, я найду способ помочь тебе..."

                p "Всё, что ты сказал правда... Он одержим мной. Он сталкерит за мной. Он бьёт меня. Он не спрашивает моё мнение. Он не даёт мне выбора. Он угрожает мне."

                p "Руи абьюзер."

                show tsukasa pain at sd

                ts "[player_name]..."

                show tsukasa pain:
                    ease 0.8 xalign -0.8
                pause 0.7
                show tsukasa pain zorder 11:
                    zoom 1.4 xalign -1.5 yalign 0.4
                    ease 0.7 xalign 0.5

                pause 0.6

                show tsukasa pain:
                    zoom 1.4 xalign 0.5 yalign 0.4

                ts "Мне очень жаль, что тебе приходиться переживать это. Спасибо, что рассказала мне об этом. Я найду способ тебе помочь."

                scene black with Dissolve(.3)

                "Цукаса крепко, но осторожно обнимает вас. Вы обнимаете его в ответ."

                "Но вы помните, ради чего вы ему столько наврали... Ваши руки лезут под футболку Цукасы."

                ts "[player_name]! Что ты делаешь?!"

                p "Твоё тело очень тёплое~"

                stop music fadeout 1.5

                play sound undress

                "Какими-то дохуя умными движением рук вы снимаете с Цукасы кофту и футблоку."

                scene bg kitchen talk
                show kitchen talk zorder 2
                show tsukasa s1 zorder 3:
                    xalign 0.5 zoom 1.2 yalign 0.4
                with Dissolve(.3)

                play music sexmusic fadein 1.5 volume 0.3

                ts "Вааааа! Как это вообще произошло?!?!?! Как ты умудрилась снять с меня футболку с кофтой???"

                show tsukasa s2 at sd(ypos=0.4)

                ts "Зачем ты это сделала, [player_name]..."

                p "Цукаса, прости... я просто... Мне так не хватает любви... Руи не даёт мне тепла."

                ts "Но ты ведь понимаешь, что секс тебе не даст тепла?"

                p "Цукаса..."

                menu:

                    "[[Заплакать]":

                        p "Цукаса... Я.. ладно прости... *хнык*"

                        show tsukasa s1 at sd(ypos=0.4)

                        ts "[player_name]... Ты плачешь?"

                        p "Прости меня за это, Цукаса! Я слишком привыкла к общению с Руи... он любит когда я вытворяю нечто такое... и может ударить, если я так не делаю..."

                        ts "[player_name]..."

                        p "Я всегда надеюсь, что смогу получить от него тепла в постели, но... он всегда... *хнык-хнык*"

                        ts "..."

                        show tsukasa s2 at sd(ypos=0.4)

                        ts "Если я соглашусь переспать с тобой, то тебе станет лучше?"

                        p "..."

                        p "Наверное..."

                        ts "Хоть мне и не нравится эта идея, но если так тебе действительно станет лучше..."

                        p "Да.. Пойдём в мою комнату..."

                    "[[Умолять]":

                        p "Цукаса... Пожалуйста... Я просто умоляю тебя!"

                        show tsukasa s1 at sd(ypos=0.4)

                        ts "[player_name]... Тебе действительно так нужно это?"

                        p "Да..."

                        show tsukasa s2 at sd(ypos=0.4)

                        ts "Ладно... Хорошо... Если это действительно поможет, то я согласен."

                        p "Правда?"

                        ts "Да.. {w=0.5}Пошли в твою комнату."

                    "[[Перейти на флирт]":

                        p "Но Цукасик~ Ты ведь тоже этого хочешь разве нет?"

                        ts "[player_name]..."

                        p "Разве ты не ради этого напросился ко мне домой? Да по твоим глазам видно, как сильно ты меня хочешь~"

                        show tsukasa s1 at sd(ypos=0.4)

                        ts "Что ты такое говоришь! Отойди от меня! Я не собирался лезть к тебе, я действительно хотел тебе помочь!"

                        show tsukasa s2 at sd(ypos=0.4)

                        ts "Но как я вижу, ты сама такая же..."

                        show tsukasa s2:
                            easein 0.8 xalign -1.5

                        if 'flirt_go' not in persistent.tsu_say_no_list:
                            $ nn_list = persistent.tsu_say_no_list
                            $ nn_list.append('flirt_go')
                            $ persistent.tsu_say_no_list = nn_list
                            $ get_ach('tsu_no')

                        "Цукаса берёт свою одежду и убегает от вас"

                        hide tsukasa

                        jump .tsu_go

        "[[Флиртовать]":

            # неудачно, цукаса убегает, т/и понимает, что руи лучший (+концовка)

            p "Слушай, Цукасик~"

            show tsukasa blush at sd

            ts "Как ты меня назвала?.."

            label .vlirt:

                p "Цукасик~"

                show tsukasa shock at sd

                ts "..."

                p "А твои родители случайно не межзвездный газ и пыль?"

                ts "Нет?.."

                p "Тогда откуда у них такая звезда?"

                ts "..."

                p "Э... {w}Слушай, Цукаса, ты очень большая звезда, ведь ты так горяч!"

                ts "..."

                p "..."

                p "Руи обычно нравится такое..."

                show tsukasa pain at sd

                ts "Я не удивлён.."

                p "Цукасик~ Тогда как насчёт того, чтобы помочь маленькой хрупкой девушке, вроде меня, с уборкой?"

                show tsukasa srs at sd

                ts "..."

                show tsukasa hard at sd

                ts "Ладно, вы с Руи идеальная пара."

                p "Что?"

                if tsu_fuck:
                    if 'flirt_fuck' not in persistent.tsu_say_no_list:
                        $ nn_list = persistent.tsu_say_no_list
                        $ nn_list.append('flirt_fuck')
                        $ persistent.tsu_say_no_list = nn_list
                        $ get_ach('tsu_no')
                else:
                    if 'flirt_one' not in persistent.tsu_say_no_list:
                        $ nn_list = persistent.tsu_say_no_list
                        $ nn_list.append('flirt_one')
                        $ persistent.tsu_say_no_list = nn_list
                        $ get_ach('tsu_no')

                ts "Я ухожу, вам двоим явно не нужна моя помощь, зря только время потратил."

                show tsukasa hard:
                    easein 0.8 xalign -0.8

                label .tsu_go:

                    p "Цукаса, постой!"

                    scene bg corridor with Fade(0.5, 0.3, 0.5)

                    p "Цукаса!"

                    p "..."

                    "Цукаса ушёл, вы так и не смогли переспать с ним, эхх."

                    "Спустя несколько минут пришёл Руи..."

                    scene black with Dissolve(.3)

                    "Он согласился переспать с вами после первого же намёка."

                    scene end rui the_best with Dissolve(.3)

                    "Теперь вы полностью уверены в том, что Руи - ваш идеальный партнёр."

                    "Только Руи способен удовлетворить вас{w=0.5}, только Руи сможет развеселить вас{w=0.5}, только Руи сможет поддержать вас..."

                    "Руи лучший. Только Руи."

                    window hide

                    call ends_rui("the_best") from _call_ends_rui_12

                    pause 5.0

                    return

        "Трахни меня":

            $ tsu_fuck = True

            p "Цукаса... {w=1}Трахни меня."

            show tsukasa scream at sd

            ts "ВАААААААААААААА!!!!!"

            show tsukasa blush at sd

            ts "Ч-что ты такое говоришь!"

            ts "[player_name]! Т-ты..."

            menu:

                "[[Флиртовать]":

                    p "Хе-хе, да ладно тебе, Цукасик~"

                    show tsukasa pain at sd

                    ts "Не называй меня так..."

                    jump .vlirt

                "[[Надавить на жалость]":

                    p "Прости, я просто... общение с Руи ломает мою психику"

                    jump .zhalost

    window hide

    scene bg room
    show tsukasa s3:
        xalign 0.5
    with Fade(0.5, 1.0, 0.5)

    pause 1.0

    window show

    ts "..."

    ts "У меня действительно давно не было опыта в этом..."

    p "О, так ты не девственник?"

    show tsukasa s4 at sd

    ts "Конечно нет! {w=1}С чего ты вообще взяла, что звезда, вроде меня, всё ещё может быть девственником к 19 годам..."

    ts "..."

    show tsukasa s3 at sd

    ts "Мне начинать?"

    p "Да..."

    ts "Хорошо..."

    show tsukasa s3:
        ease 0.7 zoom 1.4 yalign 0.4

    pause 0.7

    ts "Я..."

    show tsukasa s6 zorder 1:
        zoom 1.2 yalign 0.5

    noc "[player_name]!"

    show rui shock zorder 0 with dissolve:
        xalign 1.1 zoom 0.9 yalign 1.0

    show rui panic1 at sd

    r "[player_name], как это понимать?!"

    show tsukasa s6:
        easein 0.5 zoom 1.0 yalign 1.0 xalign 0.2

    show rui panic0:
        easeout 0.5 zoom 1.0 yalign 1.0 xalign 0.9

    p "Вот это пиздец..."

    show tsukasa s70 at sd

    ts "Р-руи..."

    show rui angry0 at sd

    r 'Ну давайте, попробуйте высрать из себя какое-нибудь тупое оправдание в стиле "это не то, что ты подумал".'

    p "Руи, я..."

    play sound udar
    with vpunch

    $ rui_pain_add('23')

    r "Молчать! Ты не имеешь права говорить сейчас!"

    ts "..."

    r "Что, Цукаса, теперь тебе страшно, да?"

    show rui panic0

    r "А нужно было думать, прежде чем делать..."

    show rui angry0 at sd

    r "Как вы вообще к этому пришли..."

    r "Аргх... я так зол... я так зол..."

    show rui panic0

    r "Нет, я не могу так просто это всё оставить!"

    play sound udar2

    ts "Ай! Руи!"

    play sound udar

    stop music fadeout 1.5

    show tsukasa s6 at sd

    ts "Перестань меня бить!"

    play sound udar2
    queue sound udar

    ts "Руи!!"

    scene end rui izmena with Fade(0.5, 0.3, 0.5)

    "Руи начал избивать Цукасу. Вы смотрели на это не вмешиваясь."

    "Вы точно знали, если вы помешаете ему сейчас, то он вас просто изобьёт до смерти..."

    if not persistent.tsu_pain_izmena:
        $ get_ach ('tsu_pain')
        $ persistent.tsu_pain_izmena = True

    "Цукаса сильно пострадал, но по какой-то причине не стал никуда докладывать на Руи, после случившегося."

    "Руи был зол на вас, но большую часть гнева выпустил именно на Цукасу."

    $ rui_pain_add('24')

    "Теперь Камиширо полностью контролирует вас, он не отоходит от вас ни на шаг... Даже в туалете."

    window hide

    call ends_rui("izmena") from _call_ends_rui_13

    pause 5.0

    return

# Руи после того, как Цукаса ушёл (-)
label rui_posle_tsu:

    window hide

    stop music fadeout 1.0
    scene bg kitchen 
    show rui hello:
        xalign 0.4
    with Fade(0.5, 0.3, 0.5)

    play music kitchen fadein 1.0 volume 0.8

    window show

    r "Присядь пока. Я заварю нам чаю."

    p "Ага..."

    window hide

    show rui hello:
        ease 0.7 xalign -0.4

    pause 0.7
    scene bg kitchen talk
    show kitchen talk zorder 10
    with dissolve

    if tsu_hurt_you:

        pause 0.5

        window show

        r "Перед тем как я поделюсь с тобой радостной новостью, скажи, ты точно в порядке?"

        show rui sad:
            xalign -0.4
            ease 1.3 xalign 0.4

        r "Что Цукаса с тобой сделал?"

        show rui sad:
            xalign 0.4

        menu:

            "Он говорил о тебе плохие вещи":

                p "Он говорил плохие вещи о тебе..."

                jump .chto_tsu_say

            "Он вёл себя как типичный Цукаса":

                p "Ну... Он вёл себя как типичный Цукаса: орал, нёс какую-то чушь. Я так и не поняла, что ему нужно было от меня..."

                r "То есть он не причинил тебе боли?"

                p "Да."

                show rui hello at sd

                r "Вух... Ну и напугала ж ты меня заявлением, что Цукаса приставал к тебя, ахах..."

                p "Я просто хотела, чтобы он побыстрее ушёл, прости..."

                r "Я понимаю, самое главное, что с тобой всё хорошо."

                r "Что ж, раз это мы уладили, то я могу рассказать, зачем я пришёл к тебе сегодня!"

            "Он домогался до меня":

                p "Руи! Он домогался до меня!"

                show rui shock at sd

                r "[player_name]... Что именно он сделал? Ты можешь рассказать мне всё, я выслушаю и поддержу."

                p "Он.. он..."

                menu:

                    "Я не могу рассказать...":

                        p "Я не могу рассказать... Это тяжело"

                        show rui sad

                        $ lie_add('5')

                        r "Я понимаю, не заставляй себя..."

                        p "..."

                        r "[player_name]... Я могу что-нибудь сделать для тебя? Всё, что угодно."

                        jump rui_dog

                    "Он ляпал меня":

                        p "Он обляпал меня!"

                        r "Он сделал что?!"

                        show rui angry at sd

                        $ lie_add('6')

                        r "Ну нет... Ему это так просто с рук не сойдёт. [player_name], я обещаю, что он поплатиться за это."

                        p "..."

                        show rui sad at sd

                        r "Ох, [player_name], прости, тебе и так плохо... {w=1}Хочешь я что-нибудь сделаю для тебя?"

                        jump rui_dog

                    "Он пытался меня поцеловать":

                        p "Он пытался меня поцеловать..."

                        show rui panic1 at sd

                        r "Что..."

                        show rui angry at sd

                        $ lie_add('7')

                        r "О нет... нет, нет, нет, я не позволю ему так поступать с {sc=3}{i}{=norm_style}моей{/i}{/sc} девушкой!"

                        show rui angry:
                            easein 0.4 xalign 0.05

                        p "Руи, стой!"

                        show rui angry:
                            xalign 0.05

                        show rui shock at sd

                        r "А?"

                        p "Мне очень плохо после произошедшего..."

                        show rui sad at sd

                        pause 0.3

                        show rui sad:
                            ease 0.4 xalign 0.5

                        r "[player_name]... {w=1}Что мне сделать для тебя?"

                        show rui sad:
                            xalign 0.5

                        jump rui_dog

    elif rui_know_tsu:
        
        pause 0.5

        window show

        r "Вообще я хотел поделиться с тобой своим новым изобретением..."

        show rui sad:
            xalign -0.4
            ease 1.3 xalign 0.4

        extend " Но скажи, что говорил тебе Цукаса?"

        show rui sad:
            xalign 0.4

        label .chto_tsu_say:

            show rui angry at sd

            $ config.menu_include_disabled = True

            r "Что именно он говорил обо мне?"

            menu:

                "[[Рассказать про фотографии]":

                    $ za_rui += 1

                    p "Руи, он говорил, что видел у тебя в портфеле мои фотографии, сделанные исподтишка... Это правда?"

                    show rui sad at sd

                    r "..."

                    r "Да.. У меня есть пару фотографий с тобой, о которых ты не знаешь."

                    p "..."

                    show rui happy at sd

                    r "Ха-ха, не переживай ты так, я просто собирал информацию о тебе для кое-какого подарка~"

                    p "Оооо!"

                    show rui hello at sd

                    r "[player_name]... Это всё, что Цукаса тебе рассказывал?"

                    menu:

                        "Да, это всё":

                            p "Да, это всё."

                            r "Отлично! Что ж, раз это мы уяснили, теперь и я могу поделиться с тобой новостью!"

                        "Он волнуется за твою менталку":

                            jump .mentalka

                        "Он считает тебя сталкером" if za_rui > za_tsu:

                            jump .stalker

                "Он волнуется за твою менталку":

                    label .mentalka:

                        p "Он сказал, что волнуется за твоё ментальное здоровье..."

                        show rui shock at sd

                        r "Что..."

                        p "Цукаса рассказывал, что ты очень сильно изменился."

                        r "..."

                        p "Он считает, что тебе нужно обратиться к специалисту."

                        show rui sad at sd

                        r "И ты согласна с ним?"

                        menu:

                            "Да":

                                p "Да... Я думаю, он в чём-то прав."

                                r "[player_name]..."

                                p "Руи, послушай.."

                                menu:

                                    "Тебе нужна помощь":

                                        jump rui_go_psiholoc

                                    "Ты неадекват конченый":

                                        show rui shock at sd

                                        p "Ты... Ты действительно неадекват конченый. Вообще не понимаю почему я с тобой втсречаюсь."

                                        r "..."

                                        show rui panic1 at sd

                                        window show

                                        p "Что смотри-{w=0.3}{nw}"

                                        play sound udar
                                        with hpunch

                                        $ rui_pain_add('25')

                                        stop music

                                        scene black with Dissolve(.3)

                                        $ rui_psyho = True

                                        jump rui_home_poh

                            "Не знаю":

                                p "Я не знаю... Я не уверена."

                                r "[player_name]... Я всегда был слегка чудным, но не более. Поверь мне..."

                                p "Да... я понимаю."

                                show rui happy at sd

                                r "Если с моей психикой действительно будет что-то не так, то я обязательно сообщу тебе об этом."

                                p "Угу."

                                show rui hello at sd

                                r "Хорошо, я рад, что мы это уяснили. А теперь позволь я поделюсь своей новостью."

                            "Нет":

                                p "Нет, конечно ж."

                                show rui happy at sd

                                r "Я рад, что ты так думаешь!"

                                show rui hello at sd

                                extend " Спасибо, что доверяешь мне, [player_name]"

                                r "А теперь позволь мне кое-что тебе рассказать..."

                "Он считает тебя сталкером" if za_rui > za_tsu:

                    label .stalker:

                        $ za_rui += 1

                        p "Он считает тебя сталкером, Руи."

                        show rui shock at sd

                        r "Что? Он думает, что я сталкерю за тобой?.."

                        p "Да..."

                        show rui sad at sd

                        r "И ты ему веришь?"

                        p "Я..."

                        r "В любом случае, в этом нет смысла... Какой смысл сталкерить за человеком, с которым ты итак уже встречаешься?"

                        show rui hello at sd

                        r "Ты ведь... Согласна со мной?"

                        menu:

                            "Да, ты прав":

                                if za_rui == 8:
                                    $ get_ach('za_rui')

                                p "Да, Руи, я думаю, ты прав. В этом нет смысла"

                                r "Рад, что ты так считаешь. Что ж, раз это мы прояснили, то позволь и мне поделиться с тобой новость."

                            "Я сомневаюсь":

                                p "Я немного сомневаюсь в этом..."

                                show rui shock at sd

                                r "[player_name]..."

                                show rui sad at sd

                                extend " Что именно тебя волнует? Ты думаешь, что я действительно способен на такое?"

                                r "Возможно, я иногда бываю навязчив и пытаюсь узнать о тебе как можно больше."

                                show rui hello at sd

                                r "Но это ж не делает меня сталкером, верно?"

                                menu:

                                    "Как раз таки делает":

                                        p "Как раз таки это и делает тебя сталкером, Руи!"

                                        show rui panic1 at sd

                                        r "Что?.."

                                        p "Руи, я не могу больше это игнорировать..."

                                        jump rui_go_psiholoc

                                    "Ты прав":

                                        p "Да... Думаю, ты прав."

                                        r "Спасибо за понимание, [player_name]."

                                        r "Раз мы это уяснили, то позволь рассказать тебе кое-что~"

                            "Нет":

                                p "Нет, Руи... Человек вполне может сталкерит даже за тем, с кем уже состоит в отношениях.."

                                show rui shock at sd

                                r "И ты думаешь, что я действительно сталкеру за тобой?"

                                menu:

                                    "Да":

                                        p "Да, я действительно так считаю, Руи. И мне это не нравится!"

                                        show rui angry at sd

                                        r "[player_name], как ты можешь так думать обо мне?!"

                                        p "..."

                                        show rui hello at sd

                                        r "Окей, сделаем так, что если я действительно слежу за тобой?"

                                        menu:

                                            "Я тебя брошу":

                                                p "Тогда я тебя брошу. Я не хочу встречаться с психом..."

                                                show rui panic1 at sd

                                                r "Вот оно что... Что ж..."

                                                show rui panic1:
                                                    ease 0.7 xalign -0.6
                                                pause 0.7
                                                show rui panic1 zorder 11:
                                                    zoom 1.4 xalign -1.0 yalign 0.4
                                                    ease 0.7 xalign 0.5

                                                pause 0.6
                                                show rui ubeysa1 with Dissolve(.1):
                                                    yalign 0.5 zoom 1.2 xalign 0.5
                                                p "!!!"

                                                stop music fadeout 1.5
                                                r "Раз считаешь меня психом, то зачем говоришь такие вещи?"

                                                window show

                                                $ rui_pain_add('26')

                                                p "Руи..."

                                                play sound udar
                                                with vpunch

                                                scene black with Dissolve(.3)

                                                $ rui_psyho = True

                                                jump rui_home_poh

                                            "Я попытаюсь помочь тебе":

                                                p "Тогда я попытаюсь помочь тебе... Я действительно люблю тебя, но иногда ты меня пугаешь."

                                                show rui angry at sd

                                                r "..."

                                                p "Руи..."

                                                jump rui_go_psiholoc

                                            "Я смирюсь":

                                                p "Хм... Хороший вопрос... {w=0.5}Наверное, я просто смирюсь с этим."

                                                r "Ахах, боже, [player_name], и зачем нужно было так меня пугать..."

                                                r "Окей сменим тему разговора..."

                                    "Нет":

                                        p "Ты навряд ли... Я говорю, что просто такое вполне возможно..."

                                        show rui hello at sd

                                        r "А.. Хм, ну как скажешь."

                                        r "В любом случае, я пришёл к тебе, чтобы рассказать кое-что..."

                "Ничего такого":

                    p "Ничего такого..."

                    show rui shock at sd

                    r "А? Что ты имеешь в виду..."

                    show rui panic1 at sd

                    r "[player_name]... Я очень хочу тебе поверить, но я действительно переживаю, что Цукаса мог многое выдумать и рассказать это тебе.."

                    p "..."

                    show rui sad at sd

                    r "Скажи, ты ведь веришь в то, что, чтобы я ни делал, это всё ради тебя?"

                    menu:

                        "Да":

                            p "Да, Руи, я верю тебе."

                            show rui hello at sd

                            r "Спасибо, [player_name]... Это важно для меня."

                        "Нет":

                            p "Не особо, если честно..."

                            show rui shock at sd

                            r "[player_name]... Ты это сейчас серьёзно?"

                            p "Да..."

                            show rui sad at sd

                            r "Чего же Цукаса тебе наговорил..."

                            show rui panic1 at sd

                            r  "..."

                            show rui panic1:
                                ease 0.7 xalign -0.6
                            pause 0.7
                            show rui panic1 zorder 11:
                                zoom 1.4 xalign -1.0 yalign 0.4
                                ease 0.7 xalign 0.5

                            pause 0.4
                            p "!!!"

                            stop music fadeout 1.5

                            r "Прости меня, [player_name]..."

                            show rui ubeysa1 with Dissolve(.1):
                                yalign 0.5 zoom 1.2 xalign 0.5

                            r "Но я не могу так это оставить!" with hpunch

                            show rui ubeysa1:
                                "rui home poh" with Dissolve(.1)

                            window show

                            $ rui_pain_add('27')
                            
                            p "Руи, стой!{w=0.3}{nw}"

                            play sound udar
                            with vpunch

                            scene black with Dissolve(.3)

                            $ rui_psyho = True

                            jump rui_home_poh
                         
    else:

        r "Так-с, я поставил кипятиться воду."

        show rui hello:
            xalign -0.4
            ease 1.3 xalign 0.4

        p "Ты выглядишь таким счастливым, смог изобрести что-то новое?"

        show rui hello:
            xalign 0.4

        r "О да..."

    show rui happy at sd

    r "Ты не представляешь, что я смог создать!"

    p "Уже страшно..."

    show rui crazy2 at sd

    r "Я смог изобрести свою собственную ядерную бомбу! Карманную!"

    p '"Карманную?"'

    show rui crazy at sd

    r "Да! По размерам она меньше моего члена и с лёгкостью поместиться в корман!"

    menu:

        "Капец ядерка маленькая...":

            p "Зная как выглядит твой член, это ж насколько она мала..."

            show rui panic1 at sd

            r "[player_name]... Не говори так... Не говори так.."

        "Руи, это замечательно!":

            p "Руи, это просто замечательно! Я впервые слушу о чём-то подобном"

            show rui happy at sd

            r "Ох, [player_name]... Спасибо за твои слова.."

        "А нахуя?":

            p "Ну и нахуя?"

            show rui sad at sd

            r "[player_name]... Ты..."

    show rui crazy2 at sd
    
    r "Послушай, на что способна ещё эта малышка!"

    r "У неё есть встроенный автопилот! Вовсе не обязательно находиться рядом с целью для поражения."

    show rui hello at sd

    r "Оооо, это ещё не всё!..."
    
    menu:

        "[[Слушать]":

            "Вы внимательно слушаете рассказ Руи о его крутой ультранавороченной ядерной бомбы. Вы нихуя не понимаете, что за дичь он несёт, но периодически киваете и ахаете."

            p "Руи! Это просто невероятно! Ты действительно гениальный изобретатель!"

            show rui happy at sd

            r "Хе-хе, спасибо, [player_name]!"

            r "Что ж, раз я закончил, чем бы ты хотела заняться сейчас?"

            jump rui_more

        "[[Засесть в телефон]":

            "Вы нахуй забиваете на то, что говорит Руи и достаёте свой телефон."

            $ timerr = 40
            $ marker = "rui_posle_tsu.time_aut"
            $ from_loc = 'rui_kitchen'

            jump telephon

            label .gen_win:

                show rui angry at sd

                r "[player_name]! Ты меня слушаешь?! Почему ты улыбаешься, смотря в телефон?"

                p "Ой, я просто..."

                r "Что просто?"

                p "Я отгадала все числа в генераторе рандомных чисел..."

                r "[player_name]... {w}Я бросаю тебя..."

                p "Что..."

                show rui sad at sd

                r "Ты меня совсем не слушаешь, а вместо этого сидишь в генераторе рандомных чисел."

                r "Мне не нужны такие отношения, прощай."

                show rui sad:
                    easein 0.5 xalign -0.4

                p "..."

                jump rangen

            label .time_aut:

                hide screen timerr
                hide screen inputrangen
                hide screen rangen

                $ renpy.notify('Вы слишком долго сидели в телефоне!')

                show rui angry at sd

                r "[player_name]! Хватит в наглую сидеть в телефоне!"

            label .ti_chto:

                r "Могла бы хотя бы сделать вид, что тебе интересно..."

                p "Я..."

                show rui sad at sd

                r "Ничего не говори..."

                "Кажется, он расстроился. Возможно вам стоит подбодрить его."

                menu:

                    "[[Предложить минет]":

                        p "Руи, прости меня... Хочешь я тебе отсосу в качестве извинений?~"

                        show rui blush at sd

                        r "А мне нравится твой настрой, [player_name]~"

                        jump rui_minet

                    "Извини":

                        p "Руи, прости меня..."

                        r "[player_name], я понимаю, что возможно не интересна вся это тема, но ты же видишь как это важно для меня..."

                        r "Когда ты полчаса воодушевлённо рассказывала какие SEGA хуессосы, не могут сделать нормальную оптимизацию в ритм игре и добавляют ужасные каверы, то я тебя ж внимательно слушал..."

                        p "А тебе было неинтересно это слушать?..."

                        show rui angry at sd

                        r "[player_name], я это к тому, что ты меня совсем не ценишь!"

                        "Кажется, он всё ещё зол на вас..."

                        menu:

                            "[[Предложить минет]":

                                p "Руи, прости меня, мне действительно очень жаль... Хочешь я отсосу тебе в качестве извинений?~"

                                show rui shock at sd

                                r "Хм..."

                                show rui blush at sd

                                r "Звучит как хороший способ проявление внимания, хе-хе~"

                                jump rui_minet

                            "Иди нахуй, заебал":

                                p "Ой, иди нахуй тогда, заебал ныть."

                                show rui panic1 at sd

                                r "Ясно..."

                                show rui panic1:
                                    ease 0.7 xalign -0.6
                                pause 0.7
                                show rui panic1 zorder 11:
                                    zoom 1.4 xalign -1.0 yalign 0.4
                                    ease 0.7 xalign 0.5

                                pause 0.6
                                show rui ubeysa1 with Dissolve(.1):
                                    yalign 0.5 zoom 1.2 xalign 0.5

                                window show

                                $ rui_pain_add('28')
                                
                                r "Я научу тебя уважать меня!"

                                play sound udar
                                with hpunch

                                stop music

                                scene black with Dissolve(.3)

                                jump rui_home_poh

                    "Поплачь":

                        p "Ну, ээ... Поплачь, раз тебе грустно."

                        play sound udar
                        with vpunch

                        stop music

                        show rui angry at sd

                        $ rui_pain_add('29')

                        p "Ай!"

                        play sound udar2
                        with hpunch

                        $ rui_pain_add('30')

                        p "Руи стой!"

                        show rui angry:
                            ease 0.7 xalign -0.6
                        pause 0.7
                        show rui angry zorder 11:
                            zoom 1.4 xalign -1.0 yalign 0.4
                            ease 0.7 xalign 0.5

                        pause 0.6
                        show rui ubeysa1 with Dissolve(.1):
                            yalign 0.5 zoom 1.2 xalign 0.5

                        window show

                        $ rui_pain_add('31')
                        
                        r "Не смей так разговаривать со мной!"

                        play sound udar
                        with hpunch

                        stop music

                        scene black with Dissolve(.3)

                        jump rui_home_poh

        "А это можно мне в жопу вставить?":

            p "Слушай, а раз ядерка такая маленькая, то её можно мне в жопу вставить?"

            show rui shock at sd

            r "[player_name]... {w=1}У тебя очень странные сексуальные фантазии..."

            p "Ну так можно или нет?"

            show rui sad at sd

            r "Чисто теоретически можно, но ты ведь понимаешь насколько это опасно?"

            p "Ну если не нажимать на пульт, то она не активируется, так?"

            r "Так то оно так, но к чему весь этот разговор?"

            p "Нет времени объяснять, суй ядерку мне в жопу!"

            r "..."

            p "Мне кажется, это будет интересный опыт..."

            show rui hello at sd

            r "[player_name]... {w=0.5}Если тебе хочется новых ощущений, то я могу придумать что-нибудь, что в случае чего не разорвёт тебя на 1000-7 частей."

            r "Я, конечно, уверен в своём изобретении. Но всё же, бомба это не то, что стоит сувать в жопу."

            p "Руи..."

            show rui sad at sd

            r "Почему ты так грустно смотришь... Ты действительно так сильно хочешь трахан трахан чпокен чпокен с ядеркой?"

            p "Да."

            show rui hello at sd

            r "Что ж с тебя взять то... "

            show rui happy at sd

            extend "Ладно уж, пойдём попробуем~"

            jump mi_budem_bum_bum

    return


# Руи идёт к психологу или ты лох (КОНЦОВКА)
label rui_go_psiholoc:

    p "Я и впрямь считаю, что тебе стоит обратиться к психотерапевту... Тебе нужна помощь!"

    stop music fadeout 1.0

    show rui shock at sd

    r "[player_name]... Но почему ты так думаешь?"

    $ renpy.notify('Отвечайте правильно как можно быстрее!')

    play music dark fadein 1.5
    show rui panic at sd

    $ timerm = True
    $ timerz = 5
    $ time_range = 5
    $ marker = 'rui_go_psiholoc.no'

    menu:

        "Ты стал более замкнутым":

            $ go_psiholoc += 1

            p "Ты стал более замкнут в себе."

        "Ты чмошник":

            label .no:

                $ go_psiholoc -= 1

                p "Ты чмошник!"

    $ nl = [1, 2, 3, 4, 5]
    $ renpy.random.shuffle(nl)

    $ timerz = 4
    $ time_range = 4

    call .nw(0) from _call_rui_go_psiholoc_nw

    $ timerz = 3.5
    $ time_range = 3.5

    call .nw(1) from _call_rui_go_psiholoc_nw_1

    $ timerz = 3
    $ time_range = 3

    call .nw(2) from _call_rui_go_psiholoc_nw_2

    $ timerz = 2
    $ time_range = 2

    call .nw(3) from _call_rui_go_psiholoc_nw_3

    $ timerz = 1.5
    $ time_range = 1.5

    call .nw(4) from _call_rui_go_psiholoc_nw_4

    stop music fadeout 1.0
    r shock "[player_name]!"

    if go_psiholoc > 2:
        jump .true_ps
    else:

        play music nn1 fadein 1.0

        $ renpy.notify('Вы проиграли!')

        $ timerm = False

        show rui angry at sd

        r "Что ты такое начала тут?"

        r "Как ты можешь обвинять меня в стольких вещах!"

        play sound udar2
        with hpunch

        $ rui_pain_add('32')

        p "Ай! Руи!"

        r "Да как ты можешь... {w=1}Я столько всего для тебя делаю, а ты вот как..."

        show rui panic1 at sd

        r "Нет, [player_name], так дела не пойдут."

        show rui panic1:
            ease 0.7 xalign -0.6
        pause 0.7
        show rui panic1 zorder 11:
            zoom 1.4 xalign -1.0 yalign 0.4
            ease 0.7 xalign 0.5

        pause 0.6
        show rui ubeysa1 with Dissolve(.1):
            yalign 0.5 zoom 1.2 xalign 0.5

        r "Придётся показать тебе, {sc}{i}{=norm_style}как сильно я тебя люблю!{/i}{/sc}"

        window show

        $ rui_pain_add('33')

        p "Руи!{w=0.3}{nw}"

        play sound udar
        with vpunch

        stop music

        scene black with Dissolve(.3)

        $ rui_psyho = True

        jump rui_home_poh

    label .nw(num):

        $ i = num

        if nl[i] == 1:
            call .n1 from _call_rui_go_psiholoc_n1
        elif nl[i] == 2:
            call .n2 from _call_rui_go_psiholoc_n2
        elif nl[i] == 3:
            call .n3 from _call_rui_go_psiholoc_n3
        elif nl[i] == 4:
            call .n4 from _call_rui_go_psiholoc_n4
        elif nl[i] == 5:
            call .n5 from _call_rui_go_psiholoc_n5

        return

    label .n1:
        r "...{w=0.3}{nw}"
        $ marker = 'rui_go_psiholoc.no1'
        menu:

            "Ты одержим мной":

                label .no1:

                    $ go_psiholoc -= 1

                    p "Ты одержим мной!"

            "Иногда ты меня пугаешь":

                $ go_psiholoc += 1

                p "Иногда ты меня пугаешь..."
        return

    label .n2:
        r "[player_name]...{w=0.3}{nw}"
        $ marker = 'rui_go_psiholoc.no2'
        menu:

            "Ты причинял мне боль":

                $ go_psiholoc += 1

                p "Ты причинял мне боль, Руи... Ты же любишь меня.."

            "Из-за тебя я страдаю":

                label .no2:

                    $ go_psiholoc -= 1

                    p "Из-за тебя я страдаю, Руи..."
        return

    label .n3:
        r "Я...{w=0.3}{nw}"
        $ marker = 'rui_go_psiholoc.no3'
        menu:

            "Тебе неважно моё мнение":

                $ go_psiholoc += 1

                p "Тебе неважно моё мнение..."

            "Я для тебя ничего не значу":

                label .no3:

                    $ go_psiholoc -= 1

                    p "Я для тебя ничего не значу!"

        return

    label .n4:
        r "Что...{w=0.3}{nw}"
        $ marker = 'rui_go_psiholoc.no4'
        menu:

            "Ты променял своих друзей на меня":

                label .no4:

                    $ go_psiholoc -= 1

                    p "Ты променял своих друзей на меня!"

            "Ты отстранился от своих друзей":

                $ go_psiholoc += 1

                p "Ты отстранился от своих друзей."
        return

    label .n5:
        r "Но...{w=0.3}{nw}"
        $ marker = 'rui_go_psiholoc.no5'
        menu:

            "Ты ущемляешь моё личное пространство":

                label .no5:

                    $ go_psiholoc -= 1

                    p "Ты ущемляешь моё личное пространство!"

            "Ты не отходишь от меня ни на шаг":

                $ go_psiholoc += 1

                p "Ты не отходишь от меня ни на шаг..."

        return

    label .true_ps:

        play music low volume 2.3

        $ renpy.notify('Вы победили!')

        show rui sad at sd

        r "Я... Я думаю, ты права..."

        if not persistent.ps_win:
            $ get_ach('reshala')
            $ persistent.ps_win = True

        p "..."

        r "Прости меня... Я действительно не замечал сколько боли тебе приношу..."

        p "Всё хорошо... Главное, что сейчас ты осознал свои ошибки и хочешь исправиться, верно?"

        show rui hello at sd

        r "Да, ты права! {w=1}Спасибо тебе, [player_name]..."

        p "Хе-хе, да не за что!"

        show rui hello:
            ease 0.7 xalign -0.6
        pause 0.7
        show rui hello zorder 11:
            zoom 1.4 xalign -1.0 yalign 0.4
            ease 0.7 xalign 0.5

        pause 1.0

        r "[player_name]..."

        play sound undress
        scene black with Dissolve(.3)

        "Руи нежно и осторожно обнимает вас."

        r "Я так тебя люблю, [player_name]... {w=1}Прости за всё, что делал. Прости за все эти страдания. Теперь я исправлюсь.. клянусь пультом от ядерки..."

        p "От какой ядерки?"

        scene bg kitchen talk
        show kitchen talk zorder 10
        show rui shock zorder 11:
            zoom 1.4 xalign 0.5 yalign 0.4
        with Dissolve(.3)

        r "Ой..."

        show rui happy at sd(ypos=0.4)

        extend " Ну я сам смог собрать ядерку..."

        p "..."

        p "Не говори только психотерапевту об этом..."

        show rui hello at sd(ypos=0.4)

        r "Хе-хе~"

        scene end rui rui_ps with Fade(0.5, 0.5, 0.5)

        "После этого Руи и впрям прошёл курс психотерапии. Его ментальное состояние заметно улучшилось."

        "Он перестал агриться на вас за любой чих, он дал вам больше личного пространства, вы вместе стали проводить больше времени с его друзьями и за постановкой шоу."

        scene black with dissolve

        'Наконец, ваши отношения стали здоровыми... {p=1}В будущем вы выйдите за Руи замуж, у вас родится ребёнок, он будет гением и в 16 лет создаст игру "Yandere pjSEKAI boys". Вы ахуете и запрёте его в подвале за это.'

        "Вот она, жизнь мечты..."

        window hide

        call ends_rui("rui_ps") from _call_ends_rui_14

        pause 5.0

    return

# гг достаёт телефон (+СЕКРЕТНАЯ концовка)
label telephon:

    show screen timerr

    label .tele_vibor:

        "Чем заняться?"

        menu:

            "Генератор рандомных чисел":

                "Отличный выбор! Вы любите пытаться отгадать какое число выведет генератор!"

                jump .gen

            "Поиграть в любимую игру":

                "Вашей любимой игрой является конечно же Yandere pjSEKAI boys!"

                jump .petlya

            "Начать смотреть тикток":

                "Вы решили посмотреть тикток..."

                jump .tiktok

    label .tiktok:

        hide screen timerr

        if from_loc == "rui_kitchen":

            r angry "[player_name], ты серьёзно решила посмотреть тикток на полной громкости, пока я тебе тут всё рассказываю?"

            jump rui_posle_tsu.ti_chto

    label .gen:

        if vic3 and vic5 and vic9:

            hide screen timerr

            "О боже! Вы угадали все числа... Вы точно человек?"

            if from_loc == "rui_kitchen":

                jump rui_posle_tsu.gen_win

        "Хмм... Сколько чисел должен генерировать генератор?"

        menu:

            "от 1 до 3" if not vic3:

                $ gen_n1 = "1"
                $ gen_n2 = "3"
                $ gen_allow = "123"
                $ gen_value = ""

                show screen inputrangen 

                "Итак, загадайте число от 1 до 3!"

                pause 0.2

                $ gen_tr = renpy.random.choice(["1", "2", "3"])

                show screen rangen

                pause 0.2

                if gen_value == "":

                    "Ха, вы ничего не ввели... И в чём смысл этой игры?"

                elif gen_value == gen_tr:

                    if '3' not in persistent.rangen_all:
                        $ nn_list = persistent.rangen_all
                        $ nn_list.append('3')
                        $ persistent.rangen_all = nn_list
                        $ get_ach('mega_rangen')

                    "Ничего себе! Вы угадали! Да вы круты. Можете попробовать более сложные уровни или сыграть во что-нибудь другое."

                    $ vic3 = True

                else:

                    "Вы не угадали, ха-ха. Можете попробовать ещё раз или сыграть во что-нибудь другое."

                jump .gen

            "от 1 до 5" if not vic5:

                $ gen_n1 = "1"
                $ gen_n2 = "5"
                $ gen_allow = "12345"
                $ gen_value = ""

                show screen inputrangen

                "Итак, загадайте число от 1 до 5!"

                pause 0.2

                $ gen_tr = renpy.random.choice(["1", "2", "3", "4", "5"])

                show screen rangen

                pause 0.2

                if gen_value == "":

                    "Ха, вы ничего не ввели... И в чём смысл этой игры?"

                elif gen_value == gen_tr:

                    if '5' not in persistent.rangen_all:
                        $ nn_list = persistent.rangen_all
                        $ nn_list.append('5')
                        $ persistent.rangen_all = nn_list
                        $ get_ach('mega_rangen')

                    "Ничего себе! Вы угадали! А ведь это повышенная сложность! Можете попробовать более сложные уровни или сыграть во что-нибудь другое."

                    $ vic5 = True

                else:

                    "Вы не угадали, ха-ха. Можете попробовать ещё раз или сыграть во что-нибудь другое."

                jump .gen

            "от 0 до 9" if not vic9:

                $ gen_n1 = "0"
                $ gen_n2 = "9"
                $ gen_allow = "0123456789"
                $ gen_value = ""

                show screen inputrangen

                "Итак, загадайте число от 0 до 9!"

                pause 0.2

                $ gen_tr = renpy.random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

                show screen rangen

                pause 0.2

                if gen_value == "":

                    "Ха, вы ничего не ввели... И в чём смысл этой игры?"

                elif gen_value == gen_tr:

                    if '10' not in persistent.rangen_all:
                        $ nn_list = persistent.rangen_all
                        $ nn_list.append('10')
                        $ persistent.rangen_all = nn_list
                        $ get_ach('mega_rangen')

                    "Ничего себе! Вы угадали! Вы точно не жульничали?.. Хм..."

                    $ vic9 = True

                else:

                    "Вы не угадали... Что ж, ожидаемо. Можете попробовать ещё раз или сыграть во что-нибудь другое."

                jump .gen

            "Сыграть в что-нибудь другое":

                jump .tele_vibor

    label .petlya:

        hide screen timerr

        if persistent.petlya >= 1:

            $ s4_add('2')

            "..."

            "Ха-ха, вы вернулись~"

            stop music fadeout 1.0

            "Так... К чёрту музыку, фон и всё остальное!"

            scene black with Dissolve(.3)

            "Отлично... Раз вы вернулись, то вам действительно хочется узнать чего-то интересного про эту игру или её автора?"

            "Хотя возможно, вам просто нравится ломать четвёртые стены в играх... Ну тогда это уже ваши заботы."

            "С чего бы начать... {w=1}с чего бы начать?"

            "Давайте я расскажу что-нибудь про минусы игры, хм..."

            "..."

            "Раньше в игре было много ошибок, но сейчас... {w=2}Их почти нет... Нофанру всё время исправляет ошибки."

            "С каждым обновлением эта секретная концовка становится всё быссмысленнее и быссмысленнее..."

            "Знаете, я могу сказать, что код в игре ОЧЕНЬ запутан и название переменных часто не имеют смысла! {w=0.5}Вот и минус!"

            "Хм, код действительно хорошо работает и так как разработчик один, наверное, всё равно как внешне выглядит код..."

            "..."

            "На самом деле, я не хочу срать на Нофанру сейчас, это уже сделали люди из фандома. {w=0.5}И это... {w=0.5}печально..."

            "Я вижу, как она старается над этой игрой, как тратит своё время, нервы и силы, чтобы сделать всё как можно лучше."

            'А в конечном итоге люди перечёркивают все эти старания одним "это отвратительно" или "это рушит канон".'

            "Игра сделана ради шутки и опыта и никому не вредит..."
            
            "Так почему люди реагируют так, будто она эту игру сделали с реальным человеком, а не с персонажем?"

            "Когда-нибудь люди просто начнут игнорировать то, что им не нравится, и мир станет лучше."

            "Знаю, знаю, кто-то скажет, что это меняет восприятие персонажа и все дела."

            "Но виновата ли в этом новелла, в которой в начале чётко сказано, что она не имеет ничего общего с каноном?"

            "А разве до появления этой новеллы этой проблемы не было?"

            "Возможно, это в какой-то степени усугубило ситуацию, но хейтит автора за это явно не выход."

            "..."

            "Я устал..."
            
            "Я не хочу больше концентрироваться на плохом."

            "Сейчас я просто хочу сказать спасибо тем, кто поддерживает Нофанру и эту игру."

            "Игрок, [player_name]... {w}Спасибо тебе за то, что ты играешь в эту игру. Спасибо тебе за всё."

            "Я и сама NoFanru действительно очень ценим это и надеемся, что ты и дальше будешь играть в эту игру."

            "Спасибо..."

            window hide

            pause 0.3

            show end secret thank with dissolve

            call ends_secret("thank") from _call_ends_secret_1

            return
        
        else:

            $ s4_add('3')

            stop music fadeout 2.0

            "..."

            "Хм... Вам не кажется, что это немного ломает четвёртую стену, нет?"

            "А, впрочем, вы не сможете ответить на этот вопрос, если {sc=2}{i}{=norm_style}я этого не захочу{/i}{/sc}, хихи~"

            scene black with Dissolve(.3)

            "Вообще {b}моя{/b} роль в игре очень недооценена! {p}Рассказчиком быть сложно..."

            "Знаете, я бы мог сейчас рассказать абсолютно все секреты этой игры и его автора... {w=1}Хм..."

            "Например, вы знали, что изначальна первым планировался не Руи?"

            "Ну ладно, наверное, вас уже достали мои разговоры, не смею больше вас отвлекать, счастливой игры в Yandere pjSEKAI boys!"

            $ persistent.petlya = int(2)

            return

    return

# победа в генераторе чисел (СЕКРЕТНАЯ концовка)
label rangen:

    stop music fadeout 2.0

    scene black with Dissolve(.3)

    "От вас отвернулись все ваши друзья, родные и близкие. Генератор рандомных чисел теперь заменяет их."

    ks1 "Такова ли конца ты хотел?.."

    window hide

    call ends_secret("genran") from _call_ends_secret_2

    pause 5.0

    return

# смачный минет Руи (2 КОНЦОВКИ)
label rui_minet:

    stop music fadeout 1.0

    window hide

    scene rui minet1 with Fade(0.3, 0.5, 0.3)

    play music sexmusic fadein 2.5 volume 0.3

    pause 0.3

    window show

    r "Ты готова, [player_name]?"

    p "Да... Я думаю.."

    r "Начинай~"

    window hide

    show rui minet2 with dissolve

    pause 0.8

    show rui minet3 with Dissolve(.3)

    window show

    p "..."

    r "Смелее, [player_name]~"

    show rui minet4

    pause 0.5

    play sound zip
    show rui minet5 with Dissolve(.1)

    p "Ох..."

    r "Всё в порядке, [player_name], Руи-младший уже заждался тебя~"

    p "Ну привет, Руи-младший..."

    show rui minet5:
        "rui minet6" with Dissolve(.1)

    p "..."

    show rui minet6:
        "rui minet7" with Dissolve(.1)

    r "Мх~"

    r "..."

    r "[player_name]..."

    show rui minet7:
        "rui minet8" with Dissolve(.1)

    r "Используй свой рот уже для этого."

    p "..."

    if igra_deivstvie:

        r "В конце концов, я ведь именно это загадал~"

    else:

        r "В конце концов, ты ведь именно это и предложила."

    p "..."

    menu:

        "[[Начать сосать]":

            $ var =1

            scene black with Dissolve(.3)

            "Вы закрываете глаза и берёте Руи-младшего в рот."

            r "Ха-ха, так сразу~"

            r "Ах... да... хорошо... {w=1}Не забывай ещё использовать свой язык, когда делаешь это... да... вот так.."

        "Мне страшно":

            $ var = 2

            p "Мне страшно, Руи..."

            r "Ох, не волнуйся, малышка, просто попробуй взять его в рот."

            scene black with Dissolve(.3)

            "Вы закрываете глаза и берёте Руи-младшего в рот."

            r "А теперь просто начинай двигаться вперёд-назад... {w=1}Ах... да, вот так."

            r "Не забывай использовать свой язык, когда мой член внутри~"

            r "О да.. вот так, ах... Хорошо..."

            r "Вот видишь, это не так страшно."

        "Я передумала":

            p "Я передумала..."

            play sound udar2
            with hpunch

            scene black with Dissolve(.3)

            $ rui_pain_add('34')

            "Вы чувствуете как Руи жестоко открывает вам рот и суёт свой хуй."

            r "Ты не можешь просто взять и передумать, шлюха!"

            menu:
            
                "Сопротивляться":

                    $ rui_horny_add('9') 

                    "Вы начали пытаться ударить его и вырваться."

                    play sound udar2

                    show end rui zastavlal with Dissolve(.3)

                    $ rui_pain_add('35')

                    r "Не пытайся даже сопротивляться!"

                    p "..."

                    r "[player_name], ты же знаешь, что так дела не делаются... Нельзя сначала предложить, а потом послать!"

                    p "Отпусти меня! Я тебя ненавижу!"

                    scene black with Dissolve(.3)

                    r "Займи свой рот лучше моим младшим!"

                "Поплакать и смириться":

                    $ rui_horny_add('10') 

                    "Вы начинаете плакать, осознавая, что ничего не можете поделать сейчас."

                    show end rui zastavlal with Dissolve(.3)

                    r "Что-то не так, [player_name]?"

                    p "..."

                    r "Бедняжка..."

                    show black with Dissolve(.3)

                    r "Уверен, на деле тебе нравится это~"

            "Руи снова трахавает вас в рот."

            "Кажется, он действительно наслаждается этой ситуацией... {p}И вы никогда и ничего не сможете с этим поделать..."

            "Ваши отношения обречены быть такими навечно."

            window hide

            call ends_rui("zastavlal") from _call_ends_rui_15

            pause 5.0

            return

    r "У тебя отлично получается делать это, [player_name]~"

    r "Да... Ах... Как хорошо..."

    "Руи осторожно берёт вас за голову и начинает двигаться, задавая вам нужный ритм."

    r "О да! Да! Это просто великолепно, [player_name]!"

    "Спустя время, вы чувствуете, как он кончает вам в рот."

    scene end rui minet with Dissolve(.3)

    if igra_deivstvie:
        if 'minet' not in persistent.pravda_or_deistvie:
            $ nn_list = persistent.pravda_or_deistvie
            $ nn_list.append('minet')
            $ persistent.pravda_or_deistvie = nn_list
            $ get_ach('play_as')

    "Вы падаете на пол и глотаете сперму Руи."

    r "Ах.. ах... Это действительно было хорошо... Тебе понравилось, [player_name]?"

    p "Что-то в этом есть..."

    r "Ха-ха, я рад~"

    "Кажется, вы действительно находите что-то приятнее в этом..."

    if var == 1:
        $ rui_horny_add('11')
    else:
        $ rui_horny_add('12')

    "Вы довольны тем к чему пришли ваши отношения с Руи."

    window hide

    call ends_rui("minet") from _call_ends_rui_16

    pause 5.0

    return    