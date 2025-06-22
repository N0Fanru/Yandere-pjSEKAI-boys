################################################################################
##### made by N0Fanru 
################################################################################

# Основной код "Дурака" на ренпай, полностью сделано N0Fanru
# Экраны хронятся в файле durak/screens.rpy, чтобы их легче можно кастомизировать
# Для настроек (изменения фраз и прочего) используйте файл durak/settings.rpy
# Для начала игры используйте call durak_game,
# после завершения игры вернётся переменная who_win_ с знчаением 0 (противник выиграл), 1 (ничья) или 2 (игрок выиграл)

# У меня не так много опыта в создании подобного рода кода, старалась оставлять комментарии и называть все переменные, функции и классы по правилам
# Код создавался с большимы промежутками времяни и изночально планировалось возможность жульчинать, поэтому местами код выглядит странно и сильно запутан и услажнён
# Но всё же надеюсь, данный код не вышел сильно костыльным

python early hide:

    # варпер для анимации карт, собирающихся в бито
    @renpy.atl_warper
    def beat_card_warper(t):
        if t < 0.5:
            t *= 2
            return 0.5 * t * t * t
        t = 2*t - 2
        if t > 0.8:
            t *= 2
        return 0.5 * (t * t * t + 2)
    

init offset = -12

init python:
    import copy as copy1
    import pygame

    ################################################################################
    ## Классы 
    ################################################################################

    # Класс для одной карты
    class DurakCard():

        def __init__(self, suit, value): # карта состоит из масти, достоинства и порядкового номера, если карта находится в наборе
            global trump_
            self.suit = suit
            self.value = value
            self.number = None
            # также в объекте хранится информация является ли карта козырём
            if suit == trump_:
                self.trump = True
            else:
                self.trump = False

        def name(self): # возвращает имя карты и True/False (козырь/нет)
            return self.suit + str(self.value) + str(self.trump) + str(self.number)

        def image(self): # возвращает имя изображения для карты
            return self.suit + str(self.value)

        def suit_name(self): # возвращает имя масти
            return suits_name_[self.suit]

        def value_name(self): # возвращает имя наминала карты
            return value_name_[str(self.value)]

        def new_number(self, n): # меняет порядковый номер
            self.number = n
    

    # Класс набора карт у игроков
    class SetCards():

        def __init__(self): # так как карты добираются из колоды, по умолчанию в объекте из атрибутов только пустой список
            self.cards = []

        def qt(self):
            return len(self.cards)

        def names(self): # возвращает имена карт
            return [x.name() for x in self.cards]

        def set(self, start=0, end=None): # возвращает список карт в диапазоне start-end
            return self.cards[start:end]

        def trumps_value(self): # возвращает список наминала козырных карт
            return [card.value for card in self.cards if card.trump]
                    
        def lesser_trump(self): # возвращает меньший козырь
            trumps = [card for card in self.cards if card.trump]
            return min(trumps, key=lambda card: card.value) if trumps else None

        def more_that(self, value): # возвращает количество карт, которые больше value
            return sum(1 for c in self.cards if c.value > value)

        def sort_cards(self): # сортирует карты от меньшего к большиму, в конце распологая козыри
            self.cards.sort(key=lambda card: (card.trump, card.value))

        def set_numbers(self): # устанавливает порядковый номер карты
            for n in range(0, len(self.cards)):
                self.cards[n].number = n+1

        def add_cards(self, cards): # добавляет карты в набор
            self.cards += cards
            self.sort_cards()
            self.set_numbers()

        def remove_card(self, card): # удаляет карту из набора
            self.cards.remove(card)
            self.set_numbers()

        def add_cards_from_dec(self, qt): # берёт карты из колоды
            global card_deck_
            self.add_cards(card_deck_[:qt])
            del card_deck_[0:qt]


    
    # Класс игрвого поле
    class PlayingField():

        def __init__(self): 
            self.cards_attack = [] # карты в атаке
            self.cards_attack_from = [] # от кого карты в атаке (True - от игрока, False - от протвиника)
            self.number_cards_attack = 0 # количсетво карт в атаке
            self.cards_beat = [] # карты которыми бьются
            self.cards_beat_from = [] # от кого карты в картах, которыми бьются (True - от игрока, False - от протвиника)
            self.number_beat_attack = 0 # количество побитых карт
            self.value = [] # список достоинств карт, которые есть на поле
            self.state = 'normal'

        def reset(self): 
            self.cards_attack = [] 
            self.cards_attack_from = [] 
            self.number_cards_attack = 0 
            self.cards_beat = [] 
            self.cards_beat_from = [] 
            self.number_beat_attack = 0 
            self.value = [] 
            self.state = 'normal'

        def im(self, n): # возвращает картинку карты по её порядковвому номеру
            return self.cards_attack[n].image()

        def im_beat(self, n): # возвращает картинку карты по её порядковвому номеру
            return self.cards_beat[n].image()

        # функция, вызывемая при бито
        def beat_durak(self, last, next):
            global durak_step, discard_pile, npc_cards_
            durak_step = 'wait'
            renpy.show_screen('durak_noti', durak_noti_name['beat'])
            self.state = 'beat'
            renpy.music.play(["<silence .13>", audio.slide_], channel='audio', loop=False, relative_volume=sound_card_valume)
            new_beat = self.cards_attack + self.cards_beat
            discard_pile += new_beat
            renpy.show_screen('reset_field', t=1.3, last=last, next=next)

        # игрок взял 
        def player_take(self):
            global durak_step, select_card_
            durak_step = 'wait'
            renpy.show_screen('durak_noti', durak_noti_name['player_take'])
            self.state = 'take'
            cards = self.cards_attack + [i for i in self.cards_beat if i is not None]
            renpy.music.play(["<silence .08>", audio.slide_], channel='audio', loop=False, relative_volume=sound_card_valume)
            renpy.show_screen('change_player_cards', act='take', card=cards, t=0.5)
            renpy.music.play(["<silence .33>", audio.take_], channel='audio', loop=False, relative_volume=sound_card_valume)
            renpy.show_screen('reset_field', t=1.1, last='n', next='npc', who_cant='p')
            select_card_ = None

        def player_beat(self, card, n): # игрок бьётся
            global durak_step, hide_player_card, player_cards_
            renpy.music.play(audio.take_, channel='audio', loop=False, relative_volume=sound_card_valume)
            hide_player_card = card
            self.cards_beat[n] = card
            self.cards_beat_from[n] = True
            self.number_beat_attack += 1
            if card.value not in self.value:
                self.value.append(card.value)
            renpy.music.play(["<silence .2>", audio.slide_], channel='audio', loop=False, relative_volume=sound_card_valume)
            if None in self.cards_beat:
                end = NullAction()
            else:
                durak_step = 'npc_throw'
                npc_emotion_.change('thinks')
                end = Show('npc_toss_t') #Function(playing_field_.npc_toss) #Function(playing_field_.beat_durak, 'n', 'player')
            renpy.show_screen('change_player_cards', 'beat', card, 0.1, end)

        def add_card_attack(self, card, from_): # дабовляет карты на поле в атаку
            self.number_cards_attack += 1
            card.new_number(self.number_cards_attack)
            if card.value not in self.value:
                self.value.append(card.value)
            self.cards_attack.append(card)
            self.cards_beat.append(None)
            self.cards_beat_from.append(None)
            self.cards_attack_from.append(from_)

        def player_translation(self, card): # игрок переводит
            global hide_player_card, durak_step, npc_emotion_
            renpy.show_screen('durak_noti', durak_noti_name['translation'])
            self.add_card_attack(card, True)
            hide_player_card = card
            renpy.music.play(["<silence .2>", audio.slide_], channel='audio', loop=False, relative_volume=sound_card_valume)
            renpy.show_screen('change_player_cards', 'trans', card)
            durak_step = 'npc_beats'
            npc_emotion_.change('thinks')

        def player_attack(self, card, scam): # игрок атакует
            global hide_player_card, durak_step, npc_emotion_
            renpy.music.play(audio.take_, channel='audio', loop=False, relative_volume=sound_card_valume)
            self.add_card_attack(card, True)
            if not renpy.get_screen('card_in_attack'):
                renpy.show_screen('card_in_attack')
            hide_player_card = card
            renpy.music.play(["<silence .2>", audio.slide_], channel='audio', loop=False, relative_volume=sound_card_valume)
            renpy.show_screen('change_player_cards', 'attack', card)
            durak_step = 'npc_beats'
            npc_emotion_.change('thinks')

        def npc_attack(self): # противник атакует
            global npc_cards_, durak_step, player_cards_

            # поиск карт с одинаковым наминалом
            set_cards = []
            l = [c.value for c in npc_cards_.cards]
            s = {}
            for c in set(l):
                if l.count(c) > 1:
                    s[c] = l.count(c)
            while s != {}:
                qt = max(s.values())
                card = list(s.keys())[list(s.values()).index(qt)]
                if self.condition_more_attack(card, qt):
                    set_cards = [c for c in npc_cards_.cards if c.value == card]
                    break
                else:
                    del s[card]

            if set_cards != []:
                for c in set_cards:
                    self.cards_attack.append(c)
                    self.cards_attack_from.append(False)
                    if c.value not in self.value:
                        self.value.append(c.value)
                    self.cards_beat.append(None)
                    self.cards_beat_from.append(None)
                    npc_cards_.remove_card(c)
                    self.number_cards_attack += 1
                    npc_emotion_.change('happy')
            else:
                min_card = npc_cards_.cards[0] # минимальная карта у противника
                self.cards_attack.append(min_card)
                self.cards_attack_from.append(False)
                self.value.append(min_card.value)
                self.cards_beat.append(None)
                self.cards_beat_from.append(None)
                npc_cards_.remove_card(min_card)
                self.number_cards_attack += 1
                npc_emotion_.change('normal')
            renpy.music.play(["<silence .17>", audio.slide_], channel='audio', loop=False, relative_volume=sound_card_valume)
            durak_step = 'player_beat'
                

        def condition_more_attack(self, card, qt): # условия, когда противник кидает несколько карт за раз
            global card_deck_, npc_cards_

            if len(card_deck_) != 0:
                for deck_len, (more, add, more_add) in sorted(condition_more_attack1.items(), reverse=True):
                    if len(card_deck_) > deck_len:
                        if card < more or (qt >= add and card < more_add):
                            return True
                        else:
                            return False
            else:
                for npc_len, (more, add, more_add) in sorted(condition_more_attack2.items(), reverse=True):
                    if len(npc_cards_.cards) > npc_len:
                        if card < more or (qt >= add and card < more_add):
                            return True
                        else:
                            return False

        def npc_toss(self): # противник подрбрасывает карты
            global npc_cards_, player_cards_, card_deck_, durak_step

            card = None

            for c in npc_cards_.cards:
                if c.value in self.value and len(playing_field_.cards_attack)+1 <= 6 and player_cards_.qt() >= 1:
                    if len(card_deck_) != 0:
                        for deck_len, (ntrump, trump) in sorted(condition_pass1.items(), reverse=True):
                            if len(card_deck_) > deck_len:
                                if (not c.trump and c.value < ntrump) or (c.trump and c.value < trump):
                                    card = c
                                    break
                    else:
                        for npc_len, (ntrump, trump) in sorted(condition_pass2.items(), reverse=True):
                            if npc_cards_.qt() > npc_len:
                                if (not c.trump and c.value < ntrump) or (c.trump and c.value < trump):
                                    card = c
                                    break
                if card is not None:
                    self.cards_attack.append(card)
                    self.cards_attack_from.append(False)
                    self.value.append(card.value)
                    self.cards_beat.append(None)
                    self.cards_beat_from.append(None)
                    npc_cards_.remove_card(card)
                    self.number_cards_attack += 1
                    npc_emotion_.change('normal')
                    renpy.music.play(["<silence .17>", audio.slide_], channel='audio', loop=False, relative_volume=sound_card_valume)
                    durak_step = 'player_beat'
                    npc_emotion_.change('happy')
                    break
            if card is None:
                npc_emotion_.change('normal')
                self.beat_durak('n', 'player')
                

        def npc_beats_more(self): # противник бьётся, когда ему перевёл игрок
            global npc_cards_, durak_step, player_cards_
            for c in npc_cards_.cards:
                if player_cards_.qt() >= len(self.cards_attack)+1 <= 6 and self.condition_transfer(c, list(set(self.value))[0], True):
                    # сначала противник попытается перевести
                    self.cards_attack.append(c)
                    self.cards_attack_from.append(False)
                    self.cards_beat.append(None)
                    self.cards_beat_from.append(None)
                    npc_cards_.remove_card(c)
                    self.number_cards_attack += 1
                    renpy.music.play(["<silence .17>", audio.slide_], channel='audio', loop=False, relative_volume=sound_card_valume)
                    npc_emotion_.change('happy')
                    renpy.show_screen('durak_noti', durak_noti_name['translation'])
                    durak_step = 'player_beat'
                    return
            attack = copy1.deepcopy(self.cards_attack)
            beaten = [None] * len(self.cards_attack)
            for c in npc_cards_.cards:
                for card in attack:
                    if card is not None and self.condition_beat(c, card):
                        i = attack.index(card)
                        beaten[i] = c
                        attack[i] = None
                        break
            if not (None in beaten):
                for c in beaten:
                    n = self.cards_beat.index(None)
                    self.cards_beat[n] = c
                    self.cards_beat_from[n] = False
                    npc_cards_.remove_card(c)
                    self.value.append(c.value)
                    self.number_beat_attack += 1
                    renpy.music.play(["<silence .17>", audio.slide_], channel='audio', loop=False, relative_volume=sound_card_valume)
                npc_emotion_.change('happy')
                durak_step = 'player_throw'
            else:
                # берёт
                self.state = 'npc_take'
                renpy.music.play(audio.slide_, channel='audio', loop=False, relative_volume=sound_card_valume)
                renpy.show_screen('reset_field', t=1, who_cant = 'n')
                renpy.show_screen('durak_noti', durak_noti_name['npc_take'])
                npc_emotion_.change('sad')
                npc_cards_.add_cards(self.cards_attack+[i for i in self.cards_beat if i is not None])
                durak_step = 'wait'

        def npc_beats(self, card): # противник бьёт карту игрока
            global npc_cards_, durak_step, player_cards_
            beat = False
            if npc_cards_.qt() < 4 and len(self.cards_beat) == 0 and player_cards_.qt() >= len(self.cards_attack)+1 <= 6:
                for c in npc_cards_.cards:
                    if card.value == c.value:
                        beat = True
                        break
            for c in npc_cards_.cards:
                # перебирает все карты
                if beat or (self.number_beat_attack == 0 and player_cards_.qt() >= len(self.cards_attack)+1 <= 6 and self.condition_transfer(c, card.value, False)):
                    # если можно переводить, то противник попытается это сделать
                    beat = True
                    self.cards_attack.append(c)
                    self.cards_attack_from.append(False)
                    self.cards_beat.append(None)
                    self.cards_beat_from.append(None)
                    npc_cards_.remove_card(c)
                    self.number_cards_attack += 1
                    renpy.music.play(["<silence .17>", audio.slide_], channel='audio', loop=False, relative_volume=sound_card_valume)
                    npc_emotion_.change('happy')
                    renpy.show_screen('durak_noti', durak_noti_name['translation'])
                    durak_step = 'player_beat'
                    break
                elif self.condition_beat(c, card):
                    # бьёт карту
                    beat = True
                    n = self.cards_beat.index(None)
                    self.cards_beat[n] = c
                    self.cards_beat_from[n] = False
                    npc_cards_.remove_card(c)
                    self.value.append(c.value)
                    self.number_beat_attack += 1
                    renpy.music.play(["<silence .17>", audio.slide_], channel='audio', loop=False, relative_volume=sound_card_valume)
                    npc_emotion_.change('happy')
                    durak_step = 'player_throw'
                    break
            if not beat:
                # берёт
                self.state = 'npc_take'
                renpy.music.play(audio.slide_, channel='audio', loop=False, relative_volume=sound_card_valume)
                renpy.show_screen('reset_field', t=1, who_cant = 'n')
                renpy.show_screen('durak_noti', durak_noti_name['npc_take'])
                npc_emotion_.change('sad')
                npc_cards_.add_cards(self.cards_attack+[i for i in self.cards_beat if i is not None])
                durak_step = 'wait'

        def condition_beat(self, c, a): # условия когда противник бьёт карту
            global card_deck_, player_cards_, npc_cards_
            if ((c.value > a.value and c.suit == a.suit) or (c.trump and not a.trump)): # первичное условие битья карты
                # Противник будет бить карты "с умом", чтобы не потратить большие карты в начале игры

                if len(card_deck_) != 0: # алгаритм побьёт ли противник, если в колоде ещё есть карты
                    for deck_len, (a_take, c_non_trump, c_trump, qt, c_non_trump_more, c_trump_more) in sorted(npc_condition_beat1.items(), reverse=True):
                        # перебираются все варианты длины колоды карт из npc_condition_beat1 (в settings.rpy), пока не найдётся подходящее
                        if len(card_deck_) > deck_len:
                            if a.trump and a.value > a_take:
                                # если игрок кинул достаточно большой козырь, то противник возьмёт
                                return False
                            elif (not c.trump and c.value < c_non_trump) or (c.trump and c.value < c_trump) or (npc_cards_.qt() > qt and ((not c.trump and c.value < c_non_trump_more) or (c.trump and c.value < c_trump_more))):
                                # условия когда противник может побить карты
                                return True
                            else:
                                # не может побить и берёт
                                return False
                            break # прерывает цикл

                else: # алгаритм побьёт ли противник, если в колоде нет карт
                    if npc_cards_.qt() < 3: # если у противника одна или две карта и он может ей побить, он побьёт
                        return True
                    elif npc_cards_.qt() <= 6:
                        # если карт меньше или 6 перебираются все варианты количсетва карт у противника из npc_condition_beat2 (в settings.rpy), пока не найдётся подходящее
                        for qt_npc, (take, value, more_that, qt_player) in sorted(npc_condition_beat2.items(), reverse=True):
                            if npc_cards_.qt() <= qt_npc:
                                if a.trump and a.value > take:
                                    # если игрок кинул достаточно большой козырь, то противник возьмёт
                                    return False
                                elif (not c.trump and (c.value < value or npc_cards_.trumps_value() != [])) or (c.value < value and (len(npc_cards_.trumps_value()) > 1 or npc_cards_.more_that(11) > more_that)) or player_cards_.qt() < qt_player:
                                    # условия когда противник может побить карты
                                    return True
                                else:
                                    # не может побить и берёт
                                    return False
                                break # прерывает цикл
                    else: # у противника карт больше 6
                        if a.trump and a.value > 11:
                            # если игрок кинул достаточно большой козырь, то противник возьмёт
                            return False
                        elif (not c.trump and c.value < 13) or (c.value < 12 and len(npc_cards_.trumps_value()) > 1) or (player_cards_.qt() < 5 and c.value < 14):
                            # условия когда противник может побить карты
                            return True
                        else:
                            # не может побить и берёт
                            return False
            
            else:
                return False # карта не может побить

        def condition_transfer(self, card, value, softer): # условия когда противник переведёт
            global card_deck_, npc_cards_

            if card.value == value:
                # карта подходит чтобы перевести

                if len(card_deck_) != 0: # алгоритм, когда в колоде есть карты
                    cond = 0 if not softer else 6
                    for deck_len, (v_no_trump, v_trump) in sorted(npc_condition_transfer1.items(), reverse=True):
                        if len(card_deck_)-cond > deck_len:
                            if (not card.trump and card.value < v_no_trump) or (card.trump and card.value < v_trump):
                                return True
                            else:
                                return False
                            break

                else: # алгоритм, когда в колоде нет карт
                    cond = 0 if not softer else 2
                    for npc_len, (v_no_trump, v_trump) in sorted(npc_condition_transfer2.items(), reverse=True):
                        if npc_cards_.qt()+cond > npc_len:
                            if (not card.trump and card.value < v_no_trump) or (card.trump and card.value < v_trump):
                                return True
                            else:
                                return False
                            break




    # Класс для эмоции персонажа
    class NPCEmotion():

        def __init__(self, emotion): # единственный атрибут это эмоция (normal, happy, sad)
            self.emotion = emotion
        
        def name(self): # возвращает имя эмоции, как указано в character_emotions_
            return character_emotions_[self.emotion]

        def image(self): # возвращает соответствующее эмоции изображение персонажа
            return character_image_[self.emotion]

        def reset(self):
            self.emotion = 'normal'

        def change(self, emotion): # меняет эмоцию
            global durak_phrase_show, durak_phrases, durak_phrase_chance
            if renpy.get_screen('reset_emotion_npc'):
                renpy.hide_screen('reset_emotion_npc')
            if emotion != 'normal':
                if emotion != 'thinks':
                    renpy.show_screen('reset_emotion_npc')
                if durak_phrase_show and durak_phrase_chance >= renpy.random.random() and durak_phrase_chance != 0:
                    text = renpy.random.choice(durak_phrases[emotion])
                    renpy.show_screen('durak_phrase_', text)
                    renpy.show_screen('durak_phrase_hide')
            self.emotion = emotion



    # Родительский класс для фраз
    class Phrase():

        def __init__(self, text=None, image=None):
            self.text = text
            self.image = image

    # Класс фраз для особых событий
    class NPCPhraseSpecial(Phrase):

        def __init__(self, can, text=None, image=None):
            super().__init__(text, image)
            self.can = can

        def show(self, act=None, extra=None):
            global npc_trump_
            if self.can:
                if '|num|' in self.text:
                    # если эта начальная фраза
                    if npc_cards_.lesser_trump() is not None:
                        text = self.text.replace('|num|', str(npc_cards_.lesser_trump().value_name())) # |num| заменяется названием наминала козыря
                        npc_trump_ = npc_cards_.lesser_trump().value
                        image = self.image
                    else:
                        npc_trump_ = None
                        text = no_npc_trump_phrase.text
                        image = no_npc_trump_phrase.image
                else:
                    text = self.text
                    image = self.image
                renpy.hide('durak_character_image')
                renpy.show_screen('phrase_modal', text, image, act, extra)
                renpy.play(["<silence .05>", audio.woosh])



    # Класс для выдачи карт
    # Является отображемым объектом для использования ивентов pygame
    class TakesCards(renpy.Displayable):

        def __init__(self):
            super(TakesCards, self).__init__()

        def render(self, *args):
            return renpy.Render(0, 0)

        def event(self, ev, x, y, st):
            global cards_taken, starting_cards, who_gets_
            if ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                # при отпускании экран убирается, карты прибавляются
                if who_gets_ is not None:
                    starting_cards[who_gets_] += 1
                    renpy.show_screen('takes_cards_plus', who=who_gets_, how=cards_taken)
                cards_taken = 1



    
    ################################################################################
    ## Функции
    ################################################################################


    def strict_eq(obj1, obj2): # вспомогательная функция, "строгое равенство"
        if type(obj1) != type(obj2):
            return False
        return obj1 == obj2


    # Функция, вызываяемая в начале игры
    def start_durak():

        # тут впервые определяются переменные, чтобы с каждой игрой они сбрасывались, нижнее подчёркивание в конце нужно лишь для избежания случайных конфликтов
        global durak_step, playing_field_, select_card_, hide_player_card, trump_, card_deck_, player_cards_, npc_cards_, npc_emotion_, npc_trump_, cards_taken, starting_cards, who_gets_, discard_pile, last_step, move_num, who_win_
        trump_ = '' # название козыря
        card_deck_ = [] # колода карт
        discard_pile = [] # битые карты
        playing_field_ = PlayingField() # игровое поле
        player_cards_ = SetCards() # набор карт у игрока
        npc_cards_ = SetCards() # набор карт у противника
        npc_emotion_ = NPCEmotion(character_emotions_default) # эмоция противника
        npc_trump_ = 0 # козырь, который назывёт противник
        starting_cards = [0, 0] # количество стартовых карт (используется, если карты раздаёт игрок)
        cards_taken = 1 # взято карт для выдочи (используется, если карты раздаёт игрок)
        who_gets_ = 0 # кому дают карты сейчас 0 - противник, 1 - игрок (используется, если карты раздаёт игрок)
        select_card_ = None # карта, которая выбрана игроком в данный момент
        hide_player_card = None # карта для скрытия (используется для анимации)
        durak_step = 'wait' # ход игры
        last_step = 'wait' # последний ход
        move_num = 0 # номер хода


        trump_ = renpy.random.choice(['hearts', 'diamonds', 'spades', 'clubs']) # выбирается случайная козырная масть
        last_trump = renpy.random.randint(6, 14) # определяется достоинство нижнего козыря
        # создаётся колода карт без нижнего козыря
        for i in ['hearts', 'diamonds', 'spades', 'clubs']:
            for j in range(6, 15):
                if not (i == trump_ and j == last_trump):
                    card_deck_.append(DurakCard(i, j))
        renpy.random.shuffle(card_deck_) # колода перемешивается
        card_deck_.append(DurakCard(trump_, last_trump)) # в конец колоды добавляется нижний козырь

        # раздаётся по 6 карт игроку и сопернику
        player_cards_.add_cards_from_dec(6)
        npc_cards_.add_cards_from_dec(6)


    # Определяет фразу и чей ход в зависимоти от того, что ответил игрок при вопросе про козыри
    def trump_phrase(n=90):
        global durak_step, who_step_, npc_trump_, player_cards_
        if n == 0:
            act='hide'
            if npc_trump_ is None:
                if who_step_ == 1 or (who_step_ == 0 and renpy.random.randint(1, 11) > 5):
                    # если ни у кого нет козырей и первый ходит игрок
                    text = p_no_trump_phrase.text
                    image = p_no_trump_phrase.image
                    durak_step = 'player'
                else:
                    # если ни у кого нет козырей и первый ходит противник
                    text = n_no_trump_phrase.text
                    image = n_no_trump_phrase.image
                    durak_step = 'npc'
            else:
                # у игрока нет козыря, а у противника есть
                text = player_no_trump_phrase.text
                image = player_no_trump_phrase.image
                durak_step = 'npc'
        elif npc_trump_ is None:
            # у противника нет козыря, а у игрока есть
            act='hide'
            text = npc_no_trump_phrase.text
            image = npc_no_trump_phrase.image
            durak_step = 'player'
        else:
            act='hide'
            if player_cards_.lesser_trump().value < npc_trump_:
                # меньший козырь у игрока
                text = lesser_trump_phrase.text
                image = lesser_trump_phrase.image
                durak_step = 'player'
            else:
                # меньший козырь у противника
                text = bigger_trump_phrase.text
                image = bigger_trump_phrase.image
                durak_step = 'npc'
        renpy.show_screen('phrase_modal_text', message=text, act=act)
        renpy.show_screen('phrase_modal', message=text, image=image, act=act, fast=True)


    # окончание хода, определение сколько карт будет выдано
    def end_move(last_move, next=None, who_cant=None):
        global card_deck_, player_cards_, npc_cards_, durak_step, who_win_, npc_emotion_

        if len(card_deck_) != 0: # если в колоде есть карты
            for_player = 0 # сколько карт будет выдано игроку
            for_npc = 0 # сколько карт будет выдано противнику
            need_player = 6-player_cards_.qt() if player_cards_.qt() < 6 and who_cant != 'p' else 0 # сколько карт не хвает игроку
            need_npc = 6-npc_cards_.qt() if npc_cards_.qt() < 6 and who_cant != 'n' else 0 # сколько карт не хвает противнику
            if need_player+need_npc <= len(card_deck_):
                # если колоды хватает, чтобы выдать карты и игроку и противнику
                for_player = need_player
                for_npc = need_npc
            else:
                # если колоды не хватает
                have_cards = len(card_deck_)
                while have_cards != 0: # колода тратиться до последнего
                    if need_player < need_npc or (need_player == need_npc and last_move == 'n'):
                        for_npc += 1
                        need_npc -= 1
                    elif need_player > need_npc or (need_player == need_npc and last_move == 'p'):
                        for_player += 1
                        need_player -= 1
                    have_cards -= 1
            issue_cards(last_move, for_player, for_npc, move=next)
        else:
            if npc_cards_.qt() == 0 and player_cards_.qt() == 0:
                who_win_ = 1
                renpy.jump('end_card_game')
            elif npc_cards_.qt() == 0:
                who_win_ = 0
                renpy.jump('end_card_game')
            elif player_cards_.qt() == 0:
                who_win_ = 2
                renpy.jump('end_card_game')
            else:
                durak_step = next
            if next == 'npc':
                npc_emotion_.change('thinks')
                renpy.show_screen('npc_attack_t')
                

    # выдача новых карт
    def issue_cards(first, p, n, move):
        global card_deck_
        second = 'n' if first == 'p' else 'p'
        num1 = p if first == 'p' else n
        x = num1 # пиздец какой-то, этот x спас мне жизнь
        num2 = n if first == 'p' else p
        cards = []
        t = 0.01
        
        while num1 != 0:
            cards.append(card_deck_[num1-1])
            name = 'c1'+str(num1)
            renpy.show_screen('issue_card', _tag = name, who=first, t=t, name=name)
            t += 0.3
            num1 -= 1

        t += 0.1
        if first == 'p' and p != 0:
            renpy.show_screen('change_player_cards', act='issue_card', card=cards, t=t)

        cards = []
        while num2 != 0:
            cards.append(card_deck_[x+num2-1])
            name = 'c2'+str(num2)
            renpy.show_screen('issue_card', _tag = name, who=second, t=t, name=name)
            t += 0.3
            num2 -= 1

        t += 0.1
        if second == 'p' and p != 0:
            renpy.show_screen('change_player_cards', act='issue_card', card=cards, t=t)

        renpy.show_screen('change_durak_move', t=t, move=move)


    def card_deck_remove(qt):
        global card_deck_
        del card_deck_[0:qt]


    def spot_move_num():
        global move_num, durak_step, last_step
        try:
            if durak_step != last_step:
                if durak_step == 'npc' or durak_step == 'player':
                    move_num += 1
                last_step = durak_step
        except NameError:
            config.overlay_functions.remove(spot_move_num)
                


    # Удаляет добавленные функции в оверлей
    def reset_overlay_functions():
        for i in [spot_move_num]:
            if i in config.overlay_functions:
                config.overlay_functions.remove(i)

    
# Экран для теста игры, не имеет фактического значения
screen test():
    zorder 1000

    $ card_deck_name = [x.name() for x in card_deck_]

    drag:
        yalign 0.8
        frame:
            ysize 200
            xfill False
            hbox:
                xfill False
                viewport id "ach_dbg":
                    mousewheel True
                    xfill False
                    vbox:
                        xfill False
                        text "[trump_] | [move_num]"
                        text "-------"
                        text "[npc_cards_.names()]"
                        text "-------"
                        text "[playing_field_.cards_attack]"
                        text "-------"
                        text "[player_cards_.names()]"
                        text "-------"
                        text "[card_deck_name]"
                        text "-------"
                        text "[config.overlay_functions]"
                        text "-------"
                        vbar value YScrollValue("ach_dbg")

# Метка мини-игры
label durak_game:

    $ renpy.stop_skipping()

    stop music fadeout 0.5

    # сохраняется значение конфигов, чтобы вернуться к ним по окончанию игры
    $ save_options_ = [quick_menu, _dismiss_pause, config.has_autosave, config.autosave_on_quit, config.context_callback]

    $ quick_menu = False # отключает быстрое меню
    $ _dismiss_pause = False # блокирует возможность пропуска паузы

    scene bg durak with Fade(0.2, 0.3, 0.5)
    window hide
    play music durak fadein 1.5 volume durak_music_valume
    pause 0.4

    # отключение автосохранений
    $ config.has_autosave = False 
    $ config.autosave_on_quit = False
    
    $ start_durak() # запускает игру
    $ renpy.block_rollback()

    
    $ config.overlay_functions.append(spot_move_num)

    #show screen test

    # в зависимости от того кто раздаёт карты обращается к нужной метки с раздачей
    if player_takes_cards_:
        call player_takes_cards from _call_player_takes_cards
    else:
        call npc_takes_cards from _call_npc_takes_cards

    pause 0.1

    # показ начального диалога, определение чей ход первый
    if first_step_ == 1:
        $ durak_step = 'player'
        if pc_start_phrase_.can:
            $ pc_start_phrase_.show(act='hide')
    elif first_step_ == 2:
        $ durak_step = 'npc' 
        if npc_start_phrase_.can:
            $ npc_start_phrase_.show(act='hide')
    else:
        if start_phrase_.can:
            $ start_phrase_.show(act='choice_trump_modal')

    show screen durak_card_game with Dissolve(.3)
    scene bg durak

    $ ui.interact()

    pause

    return


# карты раздаёт игрок
label player_takes_cards:

    show screen durak_noti(durak_noti_name['player_takes'], 2)
    pause 0.2

    show backcard as c0 zorder 100:
        zoom 1.7 xalign 0.5 yalign 1.5 rotate 0
        easein_back .8 yalign 1.17

    pause .8

    $ _dismiss_pause = True
    show screen takes_cards

    pause

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c1:
        zoom 1.7 xalign 0.5 yalign 1.1
        parallel:
            ease 0.3 zoom 1.2
        parallel:
            easein_quint 0.8 xalign 0.4 yalign 0.3 rotate -10

    $ who_gets_ = 1
    pause

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c2:
        zoom 1.7 xalign 0.5 yalign 1.1
        parallel:
            ease 0.3 zoom 1.2
        parallel:
            easein_quint 0.8 xalign 0.66 yalign 0.76 rotate -5

    $ who_gets_ = 0
    pause

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c3:
        zoom 1.7 xalign 0.5 yalign 1.1
        parallel:
            ease 0.3 zoom 1.2
        parallel:
            easein_quint 0.8 xalign 0.43 yalign 0.3 rotate -5

    $ who_gets_ = 1
    pause

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c4:
        zoom 1.7 xalign 0.5 yalign 1.1
        parallel:
            ease 0.3 zoom 1.2
        parallel:
            easein_quint 0.8 xalign 0.67 yalign 0.76 rotate -8

    $ who_gets_ = 0
    pause

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c5:
        zoom 1.7 xalign 0.5 yalign 1.1
        parallel:
            ease 0.3 zoom 1.2
        parallel:
            easein_quint 0.8 xalign 0.35 yalign 0.35 rotate 5

    $ who_gets_ = 1
    pause

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c6:
        zoom 1.7 xalign 0.5 yalign 1.1
        parallel:
            ease 0.3 zoom 1.2
        parallel:
            easein_quint 0.8 xalign 0.60 yalign 0.73 rotate -18

    $ who_gets_ = 0
    pause

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c7:
        zoom 1.7 xalign 0.5 yalign 1.1
        parallel:
            ease 0.3 zoom 1.2
        parallel:
            easein_quint 0.8 xalign 0.45 yalign 0.35 rotate -14

    $ who_gets_ = 1
    pause

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c8:
        zoom 1.7 xalign 0.5 yalign 1.1
        parallel:
            ease 0.3 zoom 1.2
        parallel:
            easein_quint 0.8 xalign 0.7 yalign 0.76 rotate 5

    $ who_gets_ = 0
    pause

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c9:
        zoom 1.7 xalign 0.5 yalign 1.1
        parallel:
            ease 0.3 zoom 1.2
        parallel:
            easein_quint 0.8 xalign 0.4 yalign 0.37 rotate -1

    $ who_gets_ = 1
    pause

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c10:
        zoom 1.7 xalign 0.5 yalign 1.1
        parallel:
            ease 0.3 zoom 1.2
        parallel:
            easein_quint 0.8 xalign 0.66 yalign 0.7 rotate 3

    $ who_gets_ = 0
    pause

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c11:
        zoom 1.7 xalign 0.5 yalign 1.1
        parallel:
            ease 0.3 zoom 1.2
        parallel:
            easein_quint 0.8 xalign 0.3 yalign 0.33 rotate -20

    $ who_gets_ = 1
    pause

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c12:
        zoom 1.7 xalign 0.5 yalign 1.1
        parallel:
            ease 0.3 zoom 1.2
        parallel:
            easein_quint 0.8 xalign 0.7 yalign 0.7 rotate -5

    $ who_gets_ = None
    pause

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c13:
        card_deck_[-1].image()
        zoom 1.7 xalign 0.5 yalign 1.1
        parallel:
            ease 0.3 zoom 1.2
        parallel:
            easein_quint 0.8 xalign 0.35 yalign 0.75 rotate -100

    pause 0.2
    show screen durak_noti(card_deck_[-1].suit_name()+durak_noti_name['trump'], -0.5)
    pause

    play audio ["<silence .1>", slide_ ] volume sound_card_valume
    show backcard as c13 zorder 1:
        card_deck_[-1].image()
        easein_quint 1 xalign -0.06 yalign 0.2 rotate -250
    pause

    play audio ["<silence .25>", slide_ ] volume sound_card_valume
    show backcard as c0 zorder 2:
        ease_cubic 1 xalign -0.1 yalign 0.17 rotate 200 zoom 1.2

    $ _dismiss_pause = False

    pause 0.7
    hide screen takes_cards

    play audio ["<silence .2>", slide_ ] volume sound_card_valume
    show backcard as c1:
        ease_cubic 1 yalign -0.5
    show backcard as c3:
        ease_cubic 1 yalign -0.5
    show backcard as c5:
        ease_cubic 1 yalign -0.5
    show backcard as c7:
        ease_cubic 1 yalign -0.5
    show backcard as c9:
        ease_cubic 1 yalign -0.5
    show backcard as c11:
        ease_cubic 1 yalign -0.5
    pause 0.2

    play audio ["<silence .3>", slide_ ] volume sound_card_valume
    show backcard as c2:
        ease_cubic 1 yalign 1.5
    show backcard as c4:
        ease_cubic 1 yalign 1.5
    show backcard as c6:
        ease_cubic 1 yalign 1.5
    show backcard as c8:
        ease_cubic 1 yalign 1.5
    show backcard as c10:
        ease_cubic 1 yalign 1.5
    show backcard as c12:
        ease_cubic 1 yalign 1.5
    pause 0.5

    return



# анимация раздачи карт противником
label npc_takes_cards:

    play audio ["<silence .1>", slide_ ] volume sound_card_valume

    show backcard as c0:
        zoom 1.2 yalign 0.0 xalign 1.15 rotate 90
        easein_quint 1.2 yalign 0.5 xalign 0.2 rotate -10
    pause 1.1

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c1:
        zoom 1.2 yalign 0.5 xalign 0.2 rotate -10
        pause 0.1
        easein_quint 0.8 yalign 0.15 xalign 0.45 rotate 10
    pause 0.15

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c2:
        zoom 1.2 yalign 0.5 xalign 0.2 rotate -10
        pause 0.1
        easein_quint 0.8 yalign 0.8 xalign 0.45 rotate 2
    pause 0.15

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c3:
        zoom 1.2 yalign 0.5 xalign 0.2 rotate -10
        pause 0.1
        easein_quint 0.8 yalign 0.2 xalign 0.48 rotate -2
    pause 0.15

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c4:
        zoom 1.2 yalign 0.5 xalign 0.2 rotate -10
        pause 0.1
        easein_quint 0.8 yalign 0.8 xalign 0.4 rotate 15
    pause 0.15

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c5:
        zoom 1.2 yalign 0.5 xalign 0.2 rotate -10
        pause 0.1
        easein_quint 0.8 yalign 0.2 xalign 0.5 rotate 8
    pause 0.15

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c6:
        zoom 1.2 yalign 0.5 xalign 0.2 rotate -10
        pause 0.1
        easein_quint 0.8 yalign 0.85 xalign 0.48 rotate 10
    pause 0.15

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c7:
        zoom 1.2 yalign 0.5 xalign 0.2 rotate -10
        pause 0.1
        easein_quint 0.8 yalign 0.2 xalign 0.38 rotate -3
    pause 0.15

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c8:
        zoom 1.2 yalign 0.5 xalign 0.2 rotate -10
        pause 0.1
        easein_quint 0.8 yalign 0.8 xalign 0.56 rotate -15
    pause 0.15

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c9:
        zoom 1.2 yalign 0.5 xalign 0.2 rotate -10
        pause 0.1
        easein_quint 0.8 yalign 0.2 xalign 0.35 rotate 10
    pause 0.15

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c10:
        zoom 1.2 yalign 0.5 xalign 0.2 rotate -10
        pause 0.1
        easein_quint 0.8 yalign 0.85 xalign 0.55 rotate 30
    pause 0.15

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c11:
        zoom 1.2 yalign 0.5 xalign 0.2 rotate -10
        pause 0.1
        easein_quint 0.8 yalign 0.2 xalign 0.56 rotate 20
    pause 0.15

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c12:
        zoom 1.2 yalign 0.5 xalign 0.2 rotate -10
        pause 0.1
        easein_quint 0.8 yalign 0.8 xalign 0.37 rotate -3
    pause 0.8

    play audio ["<silence .15>", take_] volume sound_card_valume
    show backcard as c13:
        parallel:
            zoom 1.2 yalign 0.5 xalign 0.2 rotate -10
            pause 0.1
            easein_quint 1 yalign 0.5 xalign 0.45 rotate 270
        parallel:
            pause 0.15
            card_deck_[-1].image() with Dissolve(0.1)

    pause 0.2
    show screen durak_noti(card_deck_[-1].suit_name()+durak_noti_name['trump'], -0.5)
    pause 2.3

    play audio ["<silence .1>", slide_ ] volume sound_card_valume
    show backcard as c13 zorder 1:
        card_deck_[-1].image()
        easein_quint 1 xalign -0.06 yalign 0.2 rotate -250
    pause 0.5

    play audio ["<silence .25>", slide_ ] volume sound_card_valume
    show backcard as c0 zorder 2:
        ease_cubic 1 xalign -0.1 yalign 0.17 rotate 200
    pause 0.7

    play audio ["<silence .2>", slide_ ] volume sound_card_valume
    show backcard as c1:
        ease_cubic 1 yalign -0.5
    show backcard as c3:
        ease_cubic 1 yalign -0.5
    show backcard as c5:
        ease_cubic 1 yalign -0.5
    show backcard as c7:
        ease_cubic 1 yalign -0.5
    show backcard as c9:
        ease_cubic 1 yalign -0.5
    show backcard as c11:
        ease_cubic 1 yalign -0.5
    pause 0.2

    play audio ["<silence .25>", slide_ ] volume sound_card_valume
    show backcard as c2:
        ease_cubic 1 yalign 1.5
    show backcard as c4:
        ease_cubic 1 yalign 1.5
    show backcard as c6:
        ease_cubic 1 yalign 1.5
    show backcard as c8:
        ease_cubic 1 yalign 1.5
    show backcard as c10:
        ease_cubic 1 yalign 1.5
    show backcard as c12:
        ease_cubic 1 yalign 1.5
    pause 0.5

    return



# лейбл конца игры
label end_card_game:

    stop music fadeout 0.5
    # возвращение прежних настроек
    $ quick_menu = save_options_[0]
    $ _dismiss_pause = save_options_[1]
    $ config.has_autosave = save_options_[2]
    $ config.autosave_on_quit = save_options_[3]
    $ config.context_callback = save_options_[4]
    $ reset_overlay_functions()
    
    $ renpy.scene(layer = "screens")
    scene black
    with Dissolve(.3)
    window show

    $ renpy.block_rollback() # блокирует откат

    return


################################################################################
##### made by N0Fanru 
################################################################################