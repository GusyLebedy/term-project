import random


class Deck():
    def __init__(self):
        self.cards = {'1': [3, 4, ''], '2': [2, 4, 'свойство 1'], '3': [2, 4, 'свойство 1'], '4': [5, 2, ''], '5': [1, 2, ''], '6': [4, 4, 'свойство 2'],
     '7': [2, 4, 'свойство 3'], '8': [3, 4, ''], '9': [4, 4, 'свойство 4'], '10': [3, 4, 'свойство 5']}
        self.card_shuffle = []
        for i in self.cards:
            self.card_shuffle += [i] * self.cards[i][1]
        random.shuffle(self.card_shuffle)
        self.position = 0
        print(self.card_shuffle)

    def next_card(self):
        answer = [self.card_shuffle[self.position],self.cards[self.card_shuffle[self.position]]]
        self.position += 1
        return answer


class Game(Deck):
    def new_card(self):
        if self.position < 36:
            new_card = Deck.next_card(self)
            # self.card_in_row.append(new_card)
            return new_card
        else:
            print('game over')
            return False


c = Game()
word = c.new_card()
while word != False:
    print(word)
    # print(c.card_in_row)
    word = c.new_card()