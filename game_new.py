import random


class Deck():
    def __init__(self):
        self.cards = {'1': [3, 4, '', 'Свеча'], '2': [2, 4, 'свойство 1', 'Сундук'], '3': [2, 4, 'свойство 1', 'Ключ'],
                      '4': [5, 2, '', 'Попугай'], '5': [1, 2, '', 'Штурвал'], '6': [4, 4, 'свойство 2', 'Компас'],
                      '7': [2, 4, 'свойство 3', 'Ром'], '8': [3, 4, '', 'Нож'], '9': [4, 4, 'свойство 4', 'Пистолет'],
                      '10': [3, 4, 'свойство 5', 'Якорь']}
        self.card_shuffle = []
        for i in self.cards:
            self.card_shuffle += [i] * self.cards[i][1]
        random.shuffle(self.card_shuffle)
        self.position = 0
        # print(self.card_shuffle)

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
            result_ += i[3] + ' '
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


class Player:
    def __init__(self):
        pass


class Game(Deck, Player):
    player_counter = 0
    win_count = 0
    current_card_streak = []

    def empty_current(self):
        self.current_card_streak = []

    def add_current(self, number_, card_):
        self.current_card_streak.append(card_)

    def add_to_total(self, sum_):
        self.player_counter += sum_

    def check_to_card_in(self, card_):
        return card_ in self.current_card_streak

    def give_(self):
        return self.current_card_streak, self.player_counter


c = Game()

c.win_count = int(input('Введите количество очков для победы: '))
while c.game_over() and c.player_counter < c.win_count:
    current_card = c.next_card()
    checker = c.check_to_card_in(current_card[1])
    c.add_current(current_card[1][0], current_card[1])
    first_, second_ = c.give_()
    print(c.beautiful_print(first_))
    print('Ваша текущая сумма: ' + str(second_))
    if checker:
        print('Вы поймали повтор')
        c.add_to_total(c.count_sum(c.current_card_streak, True))
        c.empty_current()
    else:
        if current_card[1][2] == 'свойство 2' and c.game_over():
            answer_ = input('Вы можете посмотреть следующую карту: ' + str(c.next_card(False)[1][3]) + '\nВведите 1, если хотите взять эту карту, и 2, если забрать карты: ')
            if answer_ == '1':
                current_card = c.next_card()
                checker = c.check_to_card_in(current_card[1])
                c.add_current(current_card[1][0], current_card[1])
                first_, second_ = c.give_()
        else:
            answer_ = input('Введите 1, если хотите взять ещё одну карту, и 2, если забрать карты: ')
        if answer_ == '2':
            # print(c.count_sum(c.current_card_streak))
            c.add_to_total(c.count_sum(c.current_card_streak))
            c.empty_current()
    print()
c.count_sum(c.current_card_streak)
if c.player_counter >= c.win_count:
    print('Ты победил')
else:
    print('Ты проиграл')