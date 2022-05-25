import random
import json


def handler(event, context):
    end_ses = 'false'
    if event['state']['session'] == {}:
        object_, text = start()
    else:
        object_ = Game(False, event['state']['session'])
        command_ = event['request']['original_utterance']
        if object_.game_over() is False:
            text = 'Ты проиграл!'
            end_ses = 'true'
            object_ = take_card(object_)
        elif command_.lower() == "продолжить":
            object_, text = next_card1(object_)
        elif command_.lower() == "грабеж":
            object_ = take_card(object_)
            object_, text = next_card1(object_)
        else:
            text = 'Неверная команда.'
    if object_.win_count <= object_.player_counter:
        text = 'Ты победил!'
        end_ses = 'true'
    return {
        'version': event['version'],
        'session': event['session'],
        'response': {
            'text': text,
            'end_session': end_ses
        },
        'session_state': object_.give_json()
    }


class Game():
    player_counter = 0
    win_count = random.randint(80, 110)
    current_card_streak = []
    position = 0
    card_shuffle = []

    def __init__(self, new_: bool = False, data_: dict = {}):
        self.cards = {'1': [3, 4, '', 'Свеча'], '2': [2, 4, 'свойство 1', 'Сундук'], '3': [2, 4, 'свойство 1', 'Ключ'],
                      '4': [5, 2, '', 'Попугай'], '5': [1, 2, '', 'Штурвал'], '6': [4, 4, 'свойство 2', 'Компас'],
                      '7': [2, 4, 'свойство 3', 'Ром'], '8': [3, 4, '', 'Нож'], '9': [4, 4, 'свойство 4', 'Пистолет'],
                      '10': [3, 4, 'свойство 5', 'Якорь']}
        if new_:
            for i in self.cards:
                self.card_shuffle += [i] * self.cards[i][1]
            random.shuffle(self.card_shuffle)
            self.position = 0
        else:
            self.card_shuffle = data_['card_shuffle']
            self.player_counter = data_['player_counter']
            self.win_count = data_['win_count']
            self.current_card_streak = data_['current_card_streak']
            self.position = data_['position']

    def next_card(self, next_position: bool = True):
        answer = [self.card_shuffle[self.position], self.cards[self.card_shuffle[self.position]]]
        if next_position:
            self.position += 1
        return answer

    def game_over(self):
        return self.position != len(self.card_shuffle)

    def beautiful_print(self, list_):
        result_ = ''
        for i in list_:
            result_ += i[3] + ' (' + str(i[0]) + ') '
        return result_

    def count_sum(self, list_, bad_result: bool = False):
        result_ = 0
        count_for_prop_1 = 0
        for i in list_:
            if i[2] == 'свойство 4' and bad_result:
                bad_result = False
                break
            result_ += i[0]
            if i[2] == 'свойство 1':
                count_for_prop_1 += 1
        if count_for_prop_1 == 2:
            result_ *= 2
        if bad_result:
            return 0
        else:
            return result_

    def empty_current(self):
        self.current_card_streak = []

    def add_current(self, card_):
        self.current_card_streak.append(card_)

    def add_to_total(self, sum_):
        self.player_counter += sum_

    def check_to_card_in(self, card_):
        return card_ in self.current_card_streak

    def give_(self):
        return self.current_card_streak, self.player_counter

    def give_json(self):
        data_ = {
            'card_shuffle': self.card_shuffle,
            'win_count': self.win_count,
            'player_counter': self.player_counter,
            'current_card_streak': self.current_card_streak,
            'position': self.position
        }
        return data_


def start():
    new_object = Game(True)
    count = 0
    if count == 0:
        text = 'Привет, капитан' + '\n' + 'Здесь, в таверне «Адмирал Бенбоу», мы собрались, чтобы поделить сокровища.' + \
               ' Бери, сколько сможешь унести, но помни, что жадность губит флибустьера.' + \
               ' В колоде находится 36 карт-трофеев, каждой из них соответствует определенное количество очков.' + \
               ' Твоя задача – набрать очков больше, чем у Билли Бонса.' + ' Начни свой рейд за сокровищами – возьми первую карту. ' + \
               ' Ты можешь закончить рейд грабежом, сказав "грабеж"  и получить очки за этот трофей,' + \
               ' а можешь испытать удачу и продолжить тянуть карты, сказав "продолжить", чтобы заработать больше очков.' + \
               ' Из карт будет составляться ряд. Если трофеи в ряду повторятся, рейд будет провален, и очки за него обнулятся.' + \
               ' Некоторые из трофеев имеют свойства: ключ и сундук в одном ряду удвоят очки за рейд; пистолет зафиксирует полученные до него очки в ряду,' + \
               ' даже если рейд будет провален.' + ' Играй с умом и помни, жадность – это плохо.' + '\n' + '\n' + \
               'Количество очков для победы: ' + str(new_object.win_count) + '\n'
        count += 1
    else:
        text = 'Количество очков для победы: ' + str(new_object.win_count) + '\n'
    new_object, text1 = next_card1(new_object)
    return new_object, text + text1


def next_card1(obj_):
    current_card = obj_.next_card()
    checker = obj_.check_to_card_in(current_card[1])
    obj_.add_current(current_card[1])
    first_, second_ = obj_.give_()
    answer = ""
    answer += obj_.beautiful_print(first_)
    answer += '\nТвоя текущая сумма: ' + str(second_)
    if checker:
        answer += '\nРейд окончен.\n'
        obj_.add_to_total(obj_.count_sum(obj_.current_card_streak, True))
        obj_.empty_current()
        obj_, answer1 = next_card1(obj_)
        answer += answer1
    return obj_, answer


def take_card(obj_):
    obj_.add_to_total(obj_.count_sum(obj_.current_card_streak))
    obj_.empty_current()
    return obj_
