#! python3

from yahoo_oauth import OAuth2
oauth = OAuth2(None, None, from_file='private.json')

if not oauth.token_is_valid():
    oauth.refresh_access_token()

