init python:
    def textsound_callback(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/ui_sfx/text.flac", channel="text", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="text", fadeout=0.25)

#####################################################
## персонажи
#####################################################



define narrator = Character(callback=textsound_callback)
define p = Character('     [player_name]', color="#dadada", callback=[name_callback, textsound_callback], cb_name=None)
define noc = Character('     ???', color='#fff', callback=textsound_callback)
define nq = Character('     ???', color='#fff')

define r = Character(_('     Руи'), color="#BB88ED", image='rui', callback=[name_callback, textsound_callback], cb_name='rui')
define ts = Character(_('     Цукаса'), color="#FFBB00", image='tsukasa', callback=[name_callback, textsound_callback], cb_name='tsukasa')

define ne = Character(_('     Нене'), color="#34DD9A", image='nene', callback=[name_callback, textsound_callback], cb_name='nene')
define e = Character(_('     Эму'), color="#FF66BC", image='emu', callback=[name_callback, textsound_callback], cb_name='emu')

define m = Character(_('     Мику'), color="#33CCBA", image='miku', callback=[name_callback, textsound_callback], cb_name='miku')
define k = Character(_('     Кайто'), color="#3f7df9", image='kaito', callback=[name_callback, textsound_callback], cb_name='kaito')
define kw = Character(_('     WxS Кайто'), color="#3f7df9", image='kaito_wxs', callback=[name_callback, textsound_callback], cb_name='kaito_wxs')

define pol = Character(_('     Полицейский'), color='#fff', callback=textsound_callback)
define sud = Character(_('     Судья'), color='#fff', callback=textsound_callback)
define ved = Character(_('     Ведущий'), color='#fff', callback=textsound_callback)
define tel = Character (_("     Телефон"), color='#fff', callback=textsound_callback)

# изображения персонажей для авто-выделения

image rui angry0 = At('rui angry', sprite_highlight('rui'))
image rui sad0 = At('rui sad', sprite_highlight('rui'))
image rui hello0 = At('rui hello', sprite_highlight('rui'))
image rui shock0 = At('rui shock', sprite_highlight('rui'))
image rui panic0 = At('rui panic1', sprite_highlight('rui'))
image rui blush0 = At('rui blush', sprite_highlight('rui'))
image rui org10 = At('rui org1', sprite_highlight('rui'))
image rui org20 = At('rui org2', sprite_highlight('rui'))
image rui org30 = At('rui org3', sprite_highlight('rui'))
image rui org40 = At('rui org4', sprite_highlight('rui'))
image rui org50 = At('rui org5', sprite_highlight('rui'))

image tsukasa srs0 = At('tsukasa srs', sprite_highlight('tsukasa'))
image tsukasa shock0 = At('tsukasa shock', sprite_highlight('tsukasa'))
image tsukasa scream0 = At('tsukasa scream', sprite_highlight('tsukasa'))
image tsukasa pain0 = At('tsukasa pain', sprite_highlight('tsukasa'))
image tsukasa hard0 = At('tsukasa hard', sprite_highlight('tsukasa'))
image tsukasa hard say0 = At('tsukasa hard say', sprite_highlight('tsukasa'))
image tsukasa ehe0 = At('tsukasa ehe', sprite_highlight('tsukasa'))
image tsukasa s70 = At('tsukasa s7', sprite_highlight('tsukasa'))
image tsukasa h10 = At('tsukasa h1', sprite_highlight('tsukasa'))
image tsukasa blush0 = At('tsukasa blush', sprite_highlight('tsukasa'))
image tsukasa s30 = At('tsukasa s3', sprite_highlight('tsukasa'))
image tsukasa s50 = At('tsukasa s5', sprite_highlight('tsukasa'))
image tsukasa s20 = At('tsukasa s2', sprite_highlight('tsukasa'))
image tsukasa s10 = At('tsukasa s1', sprite_highlight('tsukasa'))
image tsukasa org10 = At('tsukasa org1', sprite_highlight('tsukasa'))

image nene uh0 = At('nene uh', sprite_highlight('nene'))
image nene blush0 = At('nene blush', sprite_highlight('nene'))
image nene sad0 = At('nene sad', sprite_highlight('nene'))
image nene org10 = At('nene org1', sprite_highlight('nene'))
image nene org20 = At('nene org2', sprite_highlight('nene'))
image nene org30 = At('nene org3', sprite_highlight('nene'))

image emu hello0 = At('emu hello', sprite_highlight('emu'))
image emu happy hah0 = At('emu happy hah', sprite_highlight('emu'))
image emu blush0 = At('emu blush', sprite_highlight('emu'))
image emu org10 = At('emu org1', sprite_highlight('emu'))
image emu org20 = At('emu org2', sprite_highlight('emu'))
image emu org30 = At('emu org3', sprite_highlight('emu'))
image emu org40 = At('emu org4', sprite_highlight('emu'))

image kaito happy0 = At('kaito happy', sprite_highlight('kaito'))
image kaito angry0 = At('kaito angry', sprite_highlight('kaito'))
image kaito hello0 = At('kaito hello', sprite_highlight('kaito'))
image kaito sad0 = At('kaito sad', sprite_highlight('kaito'))
image kaito smile0 = At('kaito smile', sprite_highlight('kaito'))
image kaito srs0 = At('kaito srs', sprite_highlight('kaito'))
image kaito think0 = At('kaito think', sprite_highlight('kaito'))
image kaito tuch0 = At('kaito tuch', sprite_highlight('kaito'))
image kaito shock0 = At('kaito shock', sprite_highlight('kaito'))
image kaito blush0 = At('kaito blush', sprite_highlight('kaito'))

image kaito_wxs happy0 = At('kaito_wxs happy', sprite_highlight('kaito'))
image kaito_wxs shock0 = At('kaito_wxs shock', sprite_highlight('kaito'))
image kaito_wxs normal0 = At('kaito_wxs normal', sprite_highlight('kaito'))
image kaito_wxs sad0 = At('kaito_wxs sad', sprite_highlight('kaito'))
image kaito_wxs srs0 = At('kaito_wxs srs', sprite_highlight('kaito'))
image kaito_wxs think0 = At('kaito_wxs think', sprite_highlight('kaito'))

image kaito_wxs happy1 = At('kaito_wxs happy', sprite_highlight('kaito_wxs'))
image kaito_wxs shock1 = At('kaito_wxs shock', sprite_highlight('kaito_wxs'))
image kaito_wxs normal1 = At('kaito_wxs normal', sprite_highlight('kaito_wxs'))
image kaito_wxs sad1 = At('kaito_wxs sad', sprite_highlight('kaito_wxs'))
image kaito_wxs srs1 = At('kaito_wxs srs', sprite_highlight('kaito_wxs'))
image kaito_wxs think1 = At('kaito_wxs think', sprite_highlight('kaito_wxs'))
image kaito_wxs blush1 = At('kaito_wxs blush', sprite_highlight('kaito_wxs'))

image miku sad0 = At('miku sad', sprite_highlight('miku'))
image miku shock0 = At('miku shock', sprite_highlight('miku'))
image miku smile0 = At('miku smile', sprite_highlight('miku'))
image miku think0 = At('miku think', sprite_highlight('miku'))




#####################################################
## важные переменные
#####################################################

default persistent.update_004 = False

default persistent.update_end = False

default persistent.petlya = int(0)

default persistent.low = 1 if renpy.variant("android") or renpy.variant("ios") else 0

# имя
default persistent.name = ""
define thisname = ""

define every_false = False #всегда ложное, нужно для теста

default persistent.ends_spisok = False #делает из галереи концовок список

define timerm = False #таймер для выбора

define gen_value = "" #пустое значение в генераторе рандомных чисел

default persistent.time_secret = ""
default persistent.time_secret_list = []

# с бетки на релиз
default persistent.con_go_rui_home = False
default persistent.con_rui_con_poh = False

default persistent.in_game_menu = False

define allow_text_input = "йцукеёнгшщзхъфывапролджэячсмитьбюЙЦУКЕЁНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm" + str(allow_text_input_tl)


#####################################################
## переходы
#####################################################

# основа
transform sd1:

    animation

    on replaced:
        animation
        yoffset 0
        linear 0.15 yoffset 9
        alpha 0.0

    on replace:
        animation
        alpha 0.0
        pause 0.14
        yoffset 9 alpha 1.0
        linear 0.05 yoffset 12 
        ease 0.07 yoffset -5
        ease 0.02 yoffset 0


# transform sd(child):

#     yoffset 0
#     linear 0.14 yoffset 9

#     child
#     yoffset 9 alpha 1.0
#     linear 0.05 yoffset 12 
#     ease 0.07 yoffset -5
#     ease 0.02 yoffset 0

init -2:

    transform sd(child, dt=.25, dyz=.01, dxz=.005, ypos=1.0):
        subpixel True
        yanchor ypos
        yalign ypos
        xzoom 1 yzoom 1
        easein dt*.35 yzoom 1+dyz xzoom 1-dxz 
        easeout dt*.35 yzoom 1 xzoom 1
        child
        easein dt*.15 yzoom 1-dyz xzoom 1+dxz
        easeout dt*.15 yzoom 1 xzoom 1


transform dison(pa, ti):
    alpha 0.0
    pause pa
    ease ti alpha 1.0

transform disoff(pa, ti):
    alpha 1.0
    pause pa
    ease ti alpha 0.0

transform disall(pa1, ti1, pa2, ti2):
    on show:
        alpha 0.0
        pause pa1
        ease ti1 alpha 1.0
    on hide:
        alpha 1.0
        pause pa2
        ease ti2 alpha 0.0


# отсутствие перехода
transform none:

    alpha 1.0




#####################################################
## эффекты
#####################################################


# одиначное моргание, глаза полу-открыты
transform blink_short_not:
    .05
    "eye-open" with Dissolve(.05)
    .1
    "eye-half" with Dissolve(.05)
    .1
    "eye-close" with Dissolve(.05)
    .1
    "eye-close-true" with Dissolve(.05)
    .2
    "eye-close" with Dissolve(.05)
    .1
    "eye-half" with Dissolve(.05)

transform blink1:
    "eye-half"
    .1
    "eye-close" with Dissolve(.05)
    .1
    "eye-close-true" with Dissolve(.05)

transform blink2:
    "eye-close-true" 
    .1
    "eye-close" with Dissolve(.05)
    .1
    "eye-half" with Dissolve(.05)

transform blink3:
    "eye-half"
    .1
    "eye-close" with Dissolve(.05)
    .1
    "eye-close-true" with Dissolve(.05)
    .2
    "eye-close" with Dissolve(.05)
    .1
    "eye-half" with Dissolve(.05)
    .1
    "eye-close" with Dissolve(.05)
    .1
    "eye-close-true" with Dissolve(.05)
    .2
    "eye-close" with Dissolve(.05)
    .1
    "eye-half" with Dissolve(.05)

transform blink4:
    "eye-half"
    .1
    "eye-close" with Dissolve(.05)
    .1
    "eye-close-true" with Dissolve(.05)
    .2
    "eye-half" with Dissolve(.05)
    .1
    "eye-open" with Dissolve(.05)
    .1
    "eye-open-true" with Dissolve(.05)

transform blink7:
    "eye-half"
    .1
    "eye-close" with Dissolve(.05)
    .1
    "eye-close-true" with Dissolve(.05)
    .2
    "eye-half" with Dissolve(.05)
    .1
    "eye-open" with Dissolve(.05)
    .1
    "eye-open-true" with Dissolve(.05)
    .1
    alpha 0.0


transform blink5:
    "eye-open-true"
    .1
    "eye-half" with Dissolve(.05)
    .1
    "eye-close" with Dissolve(.05)
    .1
    "eye-close-true" with Dissolve(.05)

transform blink6:
    "eye-close-true" 
    .1
    "eye-close" with Dissolve(.05)
    .1
    "eye-half" with Dissolve(.05)
    .1
    "eye-open-true" with Dissolve(.05)

transform blink7:
    "eye-open-true"
    .1
    "eye-half" with Dissolve(.05)
    .1
    "eye-close" with Dissolve(.05)
    .1
    "eye-close-true" with Dissolve(.05)
    .5
    "eye-close" with Dissolve(.05)
    .1
    "eye-half" with Dissolve(.05)
    .1
    "eye-open-true" with Dissolve(.05)

transform blink_close:
    alpha 1.0
    .05
    "eye-open" with Dissolve(.05)
    .1
    "eye-half" with Dissolve(.05)
    .1
    "eye-close" with Dissolve(.05)
    .1
    "eye-close-true" with Dissolve(.05)

transform blink_open_more:
    "eye-close-true"
    .1
    "eye-close" with Dissolve(.05)
    .1
    "eye-half" with Dissolve(.05)
    .1
    "eye-open" with Dissolve(.05)
    .3
    "eye-half" with Dissolve(.05)
    .1
    "eye-close" with Dissolve(.05)
    .1
    "eye-close-true" with Dissolve(.05)
    .4
    "eye-close" with Dissolve(.05)
    .1
    "eye-half" with Dissolve(.05)
    .1
    "eye-open" with Dissolve(.05)
    .1
    "eye-open-true" with Dissolve(.05)
    .1
    ease 0.1 alpha 0.0

transform blink_open:
    "eye-close-true"
    .1
    "eye-close" with Dissolve(.05)
    .1
    "eye-half" with Dissolve(.05)
    .1
    "eye-open" with Dissolve(.05)
    .1
    "eye-open-true" with Dissolve(.05)
    .1
    ease 0.1 alpha 0.0


transform blink_no_open_more:
    "eye-close-true"
    .1
    "eye-close" with Dissolve(.05)
    .1
    "eye-half" with Dissolve(.05)
    .1
    "eye-open" with Dissolve(.05)
    .3
    "eye-half" with Dissolve(.05)
    .1
    "eye-close" with Dissolve(.05)
    .1
    "eye-close-true" with Dissolve(.05)
    .4
    "eye-close" with Dissolve(.05)
    .1
    "eye-half" with Dissolve(.05)
    .1
    "eye-open" with Dissolve(.05)
    .3
    "eye-close" with Dissolve(.05)
    .1
    "eye-close-true" with Dissolve(.05)
    .4
    "eye-close" with Dissolve(.05)
    .1
    "eye-half" with Dissolve(.05)
    .1
    "eye-open" with Dissolve(.05)


define test = ImageDissolve("test.png", 0.2)





#####################################################
## медиа
#####################################################


# видео

image end rui tsu die movie = Movie(play="images/ends/rui/end rui tsu die.webm", pos=(0.5, 0.5), anchor=(0.5, 0.5), size=(1080, 1080))
image end rui die movie = Movie(play="images/ends/rui/end rui die.webm", pos=(0.5, 0.5), anchor=(0.5, 0.5), size=(1920, 1080))
image r wtf movie = Movie(play="images/rui/rui wtf.webm", pos=(0.5, 0.5), anchor=(0.5, 0.5))

image tv rui3mv = Movie(play='videos/tv rui3.webm', pos=(0.5, 0.5), anchor=(0.5, 0.5), size=(1920, 1080), image='images/rui/tv rui4.webp', loop=False)

image r wtf low:
    "rui wtf1"
    pause 0.3
    "rui wtf2"
    pause 0.3
    "rui wtf1"
    pause 0.3
    "rui wtf3"
    pause 0.3
    repeat

# изображения

image end rui happy m:
    "end rui happy"
    choice:
        pause 1.8
    choice:
        pause 2.5
    choice:
        pause 2.0
    choice:
        pause 1.5
    "end rui happy-0"
    choice:
        pause 0.1
    choice:
        pause 0.3
    choice:
        pause 0.2
    repeat

image bg rui nome s1:
    "bg rui nome s1-1"
    choice:
        pause 1.8
    choice:
        pause 2.5
    choice:
        pause 2.0
    choice:
        pause 1.5
    "bg rui nome s1-2"
    choice:
        pause 0.1
    choice:
        pause 0.3
    choice:
        pause 0.2
    repeat

image bg rui nome s2:
    "bg rui nome s2-1"
    choice:
        pause 1.8
    choice:
        pause 2.5
    choice:
        pause 2.0
    choice:
        pause 1.5
    "bg rui nome s2-2"
    choice:
        pause 0.1
    choice:
        pause 0.3
    choice:
        pause 0.2
    repeat

image bg rui nome s3:
    "bg rui nome s3-1"
    choice:
        pause 1.8
    choice:
        pause 2.5
    choice:
        pause 2.0
    choice:
        pause 1.5
    "bg rui nome s3-2"
    choice:
        pause 0.1
    choice:
        pause 0.3
    choice:
        pause 0.2
    repeat

image bg rui nome s4:
    "bg rui nome s4-1"
    choice:
        pause 1.8
    choice:
        pause 2.5
    choice:
        pause 2.0
    choice:
        pause 1.5
    "bg rui nome s4-2"
    choice:
        pause 0.1
    choice:
        pause 0.3
    choice:
        pause 0.7
    repeat

image bum:
    "bg room"
    pause 0.2
    "bg bum"
 
image rui panic:
    choice:
        "rui panic1"
    choice:
        "rui panic2"
    choice:
        "rui panic3"
    choice:
        "rui panic4"
    choice:
        "rui panic5"
    choice:
        "rui panic6"
    pause 0.3
    repeat

image rui minet7:
    "rui minet71" with Dissolve(.1)
    choice:
        pause 0.5
    choice:
        pause 1
    choice:
        pause 0.2
    "rui minet72" with Dissolve(.1)
    choice:
        pause 0.5
    choice:
        pause 1
    choice:
        pause 0.2
    repeat

image rui bb6:
    "rui bb6 1" with Dissolve(.1)
    choice:
        pause 0.5
    choice:
        pause 1
    choice:
        pause 1.2
    "rui bb6 2" with Dissolve(.1)
    choice:
        pause 0.5
    choice:
        pause 1
    choice:
        pause 1.2
    repeat

image rui bb14:
    "rui bb14 1" with Dissolve(.1)
    choice:
        pause 0.5
    choice:
        pause 1
    choice:
        pause 1.2
    "rui bb14 2" with Dissolve(.1)
    choice:
        pause 0.5
    choice:
        pause 1
    choice:
        pause 1.2
    repeat

image rui bb14 fast:
    "rui bb14 1"
    choice:
        pause 0.1
    choice:
        pause 0.2
    "rui bb14 2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat



image bg beding = ConditionSwitch (
    "hour == 1", "bg bed1",
    "hour == 2", "bg bed2",
    "hour == 3", "bg bed3",
    "hour == 4", "bg bed4",
    "hour == 5", "bg bed5",
    "hour == 6", "bg bed6",
    "hour == 7", "bg bed7",
    "hour == 8", "bg bed8",
    "hour == 9", "bg bed9",
    "hour == 10", "bg bed10",
    "hour == 11", "bg bed11",
    "hour == 13", "bg bed1",
    "hour == 14", "bg bed2",
    "hour == 15", "bg bed3",
    "hour == 16", "bg bed4",
    "hour == 17", "bg bed5",
    "hour == 18", "bg bed6",
    "hour == 19", "bg bed7",
    "hour == 20", "bg bed8",
    "hour == 21", "bg bed9",
    "hour == 22", "bg bed10",
    "hour == 23", "bg bed11",
    "True", "bg bed12",
    )


image rkitchen2:
    "rkitchen2-1"
    choice:
        pause 1.8
    choice:
        pause 2.5
    choice:
        pause 2.0
    choice:
        pause 1.5
    "rkitchen2-2"
    choice:
        pause 0.1
    choice:
        pause 0.3
    choice:
        pause 0.7
    repeat

image rkitchen3:
    "rkitchen3-1"
    choice:
        pause 1.8
    choice:
        pause 2.5
    choice:
        pause 2.0
    choice:
        pause 1.5
    "rkitchen3-2"
    choice:
        pause 0.1
    choice:
        pause 0.3
    choice:
        pause 0.7
    repeat

image rkitchen4:
    "rkitchen4-1"
    choice:
        pause 1.8
    choice:
        pause 2.5
    choice:
        pause 2.0
    choice:
        pause 1.5
    "rkitchen4-2"
    choice:
        pause 0.1
    choice:
        pause 0.3
    choice:
        pause 0.7
    repeat

image rkitchen6:
    "rkitchen6-1"
    choice:
        pause 1.8
    choice:
        pause 2.5
    choice:
        pause 2.0
    choice:
        pause 1.5
    "rkitchen6-2"
    choice:
        pause 0.1
    choice:
        pause 0.3
    choice:
        pause 0.7
    repeat

image rkitchen7:
    "rkitchen7-1"
    choice:
        pause 1.8
    choice:
        pause 2.5
    choice:
        pause 2.0
    choice:
        pause 1.5
    "rkitchen7-2"
    choice:
        pause 0.1
    choice:
        pause 0.3
    choice:
        pause 0.7
    repeat

image rkitchen8:
    "rkitchen8-1"
    choice:
        pause 1.8
    choice:
        pause 2.5
    choice:
        pause 2.0
    choice:
        pause 1.5
    "rkitchen8-2"
    choice:
        pause 0.1
    choice:
        pause 0.3
    choice:
        pause 0.7
    repeat

image rkitchen9:
    "rkitchen9-1"
    choice:
        pause 1.8
    choice:
        pause 2.5
    choice:
        pause 2.0
    choice:
        pause 1.5
    "rkitchen9-2"
    choice:
        pause 0.1
    choice:
        pause 0.3
    choice:
        pause 0.7
    repeat

define wave_val = 10 if persistent.low < 2 else 15

image d 1 = WaveImage("images/effects/dream/d1.webp", amp = 20, damp = 0.0, speed=100, freq=40, direction=True, strip_height=wave_val)
image d 2 = WaveImage("images/effects/dream/d2.webp", amp = 20, damp = 0.0, speed=100, freq=40, direction=True, strip_height=wave_val)
image d 3 = WaveImage("images/effects/dream/d3.webp", amp = 20, damp = 0.0, speed=100, freq=40, direction=True, strip_height=wave_val)

init python:
    import time
    import random
    # меняющиеся изображения в экране телевизора
    class TVchanges(renpy.Displayable):

        def __init__(self):
            super(TVchanges, self).__init__()
            self.last_time = 0
            self.s = 0

        def render(self, width, height, st, at):
            render = renpy.Render(width, height)
            t = time.time()
            if t - self.last_time > self.s:
                i = random.randint(1, 5)
                im = 'tv' + str(i)
                self.image = renpy.displayable(im)
                self.s = random.uniform(2, 5)
                self.last_time = time.time()
            r = renpy.render(self.image, width, height, st, at)
            render.blit(r, (0, 0))
            renpy.redraw(self, 0)
            return render


image tv_changes = TVchanges()



# музыка

define audio.main = "music/main.ogg"

define audio.ruistart = "music/rui/start.ogg"
define audio.rui_bum = "music/rui/end.rui_boom.ogg"
define audio.dark = "music/rui/dark.ogg"
define audio.dillema = "music/rui/mystery.ogg"
define audio.sexmusic = "music/rui/ruisex.ogg"
define audio.sexhard = "music/rui/sexhard.ogg"

define audio.tsu = "music/rui/tsu.ogg"
define audio.low = "music/rui/low.ogg"
define audio.nn1 = "music/rui/nn1.ogg"
define audio.nn2 = "music/rui/nn2.ogg"
define audio.kitchen = "music/rui/kitchen.ogg"

define audio.hous_norm = "music/rui/hous-normal.ogg"
define audio.harmony = "music/rui/harmony.ogg"

define audio.doomed = "music/rui/doomed.ogg"
define audio.sad_nervis = "music/rui/sad_nervis.ogg"
define audio.stress = "music/rui/stress.ogg"
define audio.rui_home = "music/rui/rui_home.ogg"
define audio.night = "music/rui/night.ogg"

define audio.tv_ads = "music/rui/tv_ads.ogg"

define audio.lose_mind = "music/rui/lose_mind.ogg"

define audio.sekai = "music/rui/sekai.ogg"
define audio.iakes = "music/rui/iakes.ogg"


# звуки

define audio.none = "audio/none.ogg"

define audio.nofanru_rui = "audio/start/nofanru_rui.wav"

define audio.knock1 = "audio/knock1.ogg"
define audio.knock2 = "audio/knock2.ogg"
define audio.knock3 = "audio/knock3.ogg"

define audio.undress = "audio/undress.ogg"
define audio.zip = "audio/zip.ogg"
define audio.gandom = "audio/gandom.ogg"
define audio.udar = "audio/udar.flac"
define audio.udar2 = "audio/udar.mp3"
define audio.bed = "audio/bed.ogg"
define audio.boom = "audio/boom.mp3"
define audio.tresk = "audio/tresk.wav"
define audio.split = "audio/split.wav"
define audio.sud = "audio/sud.ogg"
define audio.wake = "audio/wake.ogg"
define audio.drink = "audio/drink.ogg"
define audio.steps = "audio/steps.ogg"
define audio.switch = "audio/switch.ogg"
define audio.eat = "audio/eat.ogg"
define audio.door = "audio/door.ogg"
define audio.shot = "audio/shot.flac"
define audio.glass = "audio/glass.flac"



# голос

define audio.k_aa = "audio/Potesne_me_audire/k_aa.ogg"
define audio.k_ahaha = "audio/Potesne_me_audire/k_ahaha.ogg"
define audio.k_eman = "audio/Potesne_me_audire/k_eman.ogg"
define audio.k_ja = "audio/Potesne_me_audire/k_ja.ogg"
define audio.k_mm = "audio/Potesne_me_audire/k_mm.ogg"
define audio.k_sad_um = "audio/Potesne_me_audire/k_sad_um.ogg"
define audio.k_um = "audio/Potesne_me_audire/k_um.ogg"
define audio.k_wa = "audio/Potesne_me_audire/k_wa.ogg"



#####################################################
## логические переменные
#####################################################


# руи (1 часть)

define home = True

define molchun1 = False
define opravdan1 = False
define yaderka_true = False
define yaderka_ladno = False
define yaderka_sila = False

define joke_tsu_die = False
define tsu_yeba = False
define donate = False
define chestno = False
define rui_know_tsu = False
define tsu_hurt_you = False
define tsu_lit_know = False
define tsu_say_gg = False
define igra_deivstvie = False
define dev_vp = False

define vic3 = False
define vic5 = False
define vic9 = False

define smazka = False
define sud_rui = False
define yaderka_huh = False
define rui_not_tsu = False
define rnt10 = False
define non_rui_orgia = False

default persistent.tsu_pain_beat = False
default persistent.tsu_pain_izmena = False

default persistent.sud_win_code = False
default persistent.sud_win_sud = False
default persistent.ps_win = False

define tsu_fuck = False


define rui_psyho = False

#####################################################
## числовые переменные
#####################################################

default hour = 0

# руи

define rui_ne_ebi = int(0)
define rui_ebi = int(0)
define molchun = int(0)

define za_rui = int(0)
define za_tsu = int(0)

define go_psiholoc = int(0)

define ruilove = int(0)

define kaito_state = int(100)

#####################################################
## прочие переменные
#####################################################

# руи
default persistent.markerr = ""

default persistent.rangen_all = []
default persistent.pr_world = []
default persistent.tsu_say_no_list = []
default persistent.pravda_or_deistvie = []
default persistent.s4 = []
default persistent.haha = []
default persistent.lie = []
default persistent.rui_pain = []
default persistent.pr_sled = []
default persistent.rui_horny = []

init python:
    def pr_sled_add(nnn):
        if nnn not in persistent.pr_sled:
            nn_list = persistent.pr_sled
            nn_list.append(nnn)
            persistent.pr_sled = nn_list
            get_ach('wtf')

    def s4_add(nnn):
        if nnn not in persistent.s4:
            nn_list = persistent.s4
            nn_list.append(nnn)
            persistent.s4 = nn_list
            get_ach('4s')

    def haha_add(nnn):
        if nnn not in persistent.haha:
            nn_list = persistent.haha
            nn_list.append(nnn)
            persistent.haha = nn_list
            get_ach('haha')

    def lie_add(nnn):
        if nnn not in persistent.lie:
            nn_list = persistent.lie
            nn_list.append(nnn)
            persistent.lie = nn_list
            get_ach('lie')

    def rui_pain_add(nnn):
        if nnn not in persistent.rui_pain:
            nn_list = persistent.rui_pain
            nn_list.append(nnn)
            persistent.rui_pain = nn_list
            get_ach('rui_why')

    def rui_horny_add(nnn):
        if nnn not in persistent.rui_horny:
            nn_list = persistent.rui_horny
            nn_list.append(nnn)
            persistent.rui_horny = nn_list
            get_ach('horny_rui')

