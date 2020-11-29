#! python3

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

for gl_id in game_league_ids:
    g_id, l_id = game_league_ids[gl_id]
    req_url = url+"/league/"+g_id+".l."+l_id
    r = oauth.session.get(req_url, params={"format": "json"})
    print(r.text)

#req_url = url + "/league/399.l.414682"
#r = oauth.session.get(req_url, params={"format": "json"})
#print(r.status_code)
#print(r.text)
#
#req_url = url + "/league/390.l.655835"
#r = oauth.session.get(req_url, params={"format": "json"})
#print(r.status_code)
#print(r.text)
