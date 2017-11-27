import json
from TwitterAPI import TwitterAPI

with open('config.json') as data_file:    
        data = json.load(data_file)

consumer_key = data["consumer-key"]
consumer_secret = data["consumer-secret"]
access_token_key = data["access-token-key"]
access_token_secret = data["access-token-secret"]

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

r = api.request('friends/ids')
for id in r:
	r = api.request('friendships/destroy',{'user_id': id})
	if r.status_code == 200:
		status = r.json()
		print('Unfollowed %s' % status['screen_name'])