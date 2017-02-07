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


class Player:
    def __init__(self, order):
        self.order = order
        self.hand = None

        self.scores = {
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
        return sum([score for score in self.scores.values() if score is not None])

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, str(self))

    def play_round(self):
        self.hand = dice.Hand()
        return

    @property
    def available_scores(self):
        scores = []
        for kind, score in self.scores.items():
            if score is None:
                scores.append(kind)
        return scores


class Human(Player):
    def __init__(self, order, name=None):
        super().__init__(order)
        self.name = name

    def __str__(self):
        return self.name

    def show_available_scores(self):
        print("You can score: {}".format(', '.join(self.available_scores)))

    def get_score(self):
        what_to_score = input("What do you want to score? ")
        if what_to_score not in self.available_scores:
            return self.get_score()
        score = self.hand.score(what_to_score)
        self.scores[what_to_score] = score
        return

    def play_round(self):
        super().play_round()
        print(self.name.center(90))
        print('-'*90)
        print("Here's your hand:")
        die_lines = []
        for die in self.hand:
            die_lines.append(die.display.split('\n'))
        for i in range(5):
            for die in die_lines:
                print(die[i], end='\t')
            print('')
        for index, key in enumerate(self.available_scores, start=1):
            print("{:^30}".format(key), end='\t')
            if not index % 3:
                print('')
        print('\n', '-'*90)
        self.get_score()
        return


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
        best_move = self.hand.score_max(self.available_scores)
        score = self.hand.score(best_move)
        self.scores[best_move] = score
        return

