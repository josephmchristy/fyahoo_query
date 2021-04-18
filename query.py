#! python

import sys
import os
import re
import json
import xmltodict

from yahoo_oauth import OAuth2

game_league_ids = {
    '2020': ('403', '6851')
}


class FYahooQuery():

    def __init__(self, league_id, game_code="nfl", season="2020", game_id=None):
        self.league_id = str(league_id)
        self.game_code = game_code
        self.season = str(season)
        self.url = "https://fantasysports.yahooapis.com/fantasy/v2"

        # Set up auth
        self.oauth = OAuth2(None, None, from_file=(os.path.join(sys.path[0], 'private.json')))
        if not self.oauth.token_is_valid():
            self.oauth.refresh_access_token()

        # Retrieve the game id if none was passed in
        if game_id:
            self.game_id = str(game_id)
        else:
            self.game_id = self.get_game_id()

        # Construct the league key
        self.league_key = self.game_id + ".l." + self.league_id

    # Query Yahoo API for requested data specified by url path
    def fyahoo_query(self, url_path, req_data):

        # Request Yahoo API for parameters
        req_url = self.url + url_path
        r = self.oauth.session.get(req_url)

        # Convert xml response into json
        xmlstring = r.text
        xmlstring = re.sub(' xmlns="[^"]+"', '', xmlstring, count=1)
        xmldict = xmltodict.parse(xmlstring)
        xmldict = xmldict['fantasy_content'][req_data]  # Remove added headers
        jsonstring = json.dumps(xmldict, indent=4)
        return jsonstring

    # Get game key
    def get_game_id(self):

        # Request json data
        url_path = "/games;game_codes=" + self.game_code + ";seasons=" + self.season
        fyahoo_data = self.fyahoo_query(url_path, "games")

        # Extract game id from json data
        fyahoo_data = json.loads(fyahoo_data)
        game_id = fyahoo_data["game"]["game_key"]
        return game_id

    # Get all teams the league
    def get_league_teams(self):
        url_path = "/league/" + self.league_key + "/teams"
        return self.fyahoo_query(url_path, "league")

    # Get all settings for the league
    def get_league_settings(self):
        url_path = "/league/" + self.league_key + "/settings"
        return self.fyahoo_query(url_path, "league")

    # Get all transactions for the league
    def get_league_transactions(self):
        url_path = "/league/" + self.league_key + "/transactions"
        return self.fyahoo_query(url_path, "league")

    # Get team statistics by given week
    def get_team_stats(self, team_id, week="current"):
        team_key = self.league_key + ".t." + str(team_id)
        url_path = "/team/" + team_key + "/stats;type=week;week=" + str(week)
        return self.fyahoo_query(url_path, "team")
