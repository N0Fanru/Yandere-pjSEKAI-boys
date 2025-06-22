image titleim = ConditionSwitch (
    "startim == 1", "r null ",
    "startim == 2", "r horny",
    "startim == 3", "r rape",
    "startim == 4", "r no",
    "startim == 5", "r comfort",
    "True", "r null"
)

image bgtitleim = ConditionSwitch (
    "startim == 1", "bg r-null",
    "startim == 2", "bg r-horny",
    "startim == 3", "bg r-rape",
    "startim == 4", "bg r-no",
    "startim == 5", "bg r-comfort",
    "True", "bg r-null"
)

image overtitleim = ConditionSwitch (
    "startim == 1", "r-null over",
    "startim == 2", "r-horny over",
    "startim == 3", "r-rape over",
    "startim == 4", "r-no over",
    "startim == 5", "r-comfort over",
    "True", "r-null over"
)

image titleimchr = ConditionSwitch (
    "startim == 1", "r null0",
    "startim == 2", "r horny0",
    "startim == 3", "r rape0",
    "startim == 4", "nothing",
    "startim == 5", "r comfort0",
    "True", "r null0"
)

image startimglitch = ConditionSwitch(
    "startim == 5", "r glitch comfort",
    "startim == 4", "r glitch no",
    "True", "nothing"
)



image r null im1:
    "r-null-im1-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-null-im1-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r null im2:
    "r-null-im2-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-null-im2-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r null im3:
    "r-null-im3-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-null-im3-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r horny im1:
    "r-horny-im1-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-horny-im1-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r horny im2:
    "r-horny-im2-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-horny-im2-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r horny im31:
    "r-horny-im3-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-horny-im3-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r horny im32:
    "r-horny-im3-3"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-horny-im3-4"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r horny im3:
    choice(kaitoim == True):
            "r horny im31"
            pause 1.0
            glitch("r horny im31", randomkey=None)
            pause 0.05
            glitch("r horny im31", randomkey=None)
            pause 0.05
            glitch("r horny im31", randomkey=None)
            pause 0.05
            glitch("r-horny-glitch1", randomkey=None)
            pause 0.05
            glitch("r horny im31", randomkey=None)
            pause 0.05
            glitch("r horny im31", randomkey=None)
            pause 0.05
            "r horny im31"
            pause 1.2
            "r horny im32" with Dissolve(0.5)
    choice:
        "r horny im31"
        pause 2.5
        "r horny im32" with Dissolve(0.5)

image r horny im4:
    "r-horny-im4-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-horny-im4-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r rape im1:
    "r-rape-im1-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-rape-im1-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r rape im2:
    "r-rape-im2-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-rape-im2-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r rape im3:
    "r-rape-im3-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-rape-im3-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r rape im4:
    "r-rape-im4-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-rape-im4-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r comfort im1:
    "r-comfort-im1-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-comfort-im1-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r comfort im2:
    "r-comfort-im2-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-comfort-im2-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r comfort im3:
    "r-comfort-im3-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-comfort-im3-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r null:
    choice(kaitoim == True):
        "r null im1" with Dissolve(.3)
        pause 0.7
        glitch("r null im1", randomkey=None)
        pause 0.05
        glitch("r null im1", randomkey=None)
        pause 0.05
        glitch("r null im1", randomkey=None)
        pause 0.05
        glitch("r-null-glitch", randomkey=None)
        pause 0.05
        glitch("r-null-glitch", randomkey=None)
        pause 0.05
        glitch("r null im1", randomkey=None)
        pause 0.05
        glitch("r null im1", randomkey=None)
        pause 0.05
        "r null im1"
    choice:
        "r null im1" with Dissolve(.3)
    choice:
        "r null im2" with Dissolve(.3)
    pause 8.0
    choice:
        "r null im3" with Dissolve(.3)
    choice:
        "r-null-im4" with Dissolve(.3)
    pause 8.0
    repeat


image r no:
    choice(kaitoim == True):
        "r-no-im1"
        pause 1.5
        glitch("r-no-im1", randomkey=None)
        pause 0.05
        glitch("r-no-im1", randomkey=None)
        pause 0.05
        glitch("r-no-im1", randomkey=None)
        pause 0.05
        glitch("r-nothing", randomkey=None)
        pause 0.05
        glitch("r-no-im1", randomkey=None)
        pause 0.05
        glitch("r-no-im1", randomkey=None)
        pause 0.05
        glitch("r-no-im1", randomkey=None)
        pause 0.05
        "r-no-im1"
        pause 10.0
        repeat
    choice(kaitoim == False):
        "r-no-im1"

image r horny:
    choice:
        "r horny im1" with Dissolve(.3)
        pause 8.0
    choice:
        "r horny im3" with Dissolve(.3)
        pause 5.0
        "r horny im32"
        pause 3.0
    pause 0.01
    choice:
        "r horny im2" with Dissolve(.3)
    choice:
        "r horny im4" with Dissolve(.3)
    pause 8.0
    repeat

image r rape:
    choice(kaitoim == True):
        "r rape im1" with Dissolve(.3)
        pause 0.7
        glitch("r rape im1", randomkey=None)
        pause 0.05
        glitch("r rape im1", randomkey=None)
        pause 0.05
        glitch("r rape im1", randomkey=None)
        pause 0.05
        glitch("r-rape-glitch", randomkey=None)
        pause 0.05
        glitch("r-rape-glitch", randomkey=None)
        pause 0.05
        glitch("r rape im1", randomkey=None)
        pause 0.05
        glitch("r rape im1", randomkey=None)
        pause 0.05
        "r rape im1"
    choice:
        "r rape im1" with Dissolve(.3)
    choice:
        "r rape im2" with Dissolve(.3)
    choice:
        "r rape im3" with Dissolve(.3)
    choice:
        "r rape im4" with Dissolve(.3)
    pause 8.0
    choice:
        "r rape im2" with Dissolve(.3)
    choice:
        "r rape im3" with Dissolve(.3)
    choice:
        "r rape im4" with Dissolve(.3)
    pause 8.0
    repeat

image r comfort:
    "r comfort im1"
    pause 8.0
    block:
        choice(kaitoim == True):
            "r comfort im3" with Dissolve(.3)
            pause 2.6
            glitch("r comfort im3", randomkey=None)
            pause 0.05
            glitch("r comfort im3", randomkey=None)
            pause 0.05
            glitch("r-comfort-glitch", randomkey=None)
            pause 0.05
            glitch("r comfort im3", randomkey=None)
            pause 0.05
            "r comfort im3"
            pause 5.0
        choice:
            "r comfort im1" with Dissolve(.3)
            pause 8.0
        choice:
            "r comfort im2" with Dissolve(.3)
            pause 8.0
        choice:
            "r comfort im3" with Dissolve(.3)
            pause 8.0
        pause 0.01
        repeat

image r comfort3:
    "r-comfort-3-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-comfort-3-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r comfort2:
    "r-comfort-2-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-comfort-2-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r comfort1:
    "r-comfort-1-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-comfort-1-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r comfort0:
    choice:
        "r comfort3"
    choice:
        "r comfort1"
    ease 0.2 alpha 1.0
    pause 8.0
    ease 0.2 alpha 0.0
    pause 0.1
    "r comfort2"
    ease 0.2 alpha 1.0
    pause 8.0
    ease 0.2 alpha 0.0
    pause 0.1
    repeat             

image r glitch comfort:
    choice(kaitoim == True):
        "nothing"
        pause 3.0
        glitch("nothing", randomkey=None)
        pause 0.05
        glitch("nothing", randomkey=None)
        pause 0.05
        glitch("r-comfort-gltch", randomkey=None)
        pause 0.05
        glitch("nothing", randomkey=None)
        pause 0.05
        "nothing"
        pause 5.2
    choice:
        "nothing"
        pause 8.6
    "nothing"
    pause 8.6
    repeat

image r horny1:
    "r-horny-1-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-horny-1-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r horny2:
    "r-horny-2-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-horny-2-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r horny31:
    "r-horny-3-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-horny-3-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r horny32:
    "r-horny-3-3"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-horny-3-4"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r horny3:
    choice(kaitoim == True):
        "r horny31"
        pause 1.0
        glitch("r horny31", randomkey=None)
        pause 0.05
        glitch("r horny31", randomkey=None)
        pause 0.05
        glitch("r horny31", randomkey=None)
        pause 0.05
        glitch("r-horny-gltch", randomkey=None)
        pause 0.05
        glitch("r horny31", randomkey=None)
        pause 0.05
        glitch("r horny31", randomkey=None)
        pause 0.05
        "r horny31"
        pause 1.2
        "r horny32" with Dissolve(0.5)
    choice:
        "r horny31"
        pause 2.5
        "r horny32" with Dissolve(0.5)

image r horny4:
    "r-horny-4-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-horny-4-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat 

image r horny0:
    choice:
        "r horny1"
        ease 0.2 alpha 1.0
        pause 8.0
        ease 0.2 alpha 0.0
        pause 0.1
    choice:
        "r horny3"
        ease 0.2 alpha 1.0
        pause 5.0
        "r horny32"
        pause 3.0
        ease 0.2 alpha 0.0
        pause 0.1
    pause 0.01
    choice:
        "r horny2"
    choice:
        "r horny4"
    ease 0.2 alpha 1.0
    pause 8.0
    ease 0.2 alpha 0.0
    pause 0.1
    repeat

image r glitch no:
    choice(kaitoim == True):
        "nothing"
        pause 3.0
        glitch("nothing", randomkey=None)
        pause 0.05
        glitch("r-no-gltch", randomkey=None)
        pause 0.05
        glitch("r-no-gltch", randomkey=None)
        pause 0.05
        glitch("nothing", randomkey=None)
        pause 0.05
        "nothing"
        pause 5.2
    choice:
        "nothing"
        pause 8.6
    "nothing"
    pause 8.6
    repeat

image r null1:
    "r-null-1-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-null-1-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r null2:
    "r-null-2-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-null-2-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r null3:
    "r-null-3-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-null-3-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r null0:
    choice(kaitoim == True):
        "r null1"
        ease 0.2 alpha 1.0
        pause 0.7
        glitch("r null1", randomkey=None)
        pause 0.05
        glitch("r null1", randomkey=None)
        pause 0.05
        glitch("r-null-gltch", randomkey=None)
        pause 0.05
        glitch("r-null-gltch", randomkey=None)
        pause 0.05
        glitch("r null1", randomkey=None)
        pause 0.05
        glitch("r null1", randomkey=None)
        pause 0.05
        "r null1"
        pause 5.2
    choice:
        "r null2"
        ease 0.2 alpha 1.0
        pause 8.0
    choice:
        "r null1"
        ease 0.2 alpha 1.0
        pause 8.0
    ease 0.2 alpha 0.0
    pause 0.1
    choice:
        "r null3"
    choice:
        "r-null-4"
    ease 0.2 alpha 1.0
    pause 8.0
    ease 0.2 alpha 0.0
    pause 0.1
    repeat

image r rape1:
    "r-rape-1-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-rape-1-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r rape2:
    "r-rape-2-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-rape-2-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r rape3:
    "r-rape-3-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-rape-3-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r rape4:
    "r-rape-4-1"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 2.5
    "r-rape-4-2"
    choice:
        pause 0.1
    choice:
        pause 0.2
    repeat

image r rape0:
    choice:
        "r rape2"
        ease 0.2 alpha 1.0
        pause 8.0
    choice(kaitoim == True):
        "r rape1"
        ease 0.2 alpha 1.0
        pause 0.7
        glitch("r rape1", randomkey=None)
        pause 0.05
        glitch("r rape1", randomkey=None)
        pause 0.05
        glitch("r-rape-gltch", randomkey=None)
        pause 0.05
        glitch("r-rape-gltch", randomkey=None)
        pause 0.05
        glitch("r rape1", randomkey=None)
        pause 0.05
        glitch("r rape1", randomkey=None)
        pause 0.05
        "r rape1"
        pause 5.2
    choice:
        "r rape1"
        ease 0.2 alpha 1.0
        pause 8.0
    ease 0.2 alpha 0.0
    pause 0.1
    choice:
        "r rape3"
    choice:
        "r rape4"
    ease 0.2 alpha 1.0
    pause 8.0
    ease 0.2 alpha 0.0
    pause 0.1
    repeat

