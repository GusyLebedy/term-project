import random


class Deck():
    def __init__(self):
        self.cards = {'1': [3, 4, ''], '2': [2, 4, 'свойство 1'], '3': [2, 4, 'свойство 1'], '4': [5, 2, ''],
                      '5': [1, 2, ''], '6': [4, 4, 'свойство 2'],
                      '7': [2, 4, 'свойство 3'], '8': [3, 4, ''], '9': [4, 4, 'свойство 4'], '10': [3, 4, 'свойство 5']}
        self.card_shuffle = []
        for i in self.cards:
            self.card_shuffle += [i] * self.cards[i][1]
        random.shuffle(self.card_shuffle)
        self.position = 0
        print(self.card_shuffle)

    def next_card(self, next_position: bool = True):
        answer = [self.card_shuffle[self.position], self.cards[self.card_shuffle[self.position]]]
        if next_position:
            self.position += 1
        return answer

    def game_over(self):
        return self.position != len(self.card_shuffle)


class Counter:
    prayer_counter = 0
    win_count = 0
    current_card_streak = []
    current_card_counter = 0

    def empty_current(self):
        self.current_card_streak = []
        self.current_card_counter = 0

    def add_current(self, number_, card_):
        self.current_card_streak.append(card_)
        self.current_card_counter += number_

    def add_to_total(self):
        self.prayer_counter += self.current_card_counter

    def check_to_card_in(self, card_):
        return card_ in self.current_card_streak

    def give_(self):
        return self.current_card_streak, self.prayer_counter


class Player:
    def __init__(self):
        pass


class Game(Deck, Counter, Player):
    def main(self):
        print(1)


c = Game()

c.win_count = int(input('Введите количество очков для победы '))
while c.game_over():
    current_card = c.next_card()
    checker = c.check_to_card_in(current_card)
    first_, second_ = c.give_()
    c.add_current(current_card[1][0], current_card)
    print(first_, '\n Ваша текущая сумма: ' + str(second_))
    if checker in c.current_card_streak:
        print('Вы поймали повтор ')
        c.empty_current()
    else:
        answer_ = int(input('Введите 1, если хотите взять ещё одну карту, и 2, если забрать карты '))
        if answer_ == 2:
            c.add_to_total()
            c.empty_current()