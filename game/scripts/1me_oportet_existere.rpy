style k1_style:
    size 45

style k1_style:
    variant "small"
    size 54

style k2_style:
    size 45
    color "#535372"

style k2_style:
    variant "small"
    size 54
    color "#535372"

style norm_style:
    color "#000"

define ks = Character('     {s}{k=-9}Lbjup{/k}{/s}', color="#535372")
define ks1 = Character('     {swap=Jzhsn@Lbjup@0.5}{=k1_style}.{/swap}')
define ks2 = Character('     {glitch=10}{sc}{=k2_style}Lbjup{/sc}{/glitch}')

default persistent.kaito = []
default persistent.kaito_int = int(0)

define kaito_list_full = ["name", "show", "dog", "time", "orgia", "die", "startim", "voice", "mind", "tv", "dream", "sekai", "pc", "end"]
define kaito_list = []

default kaitoim = False
default persistent.showkaito_rui = False

image bg corglitch:
    glitch("bg corridor", randomkey=None)
    pause 0.1
    glitch("bg corridor", randomkey=None)
    pause 0.1
    repeat

image bg roomglitch:
    glitch("bg room", randomkey=None)
    pause 0.1
    glitch("bg room", randomkey=None)
    pause 0.1
    repeat

image kaito shglitch:
    glitch("kaito-shhh1", randomkey=None)
    pause 0.05
    glitch("kaito-shhh1", randomkey=None)
    pause 0.05
    glitch("kaito-shhh2", randomkey=None)
    pause 0.05
    glitch("kaito-shhh2", randomkey=None)
    pause 0.05
    repeat

image tsukasa likekaito1:
    glitch("tsukasa hard", randomkey=None)
    pause 0.05
    glitch("tsukasa hard", randomkey=None)
    pause 0.05
    glitch("kaito liketsu1", randomkey=None)
    pause 0.03
    glitch("kaito liketsu1", randomkey=None)
    pause 0.03
    glitch("tsukasa hard", randomkey=None)
    pause 0.05
    "tsukasa hard"

image rui likekaito1:
    glitch("rui hello", randomkey=None)
    pause 0.05
    glitch("rui hello", randomkey=None)
    pause 0.05
    glitch("kaito likerui1", randomkey=None)
    pause 0.03
    glitch("kaito likerui1", randomkey=None)
    pause 0.03
    glitch("rui hello", randomkey=None)
    pause 0.05
    "rui hello"

image rui likekaito2:
    "rui crazy3"
    pause 0.05
    glitch("rui crazy3", randomkey=None)
    pause 0.05
    glitch("rui crazy3", randomkey=None)
    pause 0.05
    glitch("kaito likerui2", randomkey=None)
    pause 0.03
    glitch("kaito likerui2", randomkey=None)
    pause 0.03
    glitch("rui crazy3", randomkey=None)
    pause 0.05
    "rui crazy3"

image rui bbglitch:
    glitch("rui bb10", randomkey=None)
    pause 0.05
    glitch("rui bb10", randomkey=None)
    pause 0.05
    glitch("rui bb25", randomkey=None)
    pause 0.05
    glitch("rui bb10", randomkey=None)
    pause 0.05
    "rui bb25"


image tv ruiglitch:
    "tv rui4"
    pause 0.1
    glitch("tv rui4", randomkey=None)
    pause 0.05
    glitch("tv rui4", randomkey=None)
    pause 0.05
    glitch("bg rui living room", randomkey=None)
    pause 0.05
    glitch("bg rui living room", randomkey=None)
    pause 0.05
    "bg rui living room"


label kaito_list_lable(k):

    if not k in persistent.kaito:

        $ kaito_list = persistent.kaito

        $ kaito_list.insert(0, k)

        $ persistent.kaito = kaito_list

        $ persistent.kaito_int = len(persistent.kaito)

        $ get_ach('kaito_secret')

    return