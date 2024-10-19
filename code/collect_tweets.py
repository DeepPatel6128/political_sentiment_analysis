# import tweepy
# import configparser

# config = configparser.ConfigParser()
# config.read('config.ini')

# # getting all the keys

# api_key = config['twitter']['api_key']
# api_secret_key = config['twitter']['api_secret_key']
# access_token = config['twitter']['access_token']
# access_token_secret = config['twitter']['access_token_secret']

# print(api_key)

# #authentication 
# auth = tweepy.OAuthHandler(api_key, api_secret_key)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)

# public_tweets = api.home_timeline()

# print(public_tweets)

import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(to:BharatSolankee) lang:en until:2018-01-07 since:2017-11-09"
tweets = []
limits = 20

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limits:
        break
    else :
        tweets.append([tweet.date, tweet.user.username ,tweet.content])

df = pd.DataFrame(tweets, columns=["Date", "User", "Tweet"])

print(df)

df.to_csv('bharatSolanki.csv')
