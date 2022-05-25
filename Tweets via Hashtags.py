# -*- coding: utf-8 -*-
"""
Created on Tue May 24 13:40:37 2022

@author: Enqey De-Ben Rockson
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 24 12:59:01 2022

@author: Enqey De-Ben Rockson
"""

import tweepy
import pandas as pd 

consumer_key = "OvupU7UuLbg9fCXSgUtOAQ2FA"
consumer_secret = "oMDNQPJQvLEYKyBzf3XbV87EGw7QoeRQzz0nCQ74UL1B2RANfA"
access_token = "2615042796-Obc9jn7th9xUa1IitSiXVZMNcxZviqv1hxUHm9Z"
access_secret = "nvE6lVY9HgPs7N6OIR4OSblH0UyMMtauNgJA13dBJwNzM"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
    
keyword = '2022'
limit =  300
api = tweepy.API(auth)
tweets = tweepy.Cursor(api.search, q=keyword, count=200, tweet_mode='extended').items(limit)

cols = ['user', 'Tweet']
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])
    
df = pd.DataFrame(data, columns= cols)

print(df)