#! python

import re
import json
import xmltodict

from yahoo_oauth import OAuth2

oauth = OAuth2(None, None, from_file='private.json')

if not oauth.token_is_valid():
    oauth.refresh_access_token()

url = "https://fantasysports.yahooapis.com/fantasy/v2"
game_league_ids = {
    '2020': ('403', '6851')
}


# Query Yahoo API for data specified by url path
def yahoo_query(url_path):

    # Request Yahoo API for parameters
    req_url = url + url_path
    r = oauth.session.get(req_url)

    # Convert xml response into json
    xmlstring = r.text
    xmlstring = re.sub(' xmlns="[^"]+"', '', xmlstring, count=1)
    xmldict = xmltodict.parse(xmlstring)
    xmldict = xmldict['fantasy_content']['league']  # Remove added headers
    jsonstring = json.dumps(xmldict, indent=4)
    return jsonstring


# Get all transactions for the league
def get_league_transactions(game_id, league_id):

    # Construct the url
    l_id = game_id + ".l." + league_id
    url_path = "/league/" + l_id + "/transactions"

    # Request and return data
    league_transactions = yahoo_query(url_path)
    return league_transactions


print(get_league_transactions("403", "6851"))
