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
def addPlayer(transaction, is_waiver=False):
    owner_name = transaction['owner']
    player_name = transaction['player']

    # If player does not exist, create new player
    if player_name not in players:
        players[player_name] = Player(name=player_name)

    # Update player's owner and cost
    player = players[player_name]
    player.owner = owner_name
    if is_waiver and player.drop_date is not None:
        # If a player was dropped more than 3 days ago, they are not eligible to stay the same cost
        if transaction['date'] - datetime.timedelta(days = 3) > player.drop_date:
            is_waiver = False
    if not is_waiver:
        if player.cost > 5:
            player.cost = 5


# Drop Player Transaction
def dropPlayer(transaction):
    player_name = transaction['player']

    # Update player's owner and drop date
    player = players[player_name]
    player.owner = ''
    player.drop_date = transaction['date']


# Add Drop Waiver Transaction
def addDropWaiver(transaction):
    
    # Check if the transaction is a waiver
    is_waiver = False
    if transaction['type'] == 'Waiver':
        is_waiver = True

    transaction_add = {'date': transaction['date'], 'owner': transaction['owner'], 'player': transaction['player'][0]}
    transaction_drop = {'date': transaction['date'], 'player': transaction['player'][1]}
    addPlayer(transaction_add, is_waiver)
    dropPlayer(transaction_drop)
