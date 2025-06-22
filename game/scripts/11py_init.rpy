init python:

    renpy.add_layer('forever', above='overlay', menu_clear=False)

    import time

    # поиск в матрице
    def contains_element(matrix, element):
        return any(element in row for row in matrix)

    def noti_more_or_not():
        if contains_element(persistent.rui_end, True) or contains_element(persistent.secret_end, True):
            persistent.morenoti = True
        else:
            persistent.morenoti = False

    import random
    persistent.last_check = _preferences.get_volume("sfx")
    def play_sound_check():
        if persistent.last_check != _preferences.get_volume("sfx"):
            persistent.last_check = _preferences.get_volume("sfx")
            random_sound = random.randint(1, 5)
            if random_sound == 1:
                renpy.sound.play("audio/test/test1.ogg", "sound")
            elif random_sound == 3:
                renpy.sound.play("audio/test/test3.ogg", "sound")
            elif random_sound == 4:
                renpy.sound.play("audio/test/test4.ogg", "sound")
            elif random_sound == 5:
                renpy.sound.play("audio/test/test5.ogg", "sound")
            else:
                renpy.sound.play("audio/test/test2.ogg", "sound")


    




    # стек для хранения состояния экранов до вызова call
    screens = []
    # действие по кнопке ESC
    gamemenu = config.game_menu_action
    # добавить очередной список экранов
    def s_push(item):
        global screens
        screens.append(item)
    # извлечь последний список экранов
    def s_pop():
        global screens
        if len(screens) > 0:
            return screens.pop()
        return []
    is_call = False
    # из экрана нельзя выполнить обычный call label
    # создадим его аналог
    class MyCall(Action):
        def __init__(self, label, *args, **kwargs):
            self.label = label
            self.args = args
            self.kwargs = kwargs
        def __call__(self):
            global screens, is_call
            # отключаем ESC
            config.game_menu_action = NullAction()
            # запоминаем экраны
            s_push(renpy.current_screen().screen_name)
            # включаем флаг вызова нового контекста (чтобы спрятать кнопку)
            is_call = True
            # вызываем локацию в новом контексте
            renpy.call_in_new_context(self.label, *self.args, **self.kwargs)
    # функция для восстановления экранов в новом контексте
    def show_screens():
        for i in screens[-1:]:
            renpy.show_screen(i)
    # функция для возвращениея из локации в новом контексте
    def myreturn():
        global is_call
        # спрятать экраны
        for i in s_pop():
            renpy.hide_screen(i)
        # снять флаг новой локации, чтобы кнопка ее вызова снова появилась
        is_call = len(screens) > 0
        if not is_call:
            config.game_menu_action = gamemenu
        # сохранение данных игры
        renpy.retain_after_load()
        Return()()
    # чтобы можно было привязать к копке, например
    MyReturn = renpy.curry(myreturn)


    config.keymap['hide_windows'].remove('noshift_K_h')
    config.keymap['hide_windows'].remove('mouseup_2')
    config.keymap['game_menu'].remove('K_ESCAPE')
    config.keymap['game_menu'].remove('K_MENU')
    config.keymap['game_menu'].remove('K_PAUSE')
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['help'].remove('K_F1')
    config.keymap['help'].remove('meta_shift_/')