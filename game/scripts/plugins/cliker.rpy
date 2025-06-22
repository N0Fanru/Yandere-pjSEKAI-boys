init python:
    class SleepCliker(renpy.Displayable):

        def __init__(self):
            super(SleepCliker, self).__init__()

        def render(self, width, height, st, at):
            global sleep_clik
            render = renpy.Render(width, height)
            alpha = [1-(sleep_clik*4 / 100), 1-(sleep_clik*2.5 / 100), 1-(sleep_clik*1.5 / 100), 1-(sleep_clik / 100), 1-(sleep_clik*0.5 / 100)]
            images = ['eye-close-true', 'eye-close', 'eye-half', 'eye-open', 'eye-open-true']
            for i in range(0, 5):
                im = renpy.displayable(images[i])
                if alpha[i] > 0:
                    image = Transform(im, alpha=alpha[i])
                else:
                    image = Transform(im, alpha=0)
                r = renpy.render(image, width, height, st, at)
                render.blit(r, (0, 0))
            renpy.redraw(self, 0)
            return render
            

screen cliker():
    modal True
    add SleepCliker()
    timer 0.03 repeat True action If(sleep_clik>0, If(sleep_clik<100, SetVariable('sleep_clik', sleep_clik-1), Jump('no_sleep_on_tv')), Jump('sleep_on_tv'))

    button:
        xfill True
        yfill True
        action SetVariable('sleep_clik', sleep_clik+10)

    on "show" action Function(renpy.hide, 'eye-open-true')