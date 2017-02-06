from functools import reduce
from operator import add
from test.support import captured_stdout, captured_stdin
import unittest

import yatzy
import player
import dice


class GameTests(unittest.TestCase):
    def test_bad_init(self):
        with self.assertRaises(ValueError):
            game = yatzy.Game()

    def test_one_human(self):
        with captured_stdout() as stdout, captured_stdin() as stdin:
            stdin.write("Kenneth")
            stdin.seek(0)
            game = yatzy.Game(humans=1)
        self.assertEqual("Name for Player 1: ", stdout.getvalue())
        self.assertEqual(len(game.humans), 1)

    def test_two_humans(self):
        with captured_stdout() as stdout, captured_stdin() as stdin:
            stdin.write("Kenneth\n")
            stdin.write("Elaine\n")
            stdin.seek(0)
            game = yatzy.Game(humans=2)
        self.assertIn("Name for Player 2:", stdout.getvalue())
        self.assertEqual(len(game.humans), 2)
        self.assertEqual(game.humans[1].name, "Elaine")

    def test_one_bot(self):
        game = yatzy.Game(bots=1)
        self.assertEqual(len(game.bots), 1)

    def test_two_bots(self):
        game = yatzy.Game(bots=2)
        self.assertEqual(len(game.bots), 2)
        self.assertEqual(len({game.bots[0].name, game.bots[1].name}), 2)


class PlayerTests(unittest.TestCase):
    def test_human(self):
        human1 = player.Human(1, "Kenneth")
        self.assertEqual(human1.name, "Kenneth")

    def test_bot(self):
        bot1 = player.Bot(1)
        self.assertIn(bot1.name, player.BOT_NAMES)


class DiceTests(unittest.TestCase):
    def test_die(self):
        die = dice.Die()
        self.assertIn(die, range(1, 7))

    def test_hand(self):
        hand = dice.Hand()
        self.assertEqual(len(hand), 5)

    def test_reroll(self):
        hand = dice.Hand()
        print(hand)
        print(reduce(add, hand))
        hand[0].roll()
        print(reduce(add, hand))
        print(hand)
