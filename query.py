#! python

import xml.etree.ElementTree as ET
import re
import datetime
import json
import xmltodict
import pprint

from yahoo_oauth import OAuth2

oauth = OAuth2(None, None, from_file='private.json')

if not oauth.token_is_valid():
    oauth.refresh_access_token()

url = "https://fantasysports.yahooapis.com/fantasy/v2"
game_league_ids = {
    '2020': ('403', '6851')
}


def yahoo_query(g_id='403', l_id='6851', t_id=None,
                param1='league', param2='transactions'):
    
    # Request Yahoo API for parameters
    league_id = g_id+'.l.'+l_id
    if t_id:
        league_id = league_id+'.t.'+t_id
    req_url = url + "/"+param1+"/"+league_id +\
              "/"+param2
    r = oauth.session.get(req_url)

    # Convert xml response into json
    xmlstring = r.text
    xmlstring = re.sub(' xmlns="[^"]+"', '', xmlstring, count=1)
    xmldict = xmltodict.parse(xmlstring)
    xmldict = xmldict['fantasy_content']['league']  # Remove added headers
    jsonstring = json.dumps(xmldict, indent=4)
    return jsonstring

yahoo_query()
