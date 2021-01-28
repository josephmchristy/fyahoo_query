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
league_id = '403.l.6851'

req_url = url + "/league/"+league_id +\
          "/transactions"
r = oauth.session.get(req_url)
xmlstring = r.text
xmlstring = re.sub(' xmlns="[^"]+"', '', xmlstring, count=1)
xmldict = xmltodict.parse(xmlstring)
xmldict = xmldict['fantasy_content']['league']
for transaction in xmldict['transactions']['transaction']:
    print(transaction['transaction_key'])
jsonstring = json.dumps(xmldict, indent=4)
filename = 'txt_hockey.txt'
with open(filename, 'w+') as x:
    x.write(jsonstring)
