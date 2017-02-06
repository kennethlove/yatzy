import random


class Die(int):
    def __new__(cls, *args, **kwargs):
        return super(Die, cls).__new__(cls, random.randint(1, 6))

    def __init__(self, *args, **kwargs):
        super(int, self).__init__(*args, **kwargs)
        self.rerolls = 0

    def roll(self):
        self.rerolls += 1
        self = random.randint(1, 6)
        return self


class Hand(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _ in range(5):
            self.append(Die())
