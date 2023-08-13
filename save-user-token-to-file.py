# This script automates saving a user access token object from the osu! API to a JSON file.

from osuExchange.auth import get_access_token, OAuth2Scope
from json import JSONDecoder, dump
from sys import argv, stderr

if len(argv) != 3:
    stderr.write('Required args: <client info file> <token file>\n<client into file> must be a JSON file with your osu! client id, secret, and redirect URI\n')
    exit(1)
    
CLIENT_INFO_FILENAME = argv[1]
TOKEN_FILENAME = argv[2]

# read in client info
with open(CLIENT_INFO_FILENAME, 'r') as file:
	client_info = JSONDecoder().decode(file.read())

# authenticate and get the user access token object
access_token = get_access_token(**client_info, scopes=[OAuth2Scope.PUBLIC, OAuth2Scope.IDENTIFY])
# if you need more scopes, add more to the scopes parameter

# write the user access token object as a JSON object
with open(TOKEN_FILENAME, 'w') as file:
	dump(vars(access_token), file, indent='\t')
