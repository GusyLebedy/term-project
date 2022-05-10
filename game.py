import random


class Trophy:
    def __init__(self, name):
        self.name = name

    def score(self):
        if self.name == 'candle':
            self.score = 3
            return self.score
        if self.name == 'chest':
            self.score = 2
            return self.score
        if self.name == 'key':
            self.score = 2
            return self.score
        if self.name == 'parrot':
            self.score = 5
            return self.score
        if self.name == 'wheel':
            self.score = 1
            return self.score
        if self.name == 'compass':
            self.score = 4
            return self.score
        if self.name == 'rum':
            self.score = 2
            return self.score
        if self.name == 'knife':
            self.score = 3
            return self.score
        if self.name == 'gun':
            self.score = 4
            return self.score
        if self.name == 'anchor':
            self.score = 3
            return self.score

    def characteristic(self):
        pass

    def amount(self):
        if self.name == 'candle':
            self.amount = 4
            return self.amount
        if self.name == 'chest':
            self.amount = 4
            return self.amount
        if self.name == 'key':
            self.amount = 4
            return self.amount
        if self.name == 'parrot':
            self.amount = 2
            return self.amount
        if self.name == 'wheel':
            self.amount = 2
            return self.amount
        if self.name == 'compass':
            self.amount = 4
            return self.amount
        if self.name == 'rum':
            self.amount = 4
            return self.amount
        if self.name == 'knife':
            self.amount = 4
            return self.amount
        if self.name == 'gun':
            self.amount = 4
            return self.amount
        if self.name == 'anchor':
            self.amount = 4
            return self.amount


class Character(Trophy):
    def characteristic(self):
        if self.name == 'test':
            self.characteristic = 5
            return self.characteristic


'''t = Trophy('wheel')
print(t.score(), t.amount())
c = Character('test')
print(c.characteristic())'''

trophies = {'candle': Trophy('candle').amount(), 'chest': Trophy('chest').amount(), 'key': Trophy('key').amount(),
            'parrot': Trophy('parrot').amount(), 'wheel': Trophy('wheel').amount(), 'compass': Trophy('compass').amount(),
            'rum': Trophy('rum').amount(), 'knife': Trophy('knife').amount(), 'gun': Trophy('gun').amount(),
            'anchor': Trophy('anchor').amount()}
# trophies['candle'] = Trophy('candle').amount() - 1
# print(trophies)
ans = []
tr = ['candle', 'chest', 'key', 'parrot', 'wheel', 'compass', 'rum', 'knife', 'gun', 'anchor']
cond = 1
while cond != 0:
    if trophies['candle'] == 0 and trophies['chest'] == 0 and trophies['key'] == 0 and trophies['parrot'] == 0 and trophies['wheel'] == 0\
        and trophies['compass'] == 0 and trophies['rum'] == 0 and trophies['knife'] == 0 and trophies['gun'] == 0 and trophies['anchor'] == 0:
        cond = 0
    ind = random.randint(0, 9)
    if trophies[tr[ind]] > 0:
        trophies[tr[ind]] = trophies[tr[ind]] - 1
        # print(tr[ind], trophies.get(tr[ind]))
        if tr[ind] == 'candle':
            ans.append('Свеча')
        if tr[ind] == 'chest':
            ans.append('Сундук')
        if tr[ind] == 'key':
            ans.append('Ключ')
        if tr[ind] == 'parrot':
            ans.append('Попугай')
        if tr[ind] == 'wheel':
            ans.append('Штурвал')
        if tr[ind] == 'compass':
            ans.append('Компас')
        if tr[ind] == 'rum':
            ans.append('Ром')
        if tr[ind] == 'knife':
            ans.append('Нож')
        if tr[ind] == 'gun':
            ans.append('Пистолет')
        if tr[ind] == 'anchor':
            ans.append('Якорь')
# print(trophies)
for x in ans:
    print(x)
