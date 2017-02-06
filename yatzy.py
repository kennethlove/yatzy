from player import Human, Bot


class Game:
    def __init__(self, humans=0, bots=0):
        self.all_computer = (not humans and bots)
        self.humans = []
        self.bots = []

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
            humans.append(Human(order, name))
        return humans

    def get_bots(self, num):
        bots = set()
        while len(bots) < num:
            bots.add(Bot(len(bots)+1))
        return list(sorted(list(bots), key=lambda bot: bot.order))


