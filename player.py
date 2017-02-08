import random

import dice

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


class Scoresheet:
    def __init__(self):
        self.categories = {
            'ones': None,
            'twos': None,
            'threes': None,
            'fours': None,
            'fives': None,
            'sixes': None,
            'one_pair': None,
            'two_pairs': None,
            'three_of_a_kind': None,
            'four_of_a_kind': None,
            'small_straight': None,
            'large_straight': None,
            'full_house': None,
            'chance': None,
            'yatzy': None
        }

    @property
    def score(self):
        return sum([score for score in self.categories.values() if score is not None])

    @property
    def open_categories(self):
        categories = []
        for kind, score in self.categories.items():
            if score is None:
                categories.append(kind)
        return categories


class Player:
    def __init__(self, order):
        self.order = order
        self.scoresheet = Scoresheet()
        self.hand = None

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, str(self))

    def roll(self):
        self.hand = dice.Hand()
        return

    @property
    def score(self):
        return self.scoresheet.score


class Human(Player):
    def __init__(self, order, name=None):
        super().__init__(order)
        self.name = name

    def __str__(self):
        return self.name

    def show_available_scores(self):
        print(
            "You can score: {}".format(
                ', '.join(
                    self.scoresheet.open_categories
                )
            )
        )

    def get_score(self):
        what_to_score = input("What do you want to score? ")
        if what_to_score not in self.scoresheet.open_categories:
            return self.get_score()
        score = self.hand.score(what_to_score)
        self.scoresheet.categories[what_to_score] = score
        return

    def play_round(self):
        super().play_round()

    # def play_round(self):
    #     super().play_round()
    #     # print('{:^90}'.format(self.hand.display()))
    #     for index, key in enumerate(self.scoresheet.open_categories, start=1):
    #         print("{:^30}".format(key), end='\t')
    #         if not index % 3:
    #             print('')
    #     print('\n', '-'*90)
    #     self.get_score()
    #     return


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

    def play_round(self):
        super().play_round()
        best_move = self.hand.score_max(self.scoresheet.open_categories)
        score = self.hand.score(best_move)
        self.scoresheet.categories[best_move] = score
        return

