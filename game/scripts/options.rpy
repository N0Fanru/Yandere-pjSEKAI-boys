## Данный файл содержит настройки, способные изменить вашу игру.
##
## Строки, начинающиеся  с двух '#' — комментарии, и вы не должны их
## раскомментировать. Строки, начинающиеся с одной '#' — комментированный код,
## который вы можете раскомментировать, если посчитаете это нужным.

default persistent.text_value_set = False

init python:

    renpy.music.register_channel("ui", loop=False, mixer="sfx")
    renpy.music.register_channel("sound2", loop=False, mixer="sfx")
    renpy.music.register_channel("text", loop=True, mixer="text")

    if not persistent.text_value_set:
        persistent.text_value_set = True
        preferences.set_volume("text", 0.7)

## Основное ####################################################################

## Читаемое название игры. Используется при установке стандартного заголовка
## окна, показывается в интерфейсе и отчётах об ошибках.
##
## Символы "_()", окружающие название, отмечают его как пригодное для перевода.

define config.name = "Yandere pjSEKAI boys"

default preferences.fullscreen = True
default preferences.audio_when_minimized = False
define config.default_music_volume = 0.7
define config.default_sfx_volume = 1.0
define config.default_voice_volume = 0.2
define config.menu_include_disabled = True
define config.end_splash_transition = Dissolve(.3)
define config.enter_yesno_transition = Dissolve(.2)
define config.game_main_transition = Dissolve(.2)

# default preferences.emphasize_audio = True
# define config.emphasize_audio_channels = ['sound']
# define config.emphasize_audio_volume = 0.7

define config.context_fadein_music = 0.5
define config.context_fadeout_music = 0.5

define config.debug_prediction = True
define config.main_menu_music_fadein = 0.5
define config.minimum_presplash_time = 3.0
define config.choice_empty_window = extend

define config.gl2 = True

# define config.enable_language_autodetect = True

define config.always_shown_screens = ['scrover'] if not persistent.debugmode else ['scrover', 'debugscreen']

## Определяет, показывать ли заголовок, данный выше, на экране главного меню.
## Установите на False, чтобы спрятать заголовок.

define gui.show_name = True


## Версия игры.

define config.version = "1.0.1"

define config.developer = True if dmt == 2 else False
define config.rollback_enabled = True if dmt == 2 else False


## Текст, помещённый в экран "Об игре". Поместите текст между тройными скобками.
## Для отделения абзацев оставляйте между ними пустую строку.

define gui.about = ""


## Короткое название игры, используемое для исполняемых файлов и директорий при
## постройке дистрибутивов. Оно должно содержать текст формата ASCII и не должно
## содержать пробелы, двоеточия и точки с запятой.

define build.name = "yanderesekai"


## Звуки и музыка ##############################################################

## Эти три переменные управляют, среди прочего, тем, какие микшеры показываются
## игроку по умолчанию. Установка одной из них в False скроет соответствующий
## микшер.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## Чтобы разрешить игроку тестировать громкость на звуковом или голосовом
## каналах, раскомментируйте строчку и настройте пример звука для прослушивания.

define config.sample_sound = "audio/test.ogg"


## Раскомментируйте следующую строчку, чтобы настроить аудиофайл, который будет
## проигрываться в главном меню. Этот файл продолжит проигрываться во время
## игры, если не будет остановлен, или не начнёт проигрываться другой аудиофайл.

define config.main_menu_music = "music/main.ogg"


## Переходы ####################################################################
##
## Эти переменные задают переходы, используемые в различных событиях. Каждая
## переменная должна задавать переход или None, чтобы указать на то, что переход
## не должен использоваться.

## Вход и выход в игровое меню.

define config.enter_transition = Dissolve(.3)
define config.exit_transition = Dissolve(.3)


## Переход между экранами игрового меню.

define config.intra_transition = Dissolve(.15)


## Переход, используемый после загрузки слота сохранения.

define config.after_load_transition = dissolve


## Используется при входе в главное меню после того, как игра закончится.

define config.end_game_transition = Dissolve(.2)


## Переменная, устанавливающая переход, когда старт игры не существует. Вместо
## неё используйте функцию with после показа начальной сценки.


## Управление окнами ###########################################################
##
## Эта строка контролирует, когда появляется диалоговое окно. Если "show" — оно
## всегда показано. Если "hide" — оно показывается, только когда представлен
## диалог. Если "auto" — окно скрыто до появления оператора scene и показывается
## при появлении диалога.
##
## После начала игры этот параметр можно изменить с помощью "window show",
## "window hide" и "window auto".

define config.window = "auto"


## Переходы, используемые при показе и скрытии диалогового окна

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Стандартные настройки #######################################################

## Контролирует стандартную скорость текста. По умолчанию, это 0 — мгновенно,
## в то время как любая другая цифра — это количество символов, печатаемых в
## секунду.

default preferences.text_cps = 30


## Стандартная задержка авточтения. Большие значения означают долгие ожидания, а
## от 0 до 30 — вполне допустимый диапазон.

default preferences.afm_time = 15


## Директория сохранений #######################################################
##
## Контролирует зависимое от платформы место, куда Ren'Py будет складывать файлы
## сохранения этой игры. Файлы сохранений будут храниться в:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## Этот параметр обычно не должен изменяться, а если и изменился, должен быть
## текстовой строчкой, а не выражением.

define config.save_directory = "yandere_sekai"


## Иконка ######################################################################
##
## Иконка, показываемая на панели задач или на dock.

define config.window_icon = "gui/window_icon.png"


## Настройка Дистрибутива ######################################################
##
## Эта секция контролирует, как Ren'Py строит дистрибутивные файлы из вашего
## проекта.

init python:

    ## Следующие функции берут образцы файлов. Образцы файлов не учитывают
    ## регистр и соответствующе зависят от директории проекта (base), с или без
    ## учёта /, задающей директорию. Если обнаруживается множество одноимённых
    ## файлов, то используется только первый.
    ##
    ## Инструкция:
    ##
    ## / — разделитель директорий.
    ##
    ## * включает в себя все символы, исключая разделитель директорий.
    ##
    ## ** включает в себя все символы, включая разделитель директорий.
    ##
    ## Например, "*.txt" берёт все файлы формата txt из директории base, "game/
    ## **.ogg" берёт все файлы ogg из директории game и всех поддиректорий, а
    ## "**.psd" берёт все файлы psd из любого места проекта.

    ## Классифицируйте файлы как None, чтобы исключить их из дистрибутивов.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## Чтобы архивировать файлы, классифицируйте их, например, как 'archive'.

    build.classify('game/**.png', 'archive')
    build.classify('game/**.webp', 'archive')
    build.classify('game/**.webm', 'archive')
    build.classify('game/**.avif', 'archive')
    build.classify('game/**.ttf', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.rpy', 'archive')
    build.classify('game/**.ogv', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.wav', 'archive')
    build.classify('game/**.flac', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.opus', 'archive')
    build.classify('game/**.py', 'archive')
    build.classify('game/**.rpyc', 'archive')
    build.classify('game/**.rpy', 'archive')

    ## Файлы, соответствующие образцам документации, дублируются в приложениях
    ## Mac, чтобы они появлялись и в приложении, и в zip архиве.

    build.documentation('*.html')
    build.documentation('*.txt')


## Лицензионный ключ Google Play требуется для загрузки файлов расширений и
## поддержки внутриигровых покупок. Он может быть найден на странице "Services &
## APIs" консоли разработчика Google Play.

# define build.google_play_key = "..."


## Имя пользователя и название проекта, ассоциированные с проектом на itch.io,
## разделённые дробью.

# define build.itch_project = "renpytom/test-project"
