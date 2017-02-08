from operator import attrgetter
import os

import player


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class Yatzy:
    def __init__(self, humans=0, bots=0):
        self.all_computer = (not humans and bots)
        self.humans = []
        self.bots = []

        self.current_round = 1
        self.scores = {}

        self.game_board_width = 90

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

    def show_player_info(self, player):
        print('{0:^{1}}'.format(
            '{} ({})'.format(player.name, player.score),
            self.game_board_width
        ))
        print('-'*self.game_board_width)

    def human_precursor(self, human):
        self.show_player_info(human)
        human.hand.display(self.game_board_width)
        print('-'*self.game_board_width)

    def get_human_action(self, human):
        prompt = "[S]core"
        if human.hand.left_to_reroll:
            prompt += " or [R]eroll"
        action = input('{}: '.format(prompt)).lower()
        if action not in 'sr':
            return show_human_prompt()
        return action

    def get_human_score(self, human):
        clear()
        self.human_precursor(human)
        human.scoresheet.display(self.game_board_width)
        print('-'*self.game_board_width)
        category_to_score = input("What do you want to score? ").upper()
        if category_to_score not in human.scoresheet.open_keys:
            return self.get_human_score(human)
        else:
            category = human.scoresheet.get_by_key(category_to_score)
        score = human.hand.score(category.name)
        human.scoresheet.score_category(category_to_score, score)

    def human_round(self, human):
        self.human_precursor(human)
        action = self.get_human_action(human)
        if action == 's':
            self.get_human_score(human)
        else:
            self.human_reroll(human)

    def play_round(self):
        for human in self.humans:
            clear()
            human.roll()
            self.human_round(human)
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
    print("How many are playing? (Press ENTER for 0)")
    human_count = int(input("Human players? ") or '0')
    bot_count = int(input("Computer players? ") or '0')

    return human_count, bot_count

if __name__ == '__main__':
    try:
        humans, bots = start_game()
        game = Yatzy(humans=humans, bots=bots)
    except ValueError as err:
        print("No one's playing? OK")
    else:
        game.play()
