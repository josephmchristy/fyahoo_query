#! python

import json
import pprint
import xml.etree.ElementTree as ET
from xml.dom import minidom
import re

from yahoo_oauth import OAuth2
oauth = OAuth2(None, None, from_file='private.json')

if not oauth.token_is_valid():
    oauth.refresh_access_token()

url = "https://fantasysports.yahooapis.com/fantasy/v2"
game_league_ids = {
    '2014': ('331', '635114'),
    '2015': ('348', '521087'),
    '2016': ('359', '691742'),
    '2017': ('371', '675894'),
    '2018': ('380', '966146'),
    '2019': ('390', '655835'),
    '2020': ('399', '414682')
        }
num_league_years = len(game_league_ids)
num_teams = []

#for gl_id in game_league_ids:
#    g_id, l_id = game_league_ids[gl_id]
#    req_url = url+"/league/"+g_id+".l."+l_id
#    r = oauth.session.get(req_url, params={"format": "json"})
#    league_info = json.loads(r.text)
#    num_teams.append(league_info['fantasy_content']['league'][0]['num_teams'])

#for num in num_teams:
#    print('Number of teams: {}'.format(num))  


req_url = url+"/team/"+"399.l.414682.t.2/roster/players"
r = oauth.session.get(req_url)
xmlstring = r.text
pprint.pprint(xmlstring)
xmlstring = re.sub(' xmlns="[^"]+"', '', xmlstring, count=1)
root = ET.fromstring(xmlstring)
for player in root.iter('player'):
    player_name = player.find('name')
    player_fullname = player_name.find('full')
    print(player_fullname.text)


#req_url = url + "/league/399.l.414682"
#r = oauth.session.get(req_url, params={"format": "json"})
#print(r.status_code)
#print(r.text)
#
#req_url = url + "/league/390.l.655835"
#r = oauth.session.get(req_url, params={"format": "json"})
#print(r.status_code)
#print(r.text)
