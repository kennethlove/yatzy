from operator import attrgetter

import player


class Game:
    def __init__(self, humans=0, bots=0):
        self.all_computer = (not humans and bots)
        self.humans = []
        self.bots = []

        self.current_round = 1
        self.scores = {}

        if humans and not self.all_computer:
            self.humans = self.get_humans(humans)

        if bots or self.all_computer:
            self.bots = self.get_bots(bots)

        if not humans and not bots:
            raise ValueError("Must provide either human or bot players")

    def get_humans(self, num):
        humans = []
        for order in range(1, num+1):
            name = input("Name for Player {}: ".format(order))
            humans.append(player.Human(order, name))
        return humans

    def get_bots(self, num):
        bots = set()
        while len(bots) < num:
            bots.add(player.Bot(len(bots)+1))
        return list(sorted(list(bots), key=lambda bot: bot.order))

    def play_round(self):
        for human in self.humans:
            human.play_round()
        for bot in self.bots:
            bot.play_round()
        self.current_round += 1
        return

    def play(self):
        while self.current_round <= 15:
            self.play_round()
        else:
            winner = max(self.humans+self.bots, key=attrgetter('score'))
            print("{} won with {} points!".format(winner.name, winner.score))


if __name__ == '__main__':
    game = Game(humans=1, bots=1)
    game.play()
