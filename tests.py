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


class transactiontests(unittest.testcase):

    @classmethod
    def setupclass(cls):
        cls.transaction_add = {'type': 'add',
                               'owner': 'john doe',
                               'player': 'add_drop player'}
        cls.transaction_drop = {'date': datetime.date(2020, 12, 9),
                                'type': 'drop',
                                'owner': 'john doe',
                                'player': 'add_drop player'}
        cls.transaction_add_drop = {'date': datetime.date(2020, 12, 12),
                                    'type': 'adddrop',
                                    'owner': 'john doe',
                                    'player': ('add player',
                                               'add_drop player')}
        cls.transaction_waiver = {'date': datetime.date(2020, 12, 12),
                                  'type': 'waiver',
                                  'owner': 'john doe',
                                  'player': ('waiver player', 'add player')}

    @classmethod
    def tearDownClass(cls):
        del cls.transaction_add
        del cls.transaction_drop

    # Test an add transaction
    def test_add(self):
        transactions.addPlayer(self.transaction_add)
        added_player = transactions.players[self.transaction_add['player']]
        self.assertEqual(added_player.name, 'Add_Drop Player')
        self.assertEqual(added_player.owner, 'John Doe')
        self.assertEqual(added_player.cost, 5)

    # Test a drop transaction
    def test_drop(self):
        transactions.dropPlayer(self.transaction_drop)
        dropped_player = transactions.players[self.transaction_drop['player']]
        self.assertEqual(dropped_player.owner, '')
        self.assertEqual(dropped_player.drop_date, datetime.date(2020, 12, 9))

    # Test an add drop transaction
    def test_add_drop(self):
        transactions.addPlayer(self.transaction_add)
        transactions.addDropWaiver(self.transaction_add_drop)
        added_player = transactions.players[self.transaction_add_drop['player'][0]]
        dropped_player = transactions.players[self.transaction_add_drop['player'][1]]
        self.assertEqual(added_player.owner, 'John Doe')
        self.assertEqual(dropped_player.owner, '')
        self.assertEqual(dropped_player.drop_date, datetime.date(2020, 12, 12))

    # Test a waiver transaction
    def test_waiver(self):
        waiverPlayer = transactions.Player('Waiver Player', 'John Doe', datetime.date(2020, 12, 8), 3)
        transactions.players.update({waiverPlayer.name: waiverPlayer})
        transactions.addDropWaiver(self.transaction_waiver)
        added_player = transactions.players[self.transaction_waiver['player'][0]]
        dropped_player = transactions.players[self.transaction_waiver['player'][1]]
        self.assertEqual(added_player.owner, 'John Doe')
        self.assertEqual(added_player.cost, 3)
        self.assertEqual(dropped_player.owner, '')
        self.assertEqual(dropped_player.drop_date, datetime.date(2020, 12, 12))
        print('Current players: {}'.format(transactions.players))


if __name__ == '__main__':
    unittest.main()
