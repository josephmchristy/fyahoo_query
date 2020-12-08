#! python

# import datetime
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
    # trans_date = transaction[0]
    owner_name = transaction[2]
    player_name = transaction[3]

    # If player does not exist, create new player
    if player_name not in players:
        players[player_name] = Player(name=player_name)

    # Update player's owner and cost
    player = players[player_name]
    player.owner = owner_name
    if not is_waiver_trade:
        if player.cost > 5:
            player.cost = 5
