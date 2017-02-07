from operator import attrgetter
import os

import player


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


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
            clear()
            human.play_round()
        for bot in self.bots:
            bot.play_round()
        self.current_round += 1
        return

    def play(self):
        while self.current_round <= 15:
            self.play_round()
        else:
            all_players = list(
                sorted(
                    self.humans+self.bots,
                    key=attrgetter('score'),
                    reverse=True
                )
            )
            print("{} won with {} points!".format(all_players[0].name, all_players[0].score))
            for player in all_players[1:]:
                print("{} finished with {} points".format(player.name, player.score))


def start_game():
    while True:
        try:
            human_count = int(input("How many human players? "))
        except ValueError:
            continue
        else:
            break

    while True:
        try:
            bot_count = int(input("How many computer players? "))
        except ValueError:
            continue
        else:
            break

    return human_count, bot_count

if __name__ == '__main__':
    try:
        humans, bots = start_game()
        game = Game(humans=humans, bots=bots)
    except ValueError as err:
        print("No one's playing? OK")
    else:
        game.play()
