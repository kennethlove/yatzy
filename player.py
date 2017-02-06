import random

BOT_NAMES = [
    'Acid Burn',
    'Crash Override',
    'Zero Cool',
    'Cereal Killer',
    'Lord Nikon',
    'The Plague',
    'Razor',
    'Blade',
    'Phantom Phreak',
]


class Player:
    def __init__(self, order):
        self.order = order
        self.score = 0

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, str(self))


class Human(Player):
    def __init__(self, order, name=None):
        super().__init__(order)
        self.name = name

    def __str__(self):
        return self.name


class Bot(Player):
    def __init__(self, order):
        super().__init__(order)
        self.name = random.choice(BOT_NAMES)

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return id(str(self.name))

