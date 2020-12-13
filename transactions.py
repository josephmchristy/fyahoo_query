#! python

import datetime
import logging

logging.basicConfig(level=logging.DEBUG)

players = {}


class Player:
    def __init__(self, name='', owner='', drop_date=None, cost=5):
        self.name = name
        self.owner = owner
        self.drop_date = drop_date
        self.cost = cost


# Add Player Transaction
def addPlayer(transaction, is_waiver_trade=False):
    owner_name = transaction['owner']
    player_name = transaction['player']

    # If player does not exist, create new player
    if player_name not in players:
        players[player_name] = Player(name=player_name)

    # Update player's owner and cost
    player = players[player_name]
    player.owner = owner_name
    if not is_waiver_trade:
        if player.cost > 5:
            player.cost = 5


# Drop Player Transaction
def dropPlayer(transaction):
    player_name = transaction['player']

    # Update player's owner and drop date
    player = players[player_name]
    player.owner = ''
    player.drop_date = datetime.date.today()


# Add Drop Waiver Transaction
def addDropWaiver(transaction):
    
    # Check if the transaction is a waiver
    is_waiver = False
    if(transaction['type'] == 'waiver'):
        is_waiver = True

    transaction_add = {'owner': transaction['owner'], 'player': transaction['player'][0]}
    transaction_drop = {'player': transaction['player'][1]}
    addPlayer(transaction_add)
    dropPlayer(transaction_drop)
