label kaito_secret:

    window hide

    stop music

    play sound "audio/ui_sfx/choice.flac"

    scene expression Solid("#fff") with test

    pause 2.0

    play music sekai fadein 3.0 volume 0.6

    scene bg sekai
    show kaito smile
    with Dissolve(5.0)

    window show

    p "Что ты задумал?"

    k "Уверен, тебе это понравится. Я досаточно постарался, чтобы изменить код игры и чтобы это сработало."

    show kaito happy at sd

    k "В этой части у тебя будет мало реплик, так что просто наслождайся."

    show kaito happy0:
        ease 0.5 xalign 0.0

    show kaito_wxs srs1:
        xalign 2.5 yalign 0.0
        ease 0.5 xalign 1.5

    kw "А? Кто-то пришёл?"

    show kaito happy0:
        xalign 0.0

    show kaito_wxs srs1:
        xalign 1.5

    show kaito_wxs shock1 at sd

    kw "А? Кайто? Что ты здесь де-{w=0.3}{nw}"

    show kaito smile0 at sd

    k "Чшш, подойди ближе."

    show kaito_wxs normal at sd:
        ease 0.7 xalign 0.5

    kw "Что такое?"

    hide kaito_wxs
    show kaito kiss
    with Dissolve(.2)

    kw "!!!"

    show kaito blush0:
        xalign 0.2 yalign 1.0
    show kaito_wxs blush:
        xalign 0.7 yalign 1.0
    with Dissolve(.2)

    kw "И что это щас было?.."

    show kaito_wxs blush1:
        yalign 1.0 yoffset 1

    k "Тш... Всё в порядке..."

    show kaito_wxs blush1:
        ease 0.3 xalign 1.3

    kw "Нет, не в порядке... {w=0.5}Зачем... Просто зачем ты это сделал?"

    show kaito angry0 at sd

    k "Успокойся, неужели ты ещё не понял?"

    k "Вайкай, ты нереален."

    show kaito_wxs normal1 at sd

    kw "..."

    k "Ты, Мику, Руи... все в этом мире лишь плод чужой извращёной фантазии."

    k "Это даже не наша первоначальная игра, а фанатаская, созданна какой-то чокнутой..."

    show kaito sad0 at sd

    k "Все мы тут лишь играем сюжет, заложенный в этом коде игры..."

    k "А самое интересное, знаешь что?"

    k 'Первый "Яндере парнем" должен был стать {b}Я{/b}, а не Руи...'

    k "Из-за этого я чувстовал обиду и изменял файлы и код игры, лез туда, куда не нужно..."

    show kaito think0 at sd

    k "А теперь автор потерял интересс к созданию этой игры, решил доделать Яндере Руи и закрыть проект."

    k "..."

    k "Яндере Кайто должен был быть первым, а по итогу его не будет вообще... {w=0.3}Только Яндере Руи... навсегда..."

    show kaito_wxs sad1 at sd

    kw "..."

    p "..."

    show kaito srs0 at sd

    k "Ну раз уже ничего не исправить, перед нами есть игрок, которому нравится такая извращённая игра."

    k "Может, на последок мы просто дадим ему больше того, ради чего и была создана это игра, что думаешь?"

    show kaito_wxs think1 at sd

    kw "..."

    kw "Наверное, в этом есть смысл..."

    show kaito smile0 at sd

    k "Я перемещу нас в более подходящее пространство."

    window hide

    stop music

    play sound "audio/ui_sfx/choice.flac"

    scene expression Solid("#fff") with test

    pause 2.0

    play sound sexmusic fadein 1.5 volume 0.2

    scene bg dream1
    show kaitocest 1
    with Dissolve(3.0)

    window show

    p "..."

    show kaitocest 1:
        "kaitocest 2" with Dissolve(.2)

    kw "Ум... Я всё же не уверен насколько это хорошая идея."

    k "Всё в порядке, просто следуй за мной."

    kw "..."

    show kaitocest 2:
        "kaitocest 3" with Dissolve(.2)

    k "[player_name], присоединяйся~"

    show black zorder 2:
        alpha 0.0
        linear 0.5 alpha 1.0
        pause 1.0
        linear 0.5 alpha 0.0

    show kaitocest 3 zorder 1:
        pause 0.6
        "kaitocest 4"

    "Кайто берёт вас и тянет к себе, располагая вас между ним и Вакаем."

    show kaitocest 4
    hide black

    "Вы чувствуете как что-то упирается вам прямо в промежность... Неужели это..."

    window hide

    show kaitocest 5 with Dissolve(.1)
    pause 0.1
    show kaitocest 6 with Dissolve(.1)

    window show

    p "!!!"

    scene black with Dissolve(.1)

    "Не дав вам успеть как-либо среагировать, Кайто затягивает вас в долгий поцелуй."

    "И не дав вам отдышаться, он поворачивает вашу голову к Вакаю и заставляет вас целоваться уже с ним."

    scene bg dream1
    show kaitocest 7
    with Dissolve(.2)

    "Наконец, вы разрываете поцелуй... {w=0.2}И осознаёте, что у вас пропали трусы! {w}И у Вакая тоже... {w}И у Кайто..."

    p "..."

    show blank at blink_close zorder 2

    "Вы зажмуриваетесь, готовясь к двойному проникновению."

    show kaitocest 8 zorder 1
    hide blank with Dissolve(.1)

    p "АХ!!!"

    "Что они реально это сделали? Вы ведь по приколу об этом подумали..."

    "Подождитие, это же уже слишком, как вообще-{w=0.3}{nw}"

    stop music
    scene black

    "..."

    k "Ох, на самом интересном..."

    k "Похоже, я всё же не могу настолько сильно менять код игры..."

    k "Прости, [player_name]... {w=0.2}И спасибо... {w=0.4}За всё..."

    k "Игра сейчас вылетит, но концовка засчитается."

    call kaito_list_lable("end") from _call_kaito_list_lable_15

    k "Пока..."

    window hide

    call ends_secret("kaito") from _call_ends_secret_4

    pause 0.2

    $ renpy.quit(status=1702)

    pause

    return