#! python

import unittest
import datetime

import transactions


class PlayerTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.empty_player = transactions.Player()
        cls.arg_player = transactions.Player('Arg Player', 'John Doe',
                                             datetime.date.today(), 7)

    @classmethod
    def tearDownClass(cls):
        del cls.empty_player
        del cls.arg_player

    # Test class constructor with no arguments
    def test_empty(self):
        self.assertEqual(self.empty_player.name, '')
        self.assertEqual(self.empty_player.owner, '')
        self.assertIsNone(self.empty_player.drop_date)
        self.assertEqual(self.empty_player.cost, 5)

    # Test class constructor with arguments
    def test_args(self):
        self.assertEqual(self.arg_player.name, 'Arg Player')
        self.assertEqual(self.arg_player.owner, 'John Doe')
        self.assertEqual(self.arg_player.drop_date, datetime.date.today())
        self.assertEqual(self.arg_player.cost, 7)


class TransactionTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.player_1 = transactions.Player('Player 1', 'John Doe', None, 5)
        cls.transaction_add = [datetime.date.today(), 'Add', 'John Doe',
                               'Player 1']
        cls.transaction_drop = [datetime.date.today(), 'Drop', 'John Doe', 'Player 1']

    @classmethod
    def tearDownClass(cls):
        del cls.player_1
        del cls.transaction_add
        del cls.transaction_drop

    # Test an add transaction
    def test_add(self):
        transactions.addPlayer(self.transaction_add)
        added_player = transactions.players[self.transaction_add[3]]
        self.assertEqual(added_player.name, self.player_1.name)
        self.assertEqual(added_player.owner, self.player_1.owner)
        self.assertIsNone(added_player.drop_date)
        self.assertEqual(added_player.cost, 5)

    # Test a drop transaction
    def test_drop(self):
        transactions.dropPlayer(self.transaction_drop)
        dropped_player = transactions.players[self.transaction_drop[3]]
        self.assertEqual(dropped_player.name, self.player_1.name)
        self.assertEqual(dropped_player.owner, '')
        self.assertEqual(dropped_player.drop_date, datetime.date.today())
        self.assertEqual(dropped_player.cost, 5)


if __name__ == '__main__':
    unittest.main()
